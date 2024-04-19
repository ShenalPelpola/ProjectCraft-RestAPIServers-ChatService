import os
from flask import Flask
from api.chat_api import chat_blueprint

app = Flask(__name__)

environment = os.getenv('ENV')

if environment == "production" :
    app.config.from_object('config.ProductionConfig')
elif environment == "test" :
    app.config.from_object('config.TestConfig')
else:
    app.config.from_object('config.DevelopmentConfig')
     
app.register_blueprint(chat_blueprint)

if __name__ == "__main__":
    app.run()