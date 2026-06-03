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
