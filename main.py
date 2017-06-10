import requests
from wox import Wox

icons_dir = './icons/'
class Main(Wox):
    def request(self, url):
        if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
            proxies = {
                "http": "http://{}:{}".format(self.proxy.get("server"), self.proxy.get("port")),
                "https": "http://{}:{}".format(self.proxy.get("server"), self.proxy.get("port"))}
            return requests.get(url, proxies=proxies)
        else:
            return requests.get(url)

    def query(self, query):
        results = []
        send_data = {
            'method': 'getQuote',
            'format': 'json',
            'lang': 'en'}
        r = requests.post('http://api.forismatic.com/api/1.0/', send_data).json()
        # alternatives:
        # https://talaikis.com/api/quotes/random/
        # https://favqs.com/api/qotd
        # currquote = textwrap.fill(r['quoteText'], width=90)
        currquote = r['quoteText']
        author = r['quoteAuthor']
        if not author:
            author = "Anonymous"
        print()
        results.append({
            "Title": currquote,
            "SubTitle": author,
            "IcoPath": icons_dir + "quote.png"
        })
        if not results:
            results.append({
                "Title": 'Not found',
                "SubTitle": '',
                "IcoPath": icons_dir + "quote.png"
            })
        return results

if __name__ == "__main__":
    Main()
