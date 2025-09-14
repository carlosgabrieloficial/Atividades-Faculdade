
participantes = [{

    "Nome":"Alice",
    "País":"EUA",
    "Afiliação":"Facul 1",
    "Interesse":["Fisica","Astronomia"],
},
    {"Nome":"Bob",
    "País":"Brasil",
    "Afiliação":"Facul 2",
    "Interesse":["Biologia","Astronomia"],
},
    {"Nome":"Carlos",
    "País":"Índia",
    "Afiliação":"Facul 3",
    "Interesse":["Quimica","Engenharia"],
    },
]


regioes = set(participantes["País"] for participantes in participantes)

afiliacoes = {}
for participante in participantes:
    afiliacao = participante["Afiliação"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao.append](participante["Nome"])

interreses = ([interesse for participante in participantes for interesse in participantes["Interesse"]])
