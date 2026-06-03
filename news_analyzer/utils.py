def get_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }
    
def get_articles_by_source(articles: list[dict], source: str) -> list[dict]:
    #print({article["source"]["name"] for article in articles})
    return list(filter(
        lambda article: article['source']['name'].lower() == source.lower(),
        articles
    ))
    

def get_reading_time(article: dict) -> dict:
    """Calcula el timepo de lectura"""
    minutes = len(article['content']) //200 + 1
    article['reading_time'] = minutes
    return article