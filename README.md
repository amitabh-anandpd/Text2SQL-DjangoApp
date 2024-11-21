# Text2SQL-DjangoApp

A Django-based web application that converts natural language queries into SQL queries and executes them on user-uploaded datasets. This project integrates a fine-tuned T5 NLP model for accurate text-to-SQL conversion and supports REST API for seamless interaction between the frontend and backend.

## **Features**
- Upload Database: Users can upload their own database (in .db format).
- Text-to-SQL Conversion: Converts natural language queries into SQL queries using a fine-tuned T5 Transformer model.
- SQL Execution: Executes generated SQL queries on uploaded datasets and displays results.
- REST API: Provides endpoints for dataset upload, query generation, and result fetching.
- Model Training Notebook: Includes a Jupyter Notebook to fine-tune the T5 model on **WikiSQL** dataset, and evaluate its performance.

## Requirements
The project requires the following dependencies:

- Python 3.8+
- Django 4.2+
- PyTorch
- Hugging Face Transformers
- Pandas
