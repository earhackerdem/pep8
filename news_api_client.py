import urllib.request
import urllib.parse
import json
from errors import APIKeyError

BASE_URL = 'https://newsapi.org/v2/everything'

def newsapi_client(api_key,query,timeout=30,retries=3):
    query_string = urllib.parse.urlencode({"q": query,'apiKey':api_key})
    url = f"{BASE_URL}?{query_string}"

    try:
        with urllib.request.urlopen(url,timeout=timeout) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except urllib.error.HTTPError:
        raise APIKeyError('Ocurrio un error, no se pudo conectar con la API')
    return f"News api: {query} con timeout {timeout}"

def guardian_client(api_key, section,from_date,timeout=30,retries=3):
    return f"{section} desde {from_date}, con timeout {timeout}"


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
