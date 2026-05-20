import requests

API_KEY = "15735d42d3ea07a38a578cdace22054c"
CIDADE = "São Paulo"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    
    dados = resposta.json()
    
    temperatura = dados['main']['temp']
    condicao = dados['weather'][0]['description']
    
    print(f"Cidade: {CIDADE}")
    print(f"Temperatura atual: {temperatura}°C")
    print(f"Condição climática: {condicao}")
    
except requests.exceptions.ConnectionError:
    print("Erro: Sem conexão com a internet.")
except requests.exceptions.HTTPError:
    print("Erro: Cidade não encontrada ou API key inválida.")
except Exception as e:
    print(f"Erro inesperado: {e}")