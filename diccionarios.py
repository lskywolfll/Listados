
# Se componente de llaves y valores ej: { nombre: "Rene" }

def run():
    mi_diccionario = {
        "nombre": "Rene",
        'edad': 21,
        'nacionalidad': "Chilena"
    }

    # print(mi_diccionario)
    # print(mi_diccionario["nombre"])
    # print(mi_diccionario.keys())

    poblacion_paises = {
        "Argentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424
    }

    # print(poblacion_paises["Argentina"])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(f"{pais} tiene {poblacion} habitantes")

if __name__ == "__main__":
    run()