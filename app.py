import os
from flask import Flask, render_template, request, redirect
from azure.cosmos import CosmosClient

app = Flask(_name_)

# Securely getting our keys from Azure Environment Variables
URL = os.environ.get("COSMOS_URL")
KEY = os.environ.get("COSMOS_KEY")
DATABASE_NAME = 'TaskDatabase'
CONTAINER_NAME = 'Tasks'

# Initialize the Cosmos Client
client = CosmosClient(URL, KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

@app.route('/')
def index():
    # Fetch all tasks from the database
    tasks = list(container.read_all_items())
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    if task_content:
        # Create a new JSON document in Cosmos DB
        container.create_item(body={'id': str(os.urandom(4).hex()), 'task': task_content})
    return redirect('/')

if _name_ == '_main_':
    app.run()
