#pip install beautifulsoup4
#pip install lxml
#pip install requests
import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
titulos_con_4_estrellas = []
titulos_con_5_estrellas = []

#for pagina in range(1,51):
for pagina in range(1,5):

    print(f'Obteniendo página {pagina}...')

    resultado = requests.get(url_base.format(pagina))
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')

    libros = sopa.select('article.product_pod')

    for libro in libros:
        titulo = libro.select('h3 > a')
        if len(libro.select('.star-rating.Four')) != 0:
            titulos_con_4_estrellas.append(f"{titulo[0]['title']} ({pagina})")
        if len(libro.select('.star-rating.Five')) != 0:
            titulos_con_5_estrellas.append(f"{titulo[0]['title']} ({pagina})")

print(f'Se encontraron {len(titulos_con_4_estrellas)} libros con 4 estrellas.')
for titulo in titulos_con_4_estrellas:
    print(f"\t{titulo}")

print(f'\nSe encontraron {len(titulos_con_5_estrellas)} libros con 5 estrellas.')
for titulo in titulos_con_5_estrellas:
    print(f"\t{titulo}")
