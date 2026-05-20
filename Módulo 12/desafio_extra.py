
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/somar', methods=['GET'])
def somar_api():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({'resultado': a + b})

@app.route('/dividir', methods=['GET'])
def dividir_api():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 1))
    
    if b == 0:
        return jsonify({'erro': 'Divisão por zero!'}), 400
    
    return jsonify({'resultado': a / b})

if __name__ == '__main__':
    app.run(debug=True)
    
    # arquivo: test_api.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_somar(client):
    resposta = client.get('/somar?a=5&b=3')
    assert resposta.status_code == 200
    assert resposta.json['resultado'] == 8

def test_somar_negativos(client):
    resposta = client.get('/somar?a=-2&b=5')
    assert resposta.json['resultado'] == 3

def test_dividir(client):
    resposta = client.get('/dividir?a=10&b=2')
    assert resposta.json['resultado'] == 5

def test_dividir_por_zero(client):
    resposta = client.get('/dividir?a=10&b=0')
    assert resposta.status_code == 400
    assert 'erro' in resposta.json

def test_somar_sem_parametros(client):
    resposta = client.get('/somar')
    assert resposta.json['resultado'] == 0