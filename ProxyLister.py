# Import
try:
    import sys
    import time

    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
except ImportError as err:
    print(f"Import Error in {sys.argv[0]}:\n{err}")
    sys.exit()


class ProxyLister:
    def __init__(self):
        print("""
        Using \"ProxyLister\" in this project.
          _____                     _      _     _            
         |  __ \                   | |    (_)   | |           
         | |__) | __ _____  ___   _| |     _ ___| |_ ___ _ __ 
         |  ___/ '__/ _ \ \/ / | | | |    | / __| __/ _ \ '__|
         | |   | | | (_) >  <| |_| | |____| \__ \ ||  __/ |   
         |_|__ |_|  \___/_/\_\\\__, |______|_|___/\__\___|_|__ 
         |  _ \                __/ |   /\             |  \/  |
         | |_) |_   _         |___/   /  \    _______ | \  / |
         |  _ <| | | |               / /\ \  |_  / _ \| |\/| |
         | |_) | |_| |              / ____ \  / / (_) | |  | |
         |____/ \__, |             /_/    \_\/___\___/|_|  |_|
                 __/ |                                        
                |___/                                         
        """)

    def get_proxies(self, piece, path="chromedriver.exe", countries=None, ping=None, port=None, types=None, anon=None):
        countries = f"country={''.join([c.upper() for c in countries])}" if countries else ""
        ping = f"ping={ping}" if ping else ""
        port = f"ports={port}" if port else ""
        types = f"type={''.join(types)}" if types else ""
        anon = f"anon={anon}" if anon else ""

        parameters = f"?{'&'.join([countries, ping, port, types, anon])}"

        self.URL = f"https://hidemy.name/en/proxy-list/{parameters}#list"

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-logging")
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--headless")

        self.driver = webdriver.Chrome(executable_path=path, options=self.options)

        self.driver.get(self.URL)

        time.sleep(0.5)

        td_length = 7
        tr_xpath = "/html/body/div[1]/div[4]/div/div[4]/table/tbody/tr[{}]"
        td_xpath = f"{tr_xpath}/td[{'{}'}]"

        self.proxies = []

        for y in range(2, piece + 1):
            proxy = []

            for x in range(1, td_length + 1):
                try:
                    proxy.append(self.driver.find_element_by_xpath(td_xpath.format(y, x)).text)
                except NoSuchElementException:
                    break

            proxy = {
                "IP": proxy[0],
                "PORT": proxy[1],
                "PROXY": f"{proxy[0]}:{proxy[1]}",
                "COUNTRY&CITY": proxy[2],
                "SPEED": int(proxy[3].replace(" ms", "")),
                "TYPES": proxy[4].split(", "),
                "ANONYMITY": int(proxy[5].replace("no", "1").replace("Low", "2").replace("Average", "3").replace("High", "4"))
            }

            self.proxies.append(proxy)

        return self.proxies
