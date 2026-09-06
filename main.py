import math
def charger_villes(chemin):
    with open(chemin,'r') as file:
        content=file.readline()
        mylist=[tuple(content.split()) for content in file]
        return mylist
# print(charger_villes('./villes.txt'))

#--------------------------------------------------------------------------
def distance(villeA, villeB):
    distance1=(float(villeA[-2]),float(villeA[-1]))
    distance2=(float(villeB[-2]),float(villeB[-1]))
    return round(math.dist(distance1,distance2),2)


# print(distance(("Paris",48.8567,2.3522),("Bordeaux",44.84,-0.58)))

#-------------------------------------------------------------------------------
def itineraire_greedy(villes):
    ville1=villes[0]
    villes_visitees=[ville1]
    while(len(villes)>len(villes_visitees)):
        distances=[]
        for ville in villes:
            if ville not in villes_visitees:
                d=distance(ville1,ville)
                distances.append((d,ville))
        distance_min,ville_prochain=min(distances)
        villes_visitees.append(ville_prochain)
        ville1=ville_prochain
    return villes_visitees
        

villes=charger_villes('./villes.txt')
print(itineraire_greedy(villes))