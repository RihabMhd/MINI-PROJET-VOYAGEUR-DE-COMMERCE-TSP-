def charger_villes(chemin):
    with open(chemin,'r') as file:
        content=file.readline()
        mylist=[tuple(content.split()) for content in file]
        mylist.insert(0,len(mylist))
        print(mylist)
print(charger_villes('./villes.txt'))
#--------------------------------------------------------------------------
def distance(villeA, villeB):
    