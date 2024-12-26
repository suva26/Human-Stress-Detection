from flask import Flask, render_template, request, redirect, url_for, flash
import train_model
import predict_model
import visualize

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        train_model.train()
        flash('Model trained successfully!')
        return redirect(url_for('home'))
    return render_template('train.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = [
            float(request.form['sr']),
            float(request.form['rr']),
            float(request.form['t']),
            float(request.form['lm']),
            float(request.form['bo']),
            float(request.form['rem']),
            float(request.form['sh']),
            float(request.form['hr'])
        ]
        prediction = predict_model.predict(data)
        return redirect(url_for('result', prediction=prediction))
    return render_template('predict.html')

@app.route('/result')
def result():
    prediction = request.args.get('prediction')
    return render_template('result.html', prediction=prediction)

@app.route('/visualize')
def visualize_data():
    visual_data = visualize.create_all_visualizations()
    return render_template('visualize.html', visual_data=visual_data)

if __name__ == '__main__':
    app.run(debug=True)
