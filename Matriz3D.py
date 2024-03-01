# Matriz3D
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ambato
        [   # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # Puyo
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # Loja
        [   # Semana 1
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 25}
        ]
    ]
]
#
# Calcular el promedio de temperaturas para cada ciudad y semana
i=0
j=0
for ciudad in temperaturas:
    i=i+1
    if i == 1:#numero de la cuidad
        print(f"\nPromedio de temperaturas de la cuidad: {i}, Ambato")
    elif i ==2:
        print(f"\nPromedio de temperaturas de la cuidad: {i}, Puyo")
    else:
        print(f"\nPromedio de temperaturas de la cuidad: {i}, Loja")
    j=0
    for semana in ciudad:
        j=j+1 #para numero de la semana
        promp = 0
        for dia in semana:
            promp += dia['temp']/7
        print(f"Semana {j} temp_promedio : {promp:.2f}°C")
