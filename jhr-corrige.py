# coding : utf-8 

import csv 
import requests 
from bs4 import BeautifulSoup 

url= "http://www.contracts-contrats.phac-aspc.gc.ca/phac-aspc/pd-dp/cd-dc.nsf/WEBbypurposeF?OpenView&RP=2016-2017~1&Count=3000&lang=fra&"

fichier = "contrats-sante-JHR.csv"

entetes = {
    "User-Agent":"Beatrice Roy-Brunet-Pour une emission",
    "From":"beatriceroybrunet@gmail.com"
}

contenu = requests.get(url,headers=entetes)
page= BeautifulSoup(contenu.text,"html.parser")
# print(page)

i=0 

for ligne in page.find_all("tr"):
    if i !=0: 
        
        # print(ligne)
        lien = ligne.a.get("href")
        # print(lien)
        # lien = "http://www.contracts-contrats.phac-aspc.gc.ca/phac-aspc/pd-dp/cd-dc.nsf/"+ lien ### Ici, il fallait raccourcir la première partie de l'hyperlien
        hyperlien = "http://www.contracts-contrats.phac-aspc.gc.ca"+ lien 
        print("*"*80)
        print(hyperlien)

        contenu2 = requests.get(hyperlien,headers=entetes)
        page2 = BeautifulSoup(contenu2.text,"html.parser")

        sante = []
    
        sante.append(hyperlien)

        for item in page2.find_all("tr"):
             # print(item)
             # sante.append(item.td.text)

            if item.td is not None:
                sante.append(item.td.text)
            else:
                # santee.append(None) ### Ici, tu avais écrit "santee" au lieu de "sante"; c'est peut-être pour cela que ton script plantait...
                sante.append(None)
    
        print(sante)
    
        pomme = open(fichier,"a")
        ministere = csv.writer(pomme)
        ministere.writerow(sante)

    i += 1
