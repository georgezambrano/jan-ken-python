import random
import pdb
import time
from time import sleep
from flask import Flask, jsonify
from flask import render_template, request

app = Flask(__name__)

class Entidad:
	def __init__(self,nombre):
		self.nombre = nombre
	def __eq__(self,other):
		return (self.nombre == other.nombre)
	def __gt__(self,other):
		if (other.nombre in self.debil):
			return True
		elif (other.nombre in self.fuerte):
			return False
	def mostrar(self):
		return "%s" % self.nombre


class Papel(Entidad):
	def __init__(self):
		Entidad.__init__(self,"Papel")
		self.debil = ['Piedra','Spock']
		self.fuerte = ['Tijera','Lagarto']

class Tijera(Entidad):
	def __init__(self):
		Entidad.__init__(self,"Tijera")
		self.debil = ['Papel','Lagarto']
		self.fuerte = ['Spock','Piedra']

class Piedra(Entidad):
	def __init__(self):
		Entidad.__init__(self,"Piedra")
		self.debil = ['Lagarto','Tijera']
		self.fuerte = ['Spock','Papel']

class Lagarto(Entidad):
	def __init__(self):
		Entidad.__init__(self,"Lagarto")
		self.debil = ['Papel','Spock']
		self.fuerte = ['Tijera','Piedra']

class Spock(Entidad):
	def __init__(self):
		Entidad.__init__(self,"Spock")
		self.debil = ['Piedra','Tijera']
		self.fuerte = ['Lagarto','Papel']

depo = ['Papel', 'Piedra', 'Tijera', 'Lagarto', 'Spock'] 

def seleccion(x):
	if x == "Papel":
		return Papel()
	elif x == "Piedra":
		return Piedra()
	elif x == "Tijera":
		return Tijera()
	elif x == "Lagarto":
		return Lagarto()
	elif x == "Spock":
		return Spock()

@app.route("/")
def index():
	return render_template("app.html")

@app.route("/resultado")
def resultado():
	jugador = seleccion(request.args.get('jugador','',type = str))
	pc = random.choice([Papel(), Tijera(), Piedra(), Lagarto(), Spock()])
	if (jugador == pc):
		resultado = "Empate"
	elif (jugador > pc):
		resultado = "Ganaste =).\n%s vence a %s" % (jugador.mostrar(), pc.mostrar())
	elif (jugador < pc):
		resultado = "Perdiste =(.\n%s vence a %s" % (pc.mostrar(), jugador.mostrar())
	else:
		resultado = "Ocurrio algo raro con jugador = %s y pc = %s" % (jugador.mostrar(), pc.mostrar())
	return jsonify(jugador = jugador.mostrar(), pc = pc.mostrar(), resultado = resultado)

if __name__ == "__main__":
	app.run()

