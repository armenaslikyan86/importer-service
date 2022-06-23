from flask import Flask, request
from importer_service import ImporterService
import json

app = Flask(__name__)
importerService = ImporterService();



@app.route('/')
def home():
    return 'Importer service is running!'

@app.route('/api/tasks')
def get_tasks():
    return importerService.get_tasks()


if __name__ == '__main__':
    app.run()
