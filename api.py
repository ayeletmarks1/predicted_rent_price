from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    neighborhood = request.form.get('neighborhood')
    room_num = request.form.get('room_num')
    area = request.form.get('area')
    floor = request.form.get('floor')

    prediction = random.randint(4000, 12000)

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
