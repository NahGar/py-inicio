#pip install beautifulsoup4
#pip install lxml
#pip install requests
import bs4
import requests

url = 'https://escueladirecta-blog.blogspot.com/2024/07/copia-o-referencia.html'
resultado = requests.get(url)

sopa = bs4.BeautifulSoup(resultado.text,'lxml')

print(sopa.select('title')[0].getText())
for p in sopa.select('p'):
    print(p.getText())


url = 'https://www.bhu.com.uy/ahorro/yo-ahorro?gad_campaignid=21030242397'

sopa = bs4.BeautifulSoup(requests.get(url).text,'lxml')
item = sopa.select('#block-cotizaciones-2 > div > div > div > div:nth-child(2)')[0].getText()
print(item)

# obteniendo imagenes
resultado = requests.get('https://escueladirecta.com')
sopa = bs4.BeautifulSoup(resultado.text,'lxml')

imagen_src = sopa.select('.course-box-image-container > img')[0]['src']
print(item)
imagen = requests.get(imagen_src)

f = open('imagen_descargada.jpg','wb')
f.write(imagen.content)
f.close()