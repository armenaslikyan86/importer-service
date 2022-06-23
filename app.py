from flask import Flask, request, json
from importer_service import ImporterService

app = Flask(__name__)
importerService = ImporterService();



@app.route('/')
def home():
    return 'Importer service is running!'

@app.route('/api/layers', methods=['GET'])
def get_layers():
    data = importerService.get_layers()
    return app.response_class(data, mimetype='application/json')


if __name__ == '__main__':
    app.run()
