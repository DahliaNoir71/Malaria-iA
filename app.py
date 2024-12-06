from flask import Flask
from routes.file_routes import file_routes
from routes.predict_routes import predict_routes
import os

# Créez une instance de Flask
app = Flask(__name__)

# Charger la configuration depuis le fichier config.py
app.config.from_object('config.Config')

# Enregistrement des Blueprints
app.register_blueprint(file_routes)
app.register_blueprint(predict_routes)

if __name__ == '__main__':
    app.run(debug=True)