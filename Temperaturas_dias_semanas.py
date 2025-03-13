#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades.
#Definir parametros
#Primera dimension = Ciudade (3 ciudades)
#Segunda dimension = Dias de la semana (7 dias)
#Tecera dimension = Semanas (2 semanas)
temperaturas = {
    "Quito": [
        [   # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    "Latacunga": [
        [   # Semana 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    "Cuenca": [
        [   # Semana 1
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 13}
        ]
    ]
}

# Función para calcular el promedio de las temperaturas de cada ciudad y semana
def calcular_promedio_temperaturas(temperaturas):
    # Recorrer cada ciudad
    for ciudad, semanas in temperaturas.items():
        print(f"\nPromedios para {ciudad}:")
        # Recorrer cada semana de la ciudad
        for semana_idx, semana in enumerate(semanas):
            suma_temperaturas = sum(dia["temp"] for dia in semana)  # Suma todas las temperaturas de la semana
            promedio = suma_temperaturas / len(semana)  # Calcula el promedio
            print(f"  Promedio Semana {semana_idx + 1}: {promedio:.2f} grados")

# Llamada a la función para calcular y mostrar los promedios
calcular_promedio_temperaturas(temperaturas)



