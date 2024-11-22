from django.shortcuts import render, redirect
from .forms import SQLFileUploadForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import os
import sqlite3
from django.conf import settings
from .mlModel import Model

model = Model()

def main(request):
    selected_db = request.GET.get('db')
    if selected_db:
        db_path = os.path.join(settings.MEDIA_ROOT, 'sql_files', selected_db)
        request.session['uploaded_file_path'] = db_path
    if request.method == "POST":
        nl_query = request.POST.get('nlInput', '')
        query_string = f"?nlQuery={nl_query}"
        return HttpResponseRedirect(reverse('display_sql') + query_string)

    return render(request, 'main.html')

def display_sql(request):
    nl_query = request.GET.get('nlQuery', '')
    if nl_query.lower() == "select all" or nl_query.lower() == "all":
        sql_query = "SELECT * FROM table"
    else:
        sql_query = model.predict(nl_query)
    file_path = request.session.get('uploaded_file_path')

    if not nl_query:
        return render(request, 'search.html', {'error': 'No query entered.'})

    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_name = cursor.fetchone()[0]
        words = sql_query.split()
        sql_query = ' '.join([table_name if word == 'table' else word for word in words])
        for i in sql_query:
            if i=="$":
                sql_query.replace("", "( $ )")
        for i in nl_query.split():
            if i=="all":
                words = sql_query.split()
                words[1] = "*"
                sql_query = ' '.join(word for word in words)
        df = pd.read_sql_query(sql_query, conn)
        table_data = df.values.tolist()
        columns = df.columns
        conn.close()

        return render(request, 'search.html', {
            'sqlQuery': nl_query,
            'table_data': table_data,
            'columns': columns,
        })
    except Exception as e:
        return render(request, 'search.html', {
            'error': f"Error executing query: {str(e)}"
        })

def pdf1(request):
    return render(request, 'pdf.html')

def pdf2(request):
    return render(request, 'pdf2.html')

def upload_sql(request):
    if request.method == 'POST':
        form = SQLFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            sql_file = request.FILES['sql_file']
            file_path = os.path.join(settings.MEDIA_ROOT, 'sql_files', sql_file.name)

            # Save the file to media/sql_files/
            with open(file_path, 'wb+') as destination:
                for chunk in sql_file.chunks():
                    destination.write(chunk)

            # Connect to the uploaded SQLite database
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()

            # Get the first table's name
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table_name = cursor.fetchone()[0]  # Fetch the tables

            conn.close()

            # Save the path and table name in session
            request.session['uploaded_file_path'] = file_path
            request.session['table_name'] = table_name

            return redirect('display_sql')  # Redirect to display the data
    else:
        form = SQLFileUploadForm()

    return render(request, 'upload_sql.html', {'form': form})

DATABASE_DIR = os.path.join(settings.MEDIA_ROOT, 'sql_files')

def list_databases(request):
    try:
        # Get all files with .db extension in the directory
        databases = [f for f in os.listdir(DATABASE_DIR) if f.endswith('.db')]
    except FileNotFoundError:
        databases = []

    return render(request, 'database_list.html', {'databases': databases})


'''working nl_query (these are some of the queries that work with my 25k model)- 
        name who salary more than 5000
        select all
        all
        list <column> of those who <numerical_col> are greater than 50
        list names of who score math_score equal 50
        '''