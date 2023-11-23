from almacenamientoDatos import guardar_pokemon_mas_fuerte_en_excel, guardar_ticket_en_excel, guardar_datos_en_txt,guardar_pokemon_mas_debil_en_excel,actualizar_datos_en_excel,actualizar_datos_evoluciones_en_excel,  actualizar_datos_item_en_excel, guardar_ticket_en_txt,guardar_promedio_stats_en_excel
from calculosMatematicos import calcular_promedio_stats, pokemon_mas_debil, pokemon_mas_fuerte, generar_reporte 
from lecturaDatos import leerexcel, leertexto, load_workbook
from consultaApi import obtener_datos_item, obtener_datos_pokemon, obtener_evoluciones
import requests
import json
import os

nombre_carpeta2 = "Consulta de API"
nombre_carpeta="Reporte"
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
    carrito = []

    while True:

            menu()
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "0":
                print("Hasta luego, pokeamigo!:D")
                break
            elif opcion == "1":
                # Consultar datos de un Pokémon
                try:
                    pokemon_id = int(input("Ingrese el número del Pokémon para consultar: "))
                    datos_pokemon = obtener_datos_pokemon(pokemon_id)
                    if datos_pokemon:
                        print(f"\nDatos del Pokémon {pokemon_id}:\n{json.dumps(datos_pokemon, indent=2)}")
                        datos_pokemon_lista.append(datos_pokemon)

                        respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                        while respuesta_guardar_excel not in ['si', 's', 'no', 'n']:
                            print('Parece que no ingresaste tu respuesta correctamente. No se guardó tu archivo. Vuélvelo a intentar.')
                            print('Recuerda ingresar "S" o "Si" para guardar los datos. O "N" o "No" para descartarlos.')
                            respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                        if respuesta_guardar_excel in ['si', 's']:
                            nombre_archivo_excel = input("Ingrese el nombre del archivo Excel (con extensión .xlsx): ")
                            actualizar_datos_en_excel([datos_pokemon], nombre_archivo_excel)
                            print(f"Datos almacenados en {nombre_archivo_excel}.")
                        else:
                            print('No se guardaron los datos.')


                        # Preguntar al usuario si desea guardar la información en un archivo TXT
                        respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                        while respuesta_guardar_txt not in ['si', 's', 'no', 'n']:
                            print('Parece que no ingresaste tu respuesta correctamente. No se guardó tu archivo. Vuélvelo a intentar.')
                            print('Recuerda ingresar "S" o "Si" para guardar los datos. O "N" o "No" para descartarlos.')
                            respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                        if respuesta_guardar_txt in ['si', 's']:
                            nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                            guardar_datos_en_txt([datos_pokemon], nombre_archivo_txt)
                            print(f"Datos almacenados en {nombre_archivo_txt}.")
                        else:
                            print('No se guardaron los datos en el archivo TXT.')


                    else:
                        print(f"No se pudo obtener información del Pokémon {pokemon_id}.")
                except ValueError:
                    print("Error: Ingrese un número válido para el Pokémon.")
            elif opcion == "2":
                # Consultar datos de un ítem
                try:
                    item_id = input("Ingrese el ID del ítem que desea consultar: ")
                    datos_item = obtener_datos_item(item_id)
                    if datos_item:
                        print(f"\nDatos del ítem {item_id}:\n{json.dumps(datos_item, indent=2)}")
                        datos_item_lista.append(datos_item)

                            # Preguntar al usuario si desea guardar la información en un archivo Excel
                        respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                        while respuesta_guardar_excel not in ['si', 's', 'no', 'n']:
                            print('Parece que no ingresaste tu respuesta correctamente. No se guardó tu archivo. Vuélvelo a intentar.')
                            print('Recuerda ingresar "S" o "Si" para guardar los datos. O "N" o "No" para descartarlos.')
                            respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                        if respuesta_guardar_excel in ['si', 's']:
                            nombre_archivo_excel = input("Ingrese el nombre del archivo Excel (con extensión .xlsx): ")
                            actualizar_datos_item_en_excel(datos_item_lista, nombre_archivo_excel)
                            print(f"Datos almacenados en {nombre_archivo_excel}.")
                        else:
                            print('No se guardaron los datos en el archivo Excel.')


                        # Preguntar al usuario si desea guardar la información en un archivo TXT
                        respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                        while respuesta_guardar_txt not in ['si', 's', 'no', 'n']:
                            print('Parece que no ingresaste tu respuesta correctamente. No se guardó tu archivo. Vuélvelo a intentar.')
                            print('Recuerda ingresar "S" o "Si" para guardar los datos. O "N" o "No" para descartarlos.')
                            respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                        if respuesta_guardar_txt in ['si', 's']:
                            nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                            guardar_datos_en_txt(datos_item_lista, nombre_archivo_txt)
                            print(f"Datos almacenados en {nombre_archivo_txt}.")
                        else:
                            print('No se guardaron los datos en el archivo TXT.')


                        # Pregunta al usuario si desea agregar el ítem al carrito de compras
                        respuesta_agregar_carrito = input("¿Deseas agregar este ítem a tu carrito de compras? (Sí/No): ").lower()

                        while respuesta_agregar_carrito not in ['si', 's', 'no', 'n']:
                            print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                            print('Recuerda ingresar "S" o "Si" para agregar el ítem al carrito. O "N" o "No" para descartarlo.')
                            respuesta_agregar_carrito = input("¿Deseas agregar este ítem a tu carrito de compras? (Sí/No): ").lower()

                        if respuesta_agregar_carrito in ['si', 's']:
                            # Calcula el costo con IVA del 16% y agrega el ítem al carrito
                            costo = datos_item.get('cost', 0)
                            costo_con_iva = costo * 1.16
                            carrito.append({'name': datos_item['name'], 'cost': costo, 'cost_with_iva': costo_con_iva})
                            print("Ítem agregado al carrito de compras.")
                        else:
                            print("El ítem no se agregó al carrito de compras.")

                except ValueError:
                    print("Error: Ingrese un ID válido para el ítem.")
            elif opcion == "3":
                # Consultar evoluciones de un Pokémon
                try:
                    pokemon_id = int(input("Ingrese el número del Pokémon para consultar evoluciones: "))
                    evoluciones = obtener_evoluciones(pokemon_id)
                    if evoluciones:
                        print(f"\nEvoluciones del Pokémon {pokemon_id}:\n{json.dumps(evoluciones, indent=2)}")
                        datos_evoluciones_lista.append(evoluciones)

                        # Preguntar al usuario si desea guardar la información en un archivo Excel
                        respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                        while respuesta_guardar_excel not in ['si', 's', 'no', 'n']:
                            print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                            print('Recuerda ingresar "S" o "Si" para guardar los datos en un archivo Excel. O "N" o "No" para descartarlos.')
                            respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                        if respuesta_guardar_excel in ['si', 's']:
                            nombre_archivo_excel = input("Ingrese el nombre del archivo Excel (con extensión .xlsx): ")
                            actualizar_datos_evoluciones_en_excel(datos_evoluciones_lista, nombre_archivo_excel)
                            print(f"Datos almacenados en {nombre_archivo_excel}.")
                        else:
                            print("Los datos no se han guardado en un archivo Excel.")

                        # Preguntar al usuario si desea guardar la información en un archivo TXT
                        respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                        while respuesta_guardar_txt not in ['si', 's', 'no', 'n']:
                            print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                            print('Recuerda ingresar "S" o "Si" para guardar los datos en un archivo TXT. O "N" o "No" para descartarlos.')
                            respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                        if respuesta_guardar_txt in ['si', 's']:
                            nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                            guardar_datos_en_txt(datos_evoluciones_lista, nombre_archivo_txt)
                            print(f"Datos almacenados en {nombre_archivo_txt}.")
                        else:
                            print("Los datos no se han guardado en un archivo TXT.")


                    else:
                        print(f"No se pudo obtener información de las evoluciones del Pokémon {pokemon_id}.")
                except ValueError:
                    print("Error: Ingrese un número válido para el Pokémon.")
            elif opcion == "4":
                # Generar gráficas
                if datos_pokemon_lista:
                    generar_reporte(datos_pokemon_lista)
                else:
                    print("No hay datos de Pokémon para generar gráficas.")
            elif opcion == "5":
                try:
                # Cálculos matemáticos
                    print("Seleccione un cálculo matemático:")
                    print("1. Promedio de stats de Pokémon consultados")
                    print("2. Pokémon más fuerte")
                    print("3. Pokémon más débil")
                    print("4. Ticket de compras de items")
                    seleccion_calculo = input("Ingrese el número de la opción deseada: ")

                    if seleccion_calculo == "1":
                        try:
                            resultados_calculo = calcular_promedio_stats(datos_pokemon_lista)
                            if resultados_calculo:
                                print("\nResultados del cálculo:")
                                for key, value in resultados_calculo.items():
                                    print(f"{key}: {value}")
                               # Pregunta al usuario si quiere guardar los datos en un archivo Excel
                                respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                                while respuesta_guardar_excel not in ['si', 's', 'no', 'n']:
                                    print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                                    print('Recuerda ingresar "S" o "Si" para guardar los datos en un archivo Excel. O "N" o "No" para descartarlos.')
                                    respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                                if respuesta_guardar_excel in ['si', 's']:
                                    # Verificar si la carpeta existe, si no, crearla
                                    if not os.path.exists(nombre_carpeta):
                                        os.makedirs(nombre_carpeta)

                                    # Unir la carpeta con el nombre del archivo para obtener la ruta completa
                                    resultado_pokemon_fuerte = pokemon_mas_fuerte(datos_pokemon_lista)
                                    nombre_archivo_excel = 'pokemon_fuerte.xlsx'
                                    ruta_archivo = os.path.join(nombre_carpeta, nombre_archivo_excel)

                                    guardar_pokemon_mas_fuerte_en_excel(resultado_pokemon_fuerte, ruta_archivo)
                                    print(f"Datos almacenados en '{ruta_archivo}'.")
                                else:
                                    print("Los datos no se han guardado en un archivo Excel.")


                                # Pregunta al usuario si quiere guardar los datos en un archivo TXT
                                respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                                while respuesta_guardar_txt not in ['si', 's', 'no', 'n']:
                                    print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                                    print('Recuerda ingresar "S" o "Si" para guardar los datos en un archivo TXT. O "N" o "No" para descartarlos.')
                                    respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                                if respuesta_guardar_txt in ['si', 's']:
                                    # Verificar si la carpeta existe, si no, crearla
                                    if not os.path.exists(nombre_carpeta2):
                                        os.makedirs(nombre_carpeta2)

                                    # Unir la carpeta con el nombre del archivo para obtener la ruta completa
                                    nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                                    ruta_archivo = os.path.join(nombre_carpeta2, nombre_archivo_txt)

                                    guardar_datos_en_txt([resultados_calculo], ruta_archivo)
                                    print(f"Datos almacenados en '{ruta_archivo}'.")
                                else:
                                    print("Los datos no se han guardado en un archivo TXT.")


                        except Exception as e:
                            print(f"Error al calcular el promedio de stats: {str(e)}")

                    elif seleccion_calculo == "2":
                        try:
                            resultado_calculo = pokemon_mas_fuerte(datos_pokemon_lista)
                            if resultado_calculo:
                                print("\nResultados del cálculo:")
                                for key, value in resultado_calculo.items():
                                    print(f"{key}: {value}")



                                # Pregunta al usuario si quiere guardar los datos en un archivo Excel
                                respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                                while respuesta_guardar_excel not in ['si', 's', 'no', 'n']:
                                    print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                                    print('Recuerda ingresar "S" o "Si" para guardar los datos en un archivo Excel. O "N" o "No" para descartarlos.')
                                    respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                                if respuesta_guardar_excel in ['si', 's']:
                                    # Verificar si la carpeta existe, si no, crearla
                                    if not os.path.exists(nombre_carpeta):
                                        os.makedirs(nombre_carpeta)

                                    # Unir la carpeta con el nombre del archivo para obtener la ruta completa
                                    ruta_archivo = os.path.join(nombre_carpeta, 'pokemon_fuerte.xlsx')

                                    resultado_pokemon_fuerte = pokemon_mas_fuerte(datos_pokemon_lista)
                                    guardar_pokemon_mas_fuerte_en_excel(resultado_pokemon_fuerte, ruta_archivo)
                                    print(f"Datos almacenados en '{ruta_archivo}'.")
                                else:
                                    print("Los datos no se han guardado en un archivo Excel.")


                                # Pregunta al usuario si quiere guardar los datos en un archivo TXT
                                respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                                while respuesta_guardar_txt not in ['si', 's', 'no', 'n']:
                                    print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                                    print('Recuerda ingresar "S" o "Si" para guardar los datos en un archivo TXT. O "N" o "No" para descartarlos.')
                                    respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                                if respuesta_guardar_txt in ['si', 's']:
                                    nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                                    guardar_datos_en_txt([resultado_calculo], nombre_archivo_txt)
                                    print(f"Datos almacenados en {nombre_archivo_txt}.")
                                else:
                                    print("Los datos no se han guardado en un archivo TXT.")

                        except Exception as e:
                            print(f"Error al calcular el Pokémon más fuerte: {str(e)}")

                    elif seleccion_calculo == "3":
                        try:
                            resultado_calculo = pokemon_mas_debil(datos_pokemon_lista)
                            if resultado_calculo:
                                print("\nResultados del cálculo:")
                                for key, value in resultado_calculo.items():
                                    print(f"{key}: {value}")

                                # Pregunta al usuario si quiere guardar los datos en un archivo Excel
                                respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                                while respuesta_guardar_excel not in ['si', 's', 'no', 'n']:
                                    print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                                    print('Recuerda ingresar "S" o "Si" para guardar los datos en un archivo Excel. O "N" o "No" para descartarlos.')
                                    respuesta_guardar_excel = input("¿Desea guardar la información en un archivo Excel? (Sí/No): ").lower()

                                if respuesta_guardar_excel in ['si', 's']:
                                    resultado_pokemon_debil = pokemon_mas_debil(datos_pokemon_lista)
                                    guardar_pokemon_mas_debil_en_excel(resultado_pokemon_debil, 'pokemon_debil.xlsx')
                                    print(f"Datos almacenados en 'pokemon_debil.xlsx'.")
                                else:
                                    print("Los datos no se han guardado en un archivo Excel.")


                               # Definir la función para guardar datos en un archivo TXT
                                def guardar_datos_en_txt(datos, ruta_archivo):
                                    # Lógica para guardar los datos en un archivo TXT
                                    with open(ruta_archivo, 'w') as archivo:
                                        for dato in datos:
                                            archivo.write(str(dato) + '\n')

                                # Pregunta al usuario si quiere guardar los datos en un archivo TXT
                                respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                                while respuesta_guardar_txt not in ['si', 's', 'no', 'n']:
                                    print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                                    print('Recuerda ingresar "S" o "Si" para guardar los datos en un archivo TXT. O "N" o "No" para descartarlos.')
                                    respuesta_guardar_txt = input("¿Desea guardar la información en un archivo TXT? (Sí/No): ").lower()

                                if respuesta_guardar_txt in ['si', 's']:
                                    # Carpeta donde se guardará el archivo TXT
                                    carpeta_consulta_api = "Consulta de api"
                                    # Crear la carpeta si no existe
                                    if not os.path.exists(carpeta_consulta_api):
                                        os.makedirs(carpeta_consulta_api)

                                    # Pedir al usuario que ingrese el nombre del archivo TXT
                                    nombre_archivo_txt = input("Ingrese el nombre del archivo TXT (con extensión .txt): ")
                                    # Unir la carpeta y el nombre del archivo para obtener la ruta completa
                                    ruta_completa = os.path.join(carpeta_consulta_api, nombre_archivo_txt)

                                    # Llamar a la función para guardar los datos en el archivo TXT
                                    guardar_datos_en_txt([resultado_calculo], ruta_completa)
                                    print(f"Datos almacenados en '{ruta_completa}'.")
                                else:
                                    print("Los datos no se han guardado en un archivo TXT.")

                        except Exception as e:
                            print(f"Error al calcular el Pokémon más débil: {str(e)}")

                    elif seleccion_calculo == "4":
                        try:
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

                                while respuesta_guardar_excel not in ['si', 's', 'no', 'n']:
                                    print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                                    print('Recuerda ingresar "S" o "Si" para guardar el ticket en un archivo Excel. O "N" o "No" para descartarlo.')
                                    respuesta_guardar_excel = input("¿Desea guardar el ticket en un archivo Excel? (Sí/No): ").lower()

                                if respuesta_guardar_excel in ['si', 's']:
                                    # Carpeta donde se guardará el archivo
                                    carpeta_reportes = "reportes"
                                    # Crear la carpeta si no existe
                                    if not os.path.exists(carpeta_reportes):
                                        os.makedirs(carpeta_reportes)

                                    # Unir la carpeta y el nombre del archivo para obtener la ruta completa
                                    nombre_archivo = 'Ticket_de_compras.xlsx'
                                    ruta_completa = os.path.join(carpeta_reportes, nombre_archivo)

                                    guardar_ticket_en_excel(carrito, ruta_completa)
                                    print(f"Ticket de compras guardado en '{ruta_completa}'.")
                                else:
                                    print("El ticket no se ha guardado en un archivo Excel.")


                                # Preguntar al usuario si desea guardar el ticket en un archivo TXT
                                respuesta_guardar_txt = input("¿Desea guardar el ticket en un archivo TXT? (Sí/No): ").lower()

                                while respuesta_guardar_txt not in ['si', 's', 'no', 'n']:
                                    print('Parece que no ingresaste tu respuesta correctamente. Vuélvelo a intentar.')
                                    print('Recuerda ingresar "S" o "Si" para guardar el ticket en un archivo TXT. O "N" o "No" para descartarlo.')
                                    respuesta_guardar_txt = input("¿Desea guardar el ticket en un archivo TXT? (Sí/No): ").lower()

                                if respuesta_guardar_txt in ['si', 's']:
                                    guardar_ticket_en_txt(carrito, 'Ticket_de_compras.txt')
                                    print(f"Ticket de compras guardado en 'Ticket_de_compras.txt'.")
                                else:
                                    print("El ticket no se ha guardado en un archivo TXT.")

                            else:
                                print("No hay ítems en el carrito de compras.")

                        except Exception as e:
                            print(f"Error al generar el ticket de compras: {str(e)}")
                except Exception as e:print(f"Error inesperado: {str(e)}")          
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
            else: 
                print("Error al seleccionar una opción del menú: Ingrese un número válido del 0 al 6.")