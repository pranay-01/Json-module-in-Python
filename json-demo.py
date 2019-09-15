import json

with open('pokeverse.json') as poke:
    dat = json.load(poke)
for pokemon in dat['pokemon']:
    print(pokemon)
for pokemon in dat['pokemon']:
    del pokemon['isEvoluted']
with open('new_pokeverse.json','w') as poke:
    json.dump(dat,poke,indent=2)        
