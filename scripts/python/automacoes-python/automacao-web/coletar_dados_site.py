"""
Coleta básica de dados de uma página web (exemplo educacional)
"""

import requests
from bs4 import BeautifulSoup

URL = "https://example.com"

def coletar():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    titulos = [h.text for h in soup.find_all("h1")]

    for t in titulos:
        print(t)

if __name__ == "__main__":
    coletar()
