from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def mainpage():
    return "Welcome"

@app.route("/home")
def homedemo():
    return render_template('index.html')

if __name__ == '__main__':
    app.run("127.0.0.1", port=5000, debug=True)
