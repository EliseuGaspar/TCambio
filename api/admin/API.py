from flask import Flask, jsonify
from admin.webscraping import Scraping
from admin.database.gerenciador import Gerenciador

API = Flask(__name__)

@API.route('/')
def index():
    return {"msg":'API no ar!'}

@API.route('/tcambio/BMA')
def banco_atlantico():
    response = Scraping.BMA(Scraping)
    return jsonify(response)

@API.route('/tcambio/BNI')
def banco_bni():
    response = Scraping.BNI(Scraping)
    return jsonify(response)

@API.route('/tcambio/BAI')
def banco_bai():
    response = Scraping.BAI(Scraping)
    return jsonify(response)

@API.route('/tcambio/ilustration')
def ilus():
    respo = Scraping.ilustration(Scraping)
    return respo

@API.route('/tcambio/actualizacao')
def actualizacao():
    response = Gerenciador.Versao(Gerenciador)
    return jsonify(response)

@API.route('/tcambio/cadastrar/<string:email>',methods=['GET'])
def cadastrar(email):
    response = Gerenciador.Cadastrar(Gerenciador,email)
    return jsonify(response)