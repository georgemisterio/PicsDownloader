from bs4 import BeautifulSoup
import requests

# 1. Si ya tienes el HTML
html = '''
<div class="th nopop">
    <a href="https://pics.p/2915/387995/47.jpg" class="com-link fancybox" data-fancybox="gallery">
        <img class="thumb" src="https://pics.tranny.one/work/thumb/2915/387995/47.jpg" height="320" width="240" alt="no image">
    </a>
</div>
'''

# 2. Si es una URL real
# html = requests.get("https://tu-pagina.com").text

soup = BeautifulSoup(html, "html.parser")

# 3. Sacar todos los href de los <a>
hrefs = [a["href"] for a in soup.find_all("a", href=True)]

print(hrefs)