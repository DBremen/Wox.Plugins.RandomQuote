import requests
import textwrap
from wox import Wox

icons_dir = './icons/'

def randomquote(query):
    results = []
    send_data = {
        'method': 'getQuote',
        'format': 'json',
        'lang': 'en'}
    r = requests.post('http://api.forismatic.com/api/1.0/', send_data).json()
    # alternatives:
    # https://talaikis.com/api/quotes/random/
    # https://favqs.com/api/qotd
    currquote = textwrap.fill(r['quoteText'], width=90)
    author = r['quoteAuthor']
    if not author:
        author = "Anonymous"
    print()
    results.append({
        "Title": currquote + " ~ " + author,
        "SubTitle": '',
        "IcoPath": icons_dir + "quote.png"
    })
    if not results:
        results.append({
            "Title": 'Not found',
            "SubTitle": '',
            "IcoPath": icons_dir + "quote.png"
        })
    return results

class RandomQuote(Wox):
    def query(self, query):
        return randomquote(query)


if __name__ == "__main__":
    RandomQuote()
