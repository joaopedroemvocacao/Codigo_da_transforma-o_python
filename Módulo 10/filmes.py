import requests

API_KEY_TMDB = "SUA_CHAVE_TMDB_AQUI"

def buscar_filme(nome_filme):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY_TMDB}&query={nome_filme}&language=pt-BR"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        
        if dados['results']:
            filme = dados['results'][0]
            print(f"\nTítulo: {filme['title']}")
            print(f"Data de lançamento: {filme['release_date']}")
            print(f"Sinopse: {filme['overview'][:200]}...")
        else:
            print("Filme não encontrado!")
            
    except:
        print("Erro na requisição")

# Testando
nome = input("Digite o nome do filme: ")
buscar_filme(nome)