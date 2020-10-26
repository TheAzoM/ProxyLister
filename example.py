import ProxyLister
import pprint

proxy_lister = ProxyLister.ProxyLister() # Create class
proxies = proxy_lister.get_proxies(100, types=["hs"], ping="1000") # and scrape proxies

pprint.pprint(proxies)
