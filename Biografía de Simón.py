from bs4 import BeautifulSoup
import requests
import re


url = 'https://www.cervantesvirtual.com/portales/simon_bolivar/autor_biografia/'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.select_one('article#maincontent h2')
    paragraphs = soup.select('article#maincontent p.tabular')

    content = ""


    if title:
        content += f"Título del artículo: {title.text.strip()}\n\n"

    for paragraph in paragraphs:
        content += f"{paragraph.text.strip()}\n\n"

  
else:
    print(f"Error al acceder a la URL. Código de estado: {response.status_code}")
    
text = '\n'.join(
    re.sub(r'\s+', ' ', linea).strip() for linea in content.splitlines()
)

print(text)

SimonBolivar = 'Biografia Simon Bolivar.txt'
with open(SimonBolivar, 'w', encoding='utf-8') as archivo:
    archivo.write(text)