#En este script se desarrollan todas las funciones para consultar los datos en la pokeapi.co
import requests
import json
# Función para obtener datos de un Pokémon
def obtener_datos_pokemon(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        pokemon_stats = {
            'name': datos_pokemon['name'],
            'type': [tipo['type']['name'] for tipo in datos_pokemon['types']],
            'hp': datos_pokemon['stats'][0]['base_stat'],
            'attack': datos_pokemon['stats'][1]['base_stat'],
            'defense': datos_pokemon['stats'][2]['base_stat'],
            'weight': datos_pokemon['weight']
        }
        return pokemon_stats
    else:
        print(f'Error al obtener datos del Pokémon {pokemon_id}')
        print("Parece que el número que estás ingresando es muy largo. Prueba con otro más corto.")
        return None

# Función para obtener evoluciones de un Pokémon
def obtener_evoluciones(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}/'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos_especie = respuesta.json()
        evoluciones = {
            'name': datos_especie['evolves_from_species']['name'] if 'evolves_from_species' in datos_especie and datos_especie['evolves_from_species'] else 'none',
            'evoluciona a': datos_especie['name'],
                    }
        return evoluciones
    else:
        print(f'Error al obtener evoluciones del Pokémon {pokemon_id}')
        print("Parece que el número que estás ingresando es muy largo. Prueba con otro más corto.")
        return None
    
# Función para obtener datos de un ítem
def obtener_datos_item(item_id):
    url = f'https://pokeapi.co/api/v2/item/{item_id}/'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos_item = respuesta.json()
        item = {
            'name': datos_item['name'],
            'id': datos_item['id'],
            'cost': datos_item['cost'],
            'fling_power': datos_item['fling_power'],
            'effect': datos_item['effect_entries'][0]['effect']
        }
        return item
    