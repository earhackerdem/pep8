# main.py Todo el código en un archivo
"""
Sistema de análisis de noticias con APIS múltiples
"""

# PEP 8: Configuracion centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIME_OUT = 30

MAX_TRIES = 3

DEFAULT_LANGUAGE = "es"  # PEP8 Comillas dobles para strings


def guardian_client(api_key, section,from_date,timeout=30,retries=3):
    return f"{section} desde {from_date}, con timeout {timeout}"


# PEP 8 Utilidades comunes del proyecto - funciones snake_case
def clean_text(text):
    # PEP8 4 espacios para indentacion, no tabs
    """Limpia y normalizatexto"""
    if not text:
        return ""
    return text.strip().lower()


# PEP8 Dobles lineas en blanco entre funciones para separar lógica
def validate_api_key(api_key):
    """Valida que la API KEY tenga formato correcto"""
    return len(api_key) > 10 and api_key.isanum()


def process_article_data(raw_data):
    """Procesa datos crudos de articulo"""
    pass



def ejemplo_args(api_key,*args):
    print(f"api_key: {api_key}")
    print(f"args: {args}")
    print(f"type: {type(args)}")
    print("=====")

ejemplo_args("API_KEY_VALUE","parametro",'aca')
ejemplo_args("API_KEY_VALUE","Mundo")

def ejemplo_kwargs(**kwargs):
    print(f"kwargs: {type(kwargs)}")
    print(f'kwargs: {kwargs}')
    print("======")

ejemplo_kwargs(api_key='DEMO',query='Noticias de Python', timeout=30,retries=3)

API_KEY = '7506b5608f2a47759e319524956f9055'

BASE_URL = 'https://newsapi.org/v2/everything'

import urllib.request
import urllib.parse
import json

def newsapi_client(api_key,query,timeout=30,retries=3):
    query_string = urllib.parse.urlencode({"q": query,'apiKey':api_key})
    
    url = f"{BASE_URL}?{query_string}"

    print(url)
    with urllib.request.urlopen(url,timeout=timeout) as response:
        data = response.read().decode('utf-8')
        return json.loads(data)
        
    return f"News api: {query} con timeout {timeout}"


def fetch_news(api_name, *args, **kwargs):
    """
    Funcion flexible para conectar con la API
    """

    base_config = {
        "timeout": 30,
        "retries": 3
    }

    config = {
        **base_config,
        **kwargs
    }

    api_clients = {
        "newsapi": newsapi_client,
        "guardian" : guardian_client
    }

    client = api_clients[api_name]
    return client(*args,**config)

response_data = fetch_news('newsapi',api_key=API_KEY,query="Python")
for article in response_data['articles']:
    print(article["title"])