from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {"title": "Hola que tasl", "message": "Buenos dias a todos menos a los fanaticos del Real Madrid, Visca el Barca"}
    return render_template('index.html', data=data)

@app.route('/capstone')
def capstone():
    data = {
        "title": "intento de proyecto capstone",
        "description": "lista de cosas para hacer:",
        "items": ["Diseñar la base de datos", "Crear API REST", "Conectar Front-End"]
    }
    return render_template('CS.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
