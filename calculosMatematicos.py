import requests
from openpyxl import Workbook, load_workbook
import matplotlib.pyplot as plt
import os
import json

# Función para generar un reporte estadístico y gráficas

def generar_reporte(datos):
    # Graficar algunas estadísticas
    nombres = [pokemon['name'] for pokemon in datos]
    
    # Modificamos para manejar diferentes estructuras de datos
    hp = [pokemon.get('hp',0) for pokemon in datos]
    attack = [pokemon.get('attack',0) for pokemon in datos]
    defense = [pokemon.get('defense',0) for pokemon in datos]
    weight = [pokemon.get('weight', 0) for pokemon in datos]

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.bar(nombres, hp, color='red')
    plt.title('HP de Pokémon')
    plt.xlabel('Pokémon')
    plt.ylabel('HP')

    plt.subplot(2, 2, 2)
    plt.bar(nombres, attack, color='blue')
    plt.title('Ataque de Pokémon')
    plt.xlabel('Pokémon')
    plt.ylabel('Ataque')

    plt.subplot(2, 2, 3)
    plt.bar(nombres, defense, color='green')
    plt.title('Defensa de Pokémon')
    plt.xlabel('Pokémon')
    plt.ylabel('Defensa')

    plt.subplot(2, 2, 4)
    plt.bar(nombres, weight, color='orange')
    plt.title('Peso de Pokémon')
    plt.xlabel('Pokémon')
    plt.ylabel('Peso')

    plt.tight_layout()
    plt.show()

def calcular_promedio_stats(datos):
    if not datos:
        print("No hay datos de Pokémon para calcular el promedio de stats.")
        return None

    total_hp = sum(pokemon.get('hp', 0) for pokemon in datos)
    total_attack = sum(pokemon.get('attack', 0) for pokemon in datos)
    total_defense = sum(pokemon.get('defense', 0) for pokemon in datos)
    total_pokemons = len(datos)

    promedio_hp = total_hp / total_pokemons
    promedio_attack = total_attack / total_pokemons
    promedio_defense = total_defense / total_pokemons

    return {
        'Promedio HP': promedio_hp,
        'Promedio Ataque': promedio_attack,
        'Promedio Defensa': promedio_defense
    }
#FUNCIONES PARA CÁLCULOS MATEMÁTICOS
def pokemon_mas_fuerte(datos):
    if not datos:
        print("No hay datos de Pokémon para determinar el Pokémon más fuerte.")
        return None

    # Calculamos el promedio de stats para cada Pokémon
    promedios = calcular_promedio_stats(datos)

    # Encontramos el Pokémon con el mayor promedio
    pokemon_fuerte = max(datos, key=lambda x: (x.get('hp', 0) + x.get('attack', 0) + x.get('defense', 0)) / 3)

    return {
        'Pokemon más fuerte': pokemon_fuerte['name'],
        'Promedio de stats': (pokemon_fuerte.get('hp', 0) + pokemon_fuerte.get('attack', 0) + pokemon_fuerte.get('defense', 0)) / 3
    }

def pokemon_mas_debil(datos):
    if not datos:
        print("No hay datos de Pokémon para determinar el Pokémon más débil.")
        return None

    # Calculamos el promedio de stats para cada Pokémon
    promedios = calcular_promedio_stats(datos)

    # Encontramos el Pokémon con el menor promedio
    pokemon_debil = min(datos, key=lambda x: (x.get('hp', 0) + x.get('attack', 0) + x.get('defense', 0)) / 3)

    return {
        'Pokemon más débil': pokemon_debil['name'],
        'Promedio de stats': (pokemon_debil.get('hp', 0) + pokemon_debil.get('attack', 0) + pokemon_debil.get('defense', 0)) / 3
    }