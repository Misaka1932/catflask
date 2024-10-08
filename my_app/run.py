from my_app import app
import webbrowser

webbrowser.open_new('http://localhost:5000')
app.run(debug=True)