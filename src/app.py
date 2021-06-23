import os

from flask import Flask
from flask_restful import Api

from clothes_detector import ClothesDetector

app = Flask(__name__)
api = Api(app)

api.add_resource(ClothesDetector, '/detect')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
