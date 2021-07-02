import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/charizard')
charizard_data = r.get('https://pokeapi.co/api/v2/pokemon/charizard')
if data.status_code == 200:
    charizard_data = data.json()

    

Charizard = {
    'name' : charizard_data['species']['name'],
    'abilities': [charizard_data['abilities'][0]['ability']['name'],charizard_data['abilities'][1]['ability']['name']],
    'weight' : charizard_data['weight'], 
    'types' : [charizard_data['types'][0]['type']['name'],charizard_data['types'][1]['type']['name']]
}
print(Charizard)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/caterpie')
caterpie_data = r.get('https://pokeapi.co/api/v2/pokemon/caterpie')
if data.status_code == 200:
    caterpie_data = data.json()

    


caterpie = {
    'name' : caterpie_data['species']['name'],
    'abilities': [caterpie_data['abilities'][0]['ability']['name'],caterpie_data['abilities'][1]['ability']['name']],
    'weight' : caterpie_data['weight'], 
    'types' : caterpie_data['types'][0]['type']['name'],
}
print(caterpie)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/vulpix')
vulpix_data = r.get('https://pokeapi.co/api/v2/pokemon/vulpix')
if data.status_code == 200:
    vulpix_data = data.json()

    

vulpix = {
    'name' : vulpix_data['species']['name'],
    'abilities': [vulpix_data['abilities'][0]['ability']['name'],vulpix_data['abilities'][1]['ability']['name']],
    'weight' : vulpix_data['weight'], 
    'types' : vulpix_data['types'][0]['type']['name']
}
print(vulpix)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/vaporeon')
vaporeon_data = r.get('https://pokeapi.co/api/v2/pokemon/vaporeon')
if data.status_code == 200:
    vaporeon_data = data.json()



vaporeon = {
    'name' : vaporeon_data['species']['name'],
    'abilities': [vaporeon_data['abilities'][0]['ability']['name'],vaporeon_data['abilities'][1]['ability']['name']],
    'weight' : vaporeon_data['weight'], 
    'types' : vaporeon_data['types'][0]['type']['name']
}
print(vaporeon)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/cyndaquil')
cyndaquil_data = r.get('https://pokeapi.co/api/v2/pokemon/cyndaquil')
if data.status_code == 200:
    cyndaquil_data = data.json()

    

cyndaquil = {
    'name' : cyndaquil_data['species']['name'],
    'abilities': [cyndaquil_data['abilities'][0]['ability']['name'],cyndaquil_data['abilities'][1]['ability']['name']],
    'weight' : cyndaquil_data['weight'], 
    'types' : cyndaquil_data['types'][0]['type']['name']
}
print(cyndaquil)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/sudowoodo')
sudowoodo_data = r.get('https://pokeapi.co/api/v2/pokemon/sudowoodo')
if data.status_code == 200:
    sudowoodo_data = data.json()



sudowoodo = {
    'name' : sudowoodo_data['species']['name'],
    'abilities': [sudowoodo_data['abilities'][0]['ability']['name'],sudowoodo_data['abilities'][1]['ability']['name'],sudowoodo_data['abilities'][2]['ability']['name']],
    'weight' : sudowoodo_data['weight'], 
    'types' : sudowoodo_data['types'][0]['type']['name']
}
print(sudowoodo)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/rayquaza')
rayquaza_data = r.get('https://pokeapi.co/api/v2/pokemon/rayquaza')
if data.status_code == 200:
    rayquaza_data = data.json()



rayquaza = {
    'name' : rayquaza_data['species']['name'],
    'abilities': rayquaza_data['abilities'][0]['ability']['name'],
    'weight' : rayquaza_data['weight'], 
    'types' : [rayquaza_data['types'][0]['type']['name'],rayquaza_data['types'][1]['type']['name']]
}
print(rayquaza)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/aggron')
aggron_data = r.get('https://pokeapi.co/api/v2/pokemon/aggron')
if data.status_code == 200:
    aggron_data = data.json()



aggron = {
    'name' : aggron_data['species']['name'],
    'abilities': [aggron_data['abilities'][0]['ability']['name'],aggron_data['abilities'][1]['ability']['name'],aggron_data['abilities'][2]['ability']['name']],
    'weight' : aggron_data['weight'], 
    'types' : [aggron_data['types'][0]['type']['name'],aggron_data['types'][1]['type']['name']]
}
print(aggron)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/mudkip')
mudkip_data = r.get('https://pokeapi.co/api/v2/pokemon/mudkip')
if data.status_code == 200:
    mudkip_data = data.json()



mudkip = {
    'name' : mudkip_data['species']['name'],
    'abilities': [mudkip_data['abilities'][0]['ability']['name'],mudkip_data['abilities'][1]['ability']['name']],
    'weight' : mudkip_data['weight'], 
    'types' : mudkip_data['types'][0]['type']['name']
}
print(mudkip)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/miltank')
miltank_data = r.get('https://pokeapi.co/api/v2/pokemon/miltank')
if data.status_code == 200:
    miltank_data = data.json()



miltank = {
    'name' : miltank_data['species']['name'],
    'abilities': [miltank_data['abilities'][0]['ability']['name'],miltank_data['abilities'][1]['ability']['name'],miltank_data['abilities'][2]['ability']['name']],
    'weight' : miltank_data['weight'], 
    'types' : miltank_data['types'][0]['type']['name']
}
print(miltank)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/hitmonlee')
hitmonlee_data = r.get('https://pokeapi.co/api/v2/pokemon/hitmonlee')
if data.status_code == 200:
    hitmonlee_data = data.json()



hitmonlee = {
    'name' : hitmonlee_data['species']['name'],
    'abilities': [hitmonlee_data['abilities'][0]['ability']['name'],hitmonlee_data['abilities'][1]['ability']['name'],hitmonlee_data['abilities'][2]['ability']['name']],
    'weight' : hitmonlee_data['weight'], 
    'types' : hitmonlee_data['types'][0]['type']['name']
}
print(hitmonlee)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/teddiursa')
teddiursa_data = r.get('https://pokeapi.co/api/v2/pokemon/teddiursa')
if data.status_code == 200:
    teddiursa_data = data.json()



teddiursa = {
    'name' : teddiursa_data['species']['name'],
    'abilities': [teddiursa_data['abilities'][0]['ability']['name'],teddiursa_data['abilities'][1]['ability']['name'],teddiursa_data['abilities'][2]['ability']['name']],
    'weight' : teddiursa_data['weight'], 
    'types' : teddiursa_data['types'][0]['type']['name']
}
print(teddiursa)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/eevee')
eevee_data = r.get('https://pokeapi.co/api/v2/pokemon/eevee')
if data.status_code == 200:
    eevee_data = data.json()



eevee = {
    'name' : eevee_data['species']['name'],
    'abilities': [eevee_data['abilities'][0]['ability']['name'],eevee_data['abilities'][1]['ability']['name'],eevee_data['abilities'][2]['ability']['name']],
    'weight' : eevee_data['weight'], 
    'types' : eevee_data['types'][0]['type']['name']
}
print(eevee)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/jolteon')
jolteon_data = r.get('https://pokeapi.co/api/v2/pokemon/jolteon')
if data.status_code == 200:
    jolteon_data = data.json()



jolteon = {
    'name' : jolteon_data['species']['name'],
    'abilities': [jolteon_data['abilities'][0]['ability']['name'],jolteon_data['abilities'][1]['ability']['name']],
    'weight' : jolteon_data['weight'], 
    'types' : jolteon_data['types'][0]['type']['name']
}
print(jolteon)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/gyarados')
gyarados_data = r.get('https://pokeapi.co/api/v2/pokemon/gyarados')
if data.status_code == 200:
    gyarados_data = data.json()



gyarados = {
    'name' : gyarados_data['species']['name'],
    'abilities': [gyarados_data['abilities'][0]['ability']['name'],gyarados_data['abilities'][1]['ability']['name']],
    'weight' : gyarados_data['weight'], 
    'types' : [gyarados_data['types'][0]['type']['name'],gyarados_data['types'][1]['type']['name']]
}
print(gyarados)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/scyther')
scyther_data = r.get('https://pokeapi.co/api/v2/pokemon/scyther')
if data.status_code == 200:
    scyther_data = data.json()



scyther = {
    'name' : scyther_data['species']['name'],
    'abilities': [scyther_data['abilities'][0]['ability']['name'],scyther_data['abilities'][1]['ability']['name'],scyther_data['abilities'][2]['ability']['name']],
    'weight' : scyther_data['weight'], 
    'types' : [scyther_data['types'][0]['type']['name'],scyther_data['types'][1]['type']['name']]
}
print(scyther)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/hitmonchan')
hitmonchan_data = r.get('https://pokeapi.co/api/v2/pokemon/hitmonchan')
if data.status_code == 200:
    hitmonchan_data = data.json()



hitmonchan = {
    'name' : hitmonchan_data['species']['name'],
    'abilities': [hitmonchan_data['abilities'][0]['ability']['name'],hitmonchan_data['abilities'][1]['ability']['name'],hitmonchan_data['abilities'][2]['ability']['name']],
    'weight' : hitmonchan_data['weight'], 
    'types' : hitmonchan_data['types'][0]['type']['name']
}
print(hitmonchan)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/gastly')
gastly_data = r.get('https://pokeapi.co/api/v2/pokemon/gastly')
if data.status_code == 200:
    gastly_data = data.json()



gastly = {
    'name' : gastly_data['species']['name'],
    'abilities': gastly_data['abilities'][0]['ability']['name'],
    'weight' : gastly_data['weight'], 
    'types' : [gastly_data['types'][0]['type']['name'],gastly_data['types'][1]['type']['name']]
}
print(gastly)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/haunter')
haunter_data = r.get('https://pokeapi.co/api/v2/pokemon/haunter')
if data.status_code == 200:
    haunter_data = data.json()



haunter = {
    'name' : haunter_data['species']['name'],
    'abilities': haunter_data['abilities'][0]['ability']['name'],
    'weight' : haunter_data['weight'], 
    'types' : [haunter_data['types'][0]['type']['name'],haunter_data['types'][1]['type']['name']]
}
print(haunter)

import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/gengar')
gengar_data = r.get('https://pokeapi.co/api/v2/pokemon/gengar')
if data.status_code == 200:
    gengar_data = data.json()



gengar = {
    'name' : gengar_data['species']['name'],
    'abilities': gengar_data['abilities'][0]['ability']['name'],
    'weight' : gengar_data['weight'], 
    'types' : [gengar_data['types'][0]['type']['name'],gengar_data['types'][1]['type']['name']]
}
print(gengar)