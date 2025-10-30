

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola Mundo 1"

    # segundo commit añado un 1

if __name__ == '__main__':
    app.run(host='localhost', port=8080)

