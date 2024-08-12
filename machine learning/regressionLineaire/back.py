from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model from .pkl file
with open('./model.pkl', 'rb') as file:
	model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
	data = request.get_json()
	predictions = model.predict(data)
	return jsonify(predictions.tolist())

if __name__ == '__main__':
	app.run()
