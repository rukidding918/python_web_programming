from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/works')
def name():
    return render_template('1mincoding-bbc-covid19/1mincoding-bbc-covid19/index.html')



if __name__ == '__main__':
    app.run(debug=True)
    # app.run()