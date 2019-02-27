from flask import Flask
from flask import request #para trabajar con parametros
app = Flask(__name__)


@app.route('/')
def index():
	return 'Hola mundo'


@app.route('/salida')
def saluda():
	return 'Otro mensaje'

@app.route('/params')
def params():
	param = request.args.get('nombre','') #nombre parametro, valor por defecto
	return 'hola {}'.format(param)

if __name__ == '__main__':
	app.run(debug = True, port = 8000)