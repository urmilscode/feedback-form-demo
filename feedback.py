from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Propulsion academy feedback form</h1>'

#variable
@app.route('/home', methods=['GET', 'POST'])
def home():
    courses = ['python', 'datascience', 'blockchain']
    return render_template('example.html', student='propulsion academy. urmil', courses=courses)

if __name__ == '__main__':
    app.run(debug=True) 