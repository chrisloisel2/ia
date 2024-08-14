from flask import Flask, request, jsonify
import tensorflow as tf
# Create the Flask app

app = Flask(__name__) # __name__ is module name


model = tf.keras.models.load_model('model.h5')

# Backend API Routes

@app.route('/api')
def acceuil():
	return "Welcome to the Backend API"

@app.route('/api/echo', methods=['POST'])
def echo():
	data = request.json
	x1 = data['x1']
	x2 = data['x2']
	x3 = data['x3']
	x4 = data['x4']
	x5 = data['x5']
	prevision = model.predict([[x1, x2, x3, x4, x5]])
	print(prevision.tolist()[0])
	return jsonify(prevision.tolist()[0])

if __name__ == '__main__':
	app.run(debug=True)
