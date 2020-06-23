import random

hombre = ['ANTONIO', 'JOSE', 'FRANCISCO', 'JUAN', 'MANUEL', 'PEDRO', 'JESUS', 'ANGEL', 'MIGUEL', 'JAVIER',
          'JOSE ANTONIO', 'DAVID',
          'CARLOS', 'JOSE LUIS', 'ALEJANDRO', 'MIGUEL ANGEL', 'FRANCISCO JAVIER', 'RAFAEL', 'DANIEL',
          'JUAN JOSE', 'LUIS', 'PABLO', 'JUAN ANTONIO', 'JOAQUIN', 'SERGIO', 'FERNANDO',
          'JUAN CARLOS', 'ANDRES', 'JOSE MANUEL', 'JOSE MARIA', 'RAMON', 'RAUL', 'ALBERTO', 'ENRIQUE', 'ALVARO',
          'VICENTE',
          'EMILIO', 'FRANCISCO JOSE', 'DIEGO', 'JULIAN', 'JORGE', 'ALFONSO', 'ADRIAN',
          'RUBEN', 'SANTIAGO', 'IVAN', 'JUAN MANUEL', 'PASCUAL', 'JOSE MIGUEL', 'MARIO']

mujer = ['MARIA', 'MARIA CARMEN', 'JOSEFA', 'ISABEL', 'MARIA DOLORES', 'CARMEN',
         'FRANCISCA', 'MARIA PILAR', 'DOLORES', 'MARIA JOSE', 'ANTONIA', 'ANA', 'MARIA ISABEL',
         'MARIA ANGELES', 'PILAR', 'ANA MARIA', 'LUCIA', 'CRISTINA', 'LAURA', 'ENCARNACION', 'JUANA', 'MARIA TERESA',
         'ROSARIO', 'ELENA', 'MARTA',
         'MANUELA', 'ROSA MARIA', 'MARIA LLANOS', 'MARIA JOSEFA', 'RAQUEL', 'ANGELES', 'CONCEPCION', 'MERCEDES',
         'IRENE', 'TERESA', 'BEATRIZ',
         'PAULA', 'ANGELA', 'JULIA', 'ANA BELEN', 'ROCIO', 'AMPARO', 'ALICIA', 'CONSUELO', 'ROSA', 'ASCENSION',
         'ANDREA',
         'MARIA ROSARIO', 'MARIA JESUS', 'MARIA LUISA']

apellido = ['MARTINEZ', 'LOPEZ', 'SANCHEZ', 'GONZALEZ', 'GOMEZ',
            'FERNANDEZ', 'MORENO', 'JIMENEZ', 'PEREZ', 'RODRIGUEZ',
            'NAVARRO', 'RUIZ', 'DIAZ', 'SERRANO', 'HERNANDEZ', 'MUÑOZ', 'SAEZ', 'ROMERO',
            'RUBIO', 'ALFARO', 'MOLINA', 'LOZANO', 'CASTILLO', 'PICAZO', 'ORTEGA', 'MORCILLO',
            'CANO', 'MARIN', 'CUENCA', 'GARRIDO', 'TORRES', 'CORCOLES', 'GIL',
            'ORTIZ', 'CALERO', 'VALERO', 'CEBRIAN', 'RODENAS', 'ALARCON', 'BLAZQUEZ', 'NUÑEZ',
            'PARDO', 'MOYA', 'TEBAR', 'REQUENA', 'ARENAS', 'BALLESTEROS', 'COLLADO', 'RAMIREZ',
            'VALENCIA']


def generarNombre(genero):
    nombre = ""
    if genero == 'F':
        nombre = random.choice(mujer)
    else:
        nombre = random.choice(hombre)
    apellido1 = random.choice(apellido)
    apellido2 = random.choice(apellido)
    nombre = nombre + " " + apellido1 + " " + apellido2
    return nombre


def generarEdad():
    # edadas entre 18 y 85
    return random.randint(18, 85)


def generarSexo():
    return random.choice(['F', 'M'])
