from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)

        if username == 'admin' and password == '123456':
            return render_template('index.html')
        else:
            return "Wrong PassWord"
    else:
        return "Not Post"
    
if __name__ == '__main__':
    app.run("127.0.0.1", port=5000, debug=True)