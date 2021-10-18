import dill
import pandas as pd
import numpy as np
import os
#dill._dill._reverse_typemap['ClassType'] = type
import flask
import logging
from logging.handlers import RotatingFileHandler

import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from razdel import tokenize
from nltk.stem import SnowballStemmer
nltk.download('stopwords')
nltk.download('punkt')
from sklearn.feature_extraction.text import TfidfVectorizer

app = flask.Flask(__name__)
model = None

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def load_model(model_paht):
	# загружаем обученную модель
	global model
	with open(model_path, 'rb') as f:
		model = dill.load(f)
	print(model)

model_path = "/app/app/models/logreg_pipeline_.dill"
load_model(model_path)


@app.route("/", methods=["GET"])
def general():
	return "Welcome to comment classification process. Please use 'http://172.20.10.3:8183/classify' to POST"

@app.route("/classify", methods=["POST"])
def classify():
	# Инициализируем словарь data который будет выводиться
	data = {"success": False}

	# убедимся, что все загружено верно
	if flask.request.method == "POST":
		comment = ""
		request_json = flask.request.get_json()
		if request_json['comment']:
			comment = request_json['comment']
		logger.info(f'Data: comment={comment}')

		try:
			class_num = model.predict(comment)
			# Скорректируем значения классов, исходя из найденной наилучшей границы разбиения
			if int(class_num) > 0.36:
				class_num = 1
			else:
				class_num = 0

		except AttributeError as e:
			logger.warning(f'Exception: {str(e)}')
			data['predictions'] = str(e)
			data['success'] = False
			return flask.jsonify(data)

		data["predictions"] = class_num
		data["comment"] = comment

		# индикатор, что все прошло успешно
		data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server

if __name__ == "__main__":
	print(("* Loading the model and Flask starting server..."
		   "please wait until server has fully started"))
	port = int(os.environ.get('PORT', 8183))
	app.run(host='0.0.0.0', debug=True, port=port)

