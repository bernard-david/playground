from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def working():
    print("Working")
    return "Working"

@app.route('/play')
def play():
    print("Working")
    return render_template('index.html', times = 3, color = "cornflowerblue")

@app.route('/play/<int:x>')
def more_boxes(x):
    print("Working")
    return render_template('index.html', times = x, color = "cornflowerblue")

@app.route('/play/<int:x>/<string:color>')
def more_colored_boxes(x, color):
    print("Working")
    return render_template('index.html', times = x, color = color)



if __name__=="__main__":
    app.run(debug=True)