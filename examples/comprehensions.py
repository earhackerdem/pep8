

def extract_titles_traditional(articles):
    """Extrae solo los titulos usando un for"""
    titles = []
    for article in articles:
        if len(article["title"]) > 10:
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae solo los titulos usando un comprehension"""
    return [article["title"] for article in articles if len(article["title"]) > 10]


print(extract_titles_traditional(sample_articles))
print("==================")
print(extract_titles(sample_articles))

print("==================")


def extract_article_summaries(articles):
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"] > 1)
    }


def list_from_articles(articles):
    set = []
    for article in articles:
        name = article["source"]["name"]
        if name not in set:
            set.append(name)
    return set


# print(extract_article_summaries(sample_articles))


def get_sources_traditional(articles):
    sources = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


# {expression for member in iterable [if condition]}


def get_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }

print(get_sources_traditional(sample_articles))
print('--------------------------')
print(get_sources(sample_articles))


def categorizar_tradicional(articles):
    sources = get_sources(articles)

    results = {
    }

    for source in sources:
        if source not in results:
            results[source]= []
        for article in articles:
            if source == article.get('source').get('name'):
                results[source].append(article)
    return results

print(categorizar_tradicional(sample_articles))


def categorize(articles)
    sources = get_sources(articles)
    return {
        sources: [
            article
            for article in articles
            if source == article.get('source').get('name')
        ]
        for source in sources
    }