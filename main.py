import requests
from openpyxl import Workbook, load_workbook
import matplotlib.pyplot as plt
import os
import json
from consultaApi import obtener_datos_pokemon, obtener_datos_item, obtener_evoluciones
from calculosMatematicos import generar_reporte, calcular_promedio_stats, pokemon_mas_debil, pokemon_mas_fuerte
from almacenamientoDatos import actualizar_datos_en_excel, actualizar_datos_evoluciones_en_excel, actualizar_datos_item_en_excel, guardar_datos_en_txt, guardar_pokemon_mas_debil_en_excel, guardar_pokemon_mas_fuerte_en_excel,   guardar_promedio_stats_en_excel, guardar_ticket_en_excel, guardar_ticket_en_txt
from lecturaDatos import leerexcel, leertexto, load_workbook

carrito=[]

# Menú de opciones
def menu():
    print("Seleccione una opción:")
    print("1. Consultar Pokémon")
    print("2. Consultar Items")
    print("3. Consultar Evoluciones")
    print("4. Generar gráficas")
    print("5. Cálculos matemáticos")
    print('6. Leer archivos')
    print("0. Salir")

if __name__ == "__main__":
    datos_pokemon_lista = []
    datos_item_lista = []
    datos_evoluciones_lista = []

    while True:
        menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "0":
            print("Hasta luego, pokeamigo!:D")
            break
        elif opcion == "1":
            # Consultar datos de un Pokémon
            pokemon_id = int(input("Ingrese el número del Pokémon para consultar: "))
            datos_pokemon = obtener_datos_pokemon(pokemon_id)
            if datos_pokemon:
                print(f"\nDatos del Pokémon {pokemon_id}:\n{json.dumps(datos_pokemon, indent=2)}")
                datos_pokemon_lista.append(datos_pokemon)

                # Preguntar al usuario si desea guardar la información en un archivo Excel
                respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()
                if respuesta_guardar_excel == 'si' or respuesta_guardar_excel == 's':
                    nombre_archivo_excel = input("Ingrese el nombre del archivo Excel (con extensión .xlsx): ")
                    actualizar_datos_en_excel([datos_pokemon], nombre_archivo_excel)
                    print(f"Datos almacenados en {nombre_archivo_excel}.")

                # Preguntar al usuario si desea guardar la información en un archivo TXT
                respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()
                if respuesta_guardar_txt == 'si' or respuesta_guardar_txt == 's':
                    nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                    guardar_datos_en_txt([datos_pokemon], nombre_archivo_txt)
                    print(f"Datos almacenados en {nombre_archivo_txt}.")

            else:
                print(f"No se pudo obtener información del Pokémon {pokemon_id}.")
        elif opcion == "2":
            # Consultar datos de un ítem
            item_id = input("Ingrese el ID del ítem que desea consultar: ")
            datos_item = obtener_datos_item(item_id)
            if datos_item:
                print(f"\nDatos del ítem {item_id}:\n{json.dumps(datos_item, indent=2)}")
                datos_item_lista.append(datos_item)

                # Preguntar al usuario si desea guardar la información en un archivo Excel
                respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()
                if respuesta_guardar_excel == 'si' or respuesta_guardar_excel == 's':
                    nombre_archivo_excel = input("Ingrese el nombre del archivo Excel (con extensión .xlsx): ")
                    actualizar_datos_item_en_excel(datos_item_lista, nombre_archivo_excel)
                    print(f"Datos almacenados en {nombre_archivo_excel}.")

                # Preguntar al usuario si desea guardar la información en un archivo TXT
                respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()
                if respuesta_guardar_txt == 'si' or respuesta_guardar_txt == 's':
                    nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                    guardar_datos_en_txt(datos_item_lista, nombre_archivo_txt)
                    print(f"Datos almacenados en {nombre_archivo_txt}.")

                # Pregunta al usuario si desea agregar el ítem al carrito de compras
                respuesta_agregar_carrito = input("¿Deseas agregar este ítem a tu carrito de compras? (Sí/No): ").lower()
                if respuesta_agregar_carrito == 'si' or respuesta_agregar_carrito == 's':
                    # Calcula el costo con IVA del 16% y agrega el ítem al carrito
                    costo = datos_item.get('cost', 0)
                    costo_con_iva = costo * 1.16
                    carrito.append({'name': datos_item['name'], 'cost': costo, 'cost_with_iva': costo_con_iva})

            else:
                print(f"No se pudo obtener información del ítem {item_id}.")
        elif opcion == "3":
            # Consultar evoluciones de un Pokémon
            pokemon_id = int(input("Ingrese el número del Pokémon para consultar evoluciones: "))
            evoluciones = obtener_evoluciones(pokemon_id)
            if evoluciones:
                print(f"\nEvoluciones del Pokémon {pokemon_id}:\n{json.dumps(evoluciones, indent=2)}")
                datos_evoluciones_lista.append(evoluciones)

                # Preguntar al usuario si desea guardar la información en un archivo Excel
                respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()
                if respuesta_guardar_excel == 'si' or respuesta_guardar_excel == 's':
                    nombre_archivo_excel = input("Ingrese el nombre del archivo Excel (con extensión .xlsx): ")
                    actualizar_datos_evoluciones_en_excel([evoluciones], nombre_archivo_excel)
                    print(f"Datos almacenados en {nombre_archivo_excel}.")

                # Preguntar al usuario si desea guardar la información en un archivo TXT
                respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()
                if respuesta_guardar_txt == 'si' or respuesta_guardar_txt == 's':
                    nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                    guardar_datos_en_txt([evoluciones], nombre_archivo_txt)
                    print(f"Datos almacenados en {nombre_archivo_txt}.")

            else:
                print(f"No se encontraron evoluciones para el Pokémon {pokemon_id}.")
        elif opcion == "4":
            # Generar reporte estadístico y gráficas
            if datos_pokemon_lista:
                generar_reporte(datos_pokemon_lista)
            else:
                print("No hay datos de Pokémon para generar gráficas.")
        elif opcion == "5":
            # Cálculos matemáticos
            print("Seleccione un cálculo matemático:")
            print("1. Promedio de stats de Pokémon consultados")
            print("2. Pokémon más fuerte")
            print("3. Pokémon más débil")
            print("4. Ticket de compras de items")
            seleccion_calculo = input("Ingrese el número de la opción deseada: ")

            if seleccion_calculo == "1":
                resultados_calculo = calcular_promedio_stats(datos_pokemon_lista)
                if resultados_calculo:
                    print("\nResultados del cálculo:")
                    for key, value in resultados_calculo.items():
                        print(f"{key}: {value}")

                    respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()
                    if respuesta_guardar_excel == 'si' or respuesta_guardar_excel == 's':
                       resultados_promedio_stats = calcular_promedio_stats(datos_pokemon_lista)
                       guardar_promedio_stats_en_excel(resultados_promedio_stats, 'promedio_stats.xlsx')
                       print(f"Datos almacenados en 'promedio_stats.xlsx'")

                    respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()
                    if respuesta_guardar_txt == 'si' or respuesta_guardar_txt == 's':
                        nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                        guardar_datos_en_txt([resultados_calculo], nombre_archivo_txt)
                        print(f"Datos almacenados en {nombre_archivo_txt}.")

            elif seleccion_calculo == "2":
                resultado_calculo = pokemon_mas_fuerte(datos_pokemon_lista)
                if resultado_calculo:
                    print("\nResultados del cálculo:")
                    for key, value in resultado_calculo.items():
                        print(f"{key}: {value}")

                    respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()
                    if respuesta_guardar_excel == 'si' or respuesta_guardar_excel == 's':
                       resultado_pokemon_fuerte = pokemon_mas_fuerte(datos_pokemon_lista)
                       guardar_pokemon_mas_fuerte_en_excel(resultado_pokemon_fuerte, 'pokemon_fuerte.xlsx')
                       print(f"Datos almacenados en 'pokemon_fuerte.xlsx'")

                    respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()
                    if respuesta_guardar_txt == 'si' or respuesta_guardar_txt == 's':
                        nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                        guardar_datos_en_txt([resultado_calculo], nombre_archivo_txt)
                        print(f"Datos almacenados en {nombre_archivo_txt}.")

            elif seleccion_calculo == "3":
                resultado_calculo = pokemon_mas_debil(datos_pokemon_lista)
                if resultado_calculo:
                    print("\nResultados del cálculo:")
                    for key, value in resultado_calculo.items():
                        print(f"{key}: {value}")

                    respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()
                    if respuesta_guardar_excel == 'si' or respuesta_guardar_excel == 's':
                        resultado_pokemon_debil = pokemon_mas_debil(datos_pokemon_lista)
                        guardar_pokemon_mas_debil_en_excel(resultado_pokemon_debil, 'pokemon_debil.xlsx')
                        print(f"Datos almacenados en 'pokemon_debil.xlsx.'")

                    respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()
                    if respuesta_guardar_txt == 'si' or respuesta_guardar_txt == 's':
                        nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                        guardar_datos_en_txt([resultado_calculo], nombre_archivo_txt)
                        print(f"Datos almacenados en {nombre_archivo_txt}.")
            elif seleccion_calculo == "4":
                if carrito:
                    print("Ticket de compras:")
                    for item in carrito:
                        print(f"{item['name']}: ${item['cost']} (IVA del 16%: ${item['cost_with_iva']})")

                    subtotal = sum(item['cost'] for item in carrito)
                    total_con_iva = sum(item['cost_with_iva'] for item in carrito)
                    print(f"\nSubtotal: ${subtotal}")
                    print(f"Total (con IVA del 16%): ${total_con_iva:.2f}")

                    # Preguntar al usuario si desea guardar el ticket en un archivo Excel
                    respuesta_guardar_excel = input("¿Desea guardar el ticket en un archivo Excel? (Sí/No): ").lower()
                    if respuesta_guardar_excel == 'si' or respuesta_guardar_excel == 's':
                        guardar_ticket_en_excel(carrito, 'Ticket_de_compras.xlsx')
                        print(f"Ticket de compras guardado en 'Ticket_de_compras.xlsx.")

                    # Preguntar al usuario si desea guardar el ticket en un archivo TXT
                    respuesta_guardar_txt = input("¿Desea guardar el ticket en un archivo TXT? (Sí/No): ").lower()
                    if respuesta_guardar_txt == 'si' or respuesta_guardar_txt == 's':
                        guardar_ticket_en_txt(carrito, 'Ticket_de_compras.txt')
                        print(f"Ticket de compras guardado en 'Ticket_de_compras.txt'.")
                else:
                    print("No hay ítems en el carrito de compras.")
                
            else:
                print("Opción no válida.")
        
        elif opcion == '6':
            print('Seleccione una opción:')
            print('1. Leer archivo excel (xlsx)')
            print('2. Leer archivo de texto (txt)')
            seleción_de_opción=input('Ingresa el número de la opción deseada:')
            if seleción_de_opción == '1':
                leerexcel()
            elif seleción_de_opción =='2':
                leertexto()
            else:
                print("Opción no válida.")
