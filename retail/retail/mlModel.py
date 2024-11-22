import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

_cached_model = None

def load_model():
        global _cached_model
        if _cached_model is None:
            _cached_model = T5ForConditionalGeneration.from_pretrained('t5-base')
            try:
                _cached_model.load_state_dict(torch.load('/path/to/model.pt'))
            except Exception as e:
                print(e)
                try:
                    _cached_model.load_state_dict(torch.load('model.pt', map_location=torch.device('cpu'))) # load on cpu if no gpu available
                except Exception as e:
                    print(e)
                    exit()
            _cached_model.eval()
        return _cached_model


class Model():
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained('t5-base', model_max_length=1024)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = load_model().to(self.device)

    def predict(self, input_text):
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt').to(self.device)
        output = self.model.generate(input_ids, max_length=100, num_beams=5, early_stopping=True)
        decoded_output = self.tokenizer.decode(output[0], skip_special_tokens=True)

        return str(decoded_output)
