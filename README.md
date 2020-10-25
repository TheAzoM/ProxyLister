# ProxyLister
This project gets proxies with selenium.

# Example
```py
import ProxyLister

proxy_lister = ProxyLister.ProxyLister()
proxies = proxy_lister.get
proxies = proxy_lister.get_proxies(5)

print(proxies)
>>> [ {'IP': '11.11.111.11', 'PORT': '8080', 'COUNTRY&CITY': 'Indonesia', 'SPEED': 100, 'TYPES': ['HTTP'], 'ANONYMITY': 1}, .. ]
```
"get_proxies" function gets 7 parameters.
> piece, path="chromedriver.exe", countries=None, ping=None, port=None, types=None, anon=None
