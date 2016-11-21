# coding : utf-8 

import csv 
import requests 
from bs4 import BeautifulSoup

fichier = "seao.csv"

# Très bonne idée que de vouloir moissonner des données du SEAO! :)
# Cette information est disponible ici:
# https://www.donneesquebec.ca/recherche/fr/dataset/systeme-electronique-dappel-doffres-seao
# Mais c'est en format XML et ça peut être difficile à déchiffrer...
url= "https://www.seao.ca/Recherche/Avis/Adjudication?SubCategoryCode=G21&callingPage=4&CatChoosen=1&Opp=0"
# Par ailleurs, l'URL ci-dessus ne te donne que les 10 premiers avis sur 158.
# J'ai essayé de les ramasser tous en créant une boucle qui va de 1 à 16:

for p in range(1,17):

    # On transforme p (qui est un nombre) en chaîne de caractère ("string"):
    p = str(p)

    # On ajoute «p» à la fin de cet URL:
    url = "https://www.seao.ca/Recherche/Avis/Adjudication?SubCategoryCode=G21&callingPage=4&CatChoosen=1&Opp=0#p=" + p
    # print(url)

    entetes = {
        "User-Agent":"Beatrice Roy-Brunet-Pour une emission",
        "From":"beatriceroybrunet@gmail.com"
    }

    contenu = requests.get(url,headers=entetes)
    page= BeautifulSoup(contenu.text,"html.parser")

    i=0

    for ligne in page.find_all("tr"):
        if i !=0:
            lien = ligne.a.get("href")
            # print(lien)
            numeroAvis = ligne.a.text
            donneurOuvrage = ligne.b.text.strip()

            hyperlien = "https://www.seao.ca" + lien ### Ici aussi, il fallait raccourcir le début de l'hyperlien
            print("#"*50)
            print(numeroAvis)
            print(donneurOuvrage)
            print(hyperlien)

# Mais finalement, j'ai réalisé que ça ne fonctionne pas.
# Ici, c'est un cas où il faudrait «simuler un humain» avec l'aide de selenium...
# ce qui est plus ardu...

        i += 1
