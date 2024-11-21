import pandas as pd
data1 = pd.read_json("C:/Users/amita/Desktop/Intro to AI/IntroToAI Project/Dataset/dev.json")
data2 = pd.read_json("C:/Users/amita/Desktop/Intro to AI/IntroToAI Project/Dataset/spider-realistic.json")
#data3 = pd.read_json("C:/Users/amita/Desktop/Intro to AI/IntroToAI Project/Dataset/tables.json.csv")

data = pd.concat([data1, data2])

cleaned = pd.DataFrame()
list_retail = ["customer"]
data['question'] = data['question'].str.lower()
'''for i in range(len(data)):
    for j in range(len(list_retail)):
        try:
            if list_retail[j] in data['question'][i]:
                try:
                    cleaned.loc[len(cleaned)] = data[i]
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)'''

#print(len(cleaned))
data.to_csv("C:/Users/amita/Desktop/Intro to AI/IntroToAI Project/Dataset/cleaned2.csv", index=False)