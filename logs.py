from flask import Flask
from src.logger import logging
from src.exception import CustomException
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing our exception file")
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)
        logging.info("We are Testing Logging file ")
        return "Welcome to shivpuri"

if __name__ == '__main__':
    app.run(debug=True)
