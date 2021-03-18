from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Propulsion academy feedback form</h1>'

#variable
@app.route('/home', methods=['GET', 'POST'])
def home(place):
    return '<h2>You are on the' + place  + 'page!!</h2>'

if __name__ == '__main__':
    app.run(debug=True) 