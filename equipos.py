


class pg:
    equipo = "pinguinos galacticos"    
    int1 = "yesica Rodriguez"
    int2 = "yahir monje"
    int3 = ""
    integrantes = "{} \n {} \n {}".format(int1, int2, int3)

class mosq:
    equipo = "Los 3 mosqueteros"    
    int1 = "Dania Benavides"
    int2 = "Erick Lozano"
    int3 = "Ana Valenzuela"
    integrantes = "{} \n {} \n {}".format(int1, int2, int3)

class innombrables:
    equipo = "Los =^UwU^="    
    int1 = "Leonardo Gonzáles"
    int2 = "Norma Mendoza"
    int3 = "Jonathan Durán"
    integrantes = "{} \n {} \n {}".format(int1, int2, int3)

class web:
    equipo = "WebHeros"    
    int1 = "Jesus Arellano"
    int2 = "Axel Reyes"
    int3 = "Daniel Delgado"
    integrantes = "{} \n {} \n {}".format(int1, int2, int3)

class poly:
    equipo = "PolyStation"    
    int1 = "Fernando Siqueiros"
    int2 = "Ixchel Arreguin"
    int3 = ""
    integrantes = "{} \n {} \n {}".format(int1, int2, int3)

class toyota:
    equipo = "toyotalegacy"    
    int1 = "Israel Chacon"
    int2 = "Mauricio Garcia"
    int3 = "Elias Sierra"
    integrantes = "{} \n {} \n {}".format(int1, int2, int3)



class fs3:
    print("equipos \n 1.-pinguinos galacticos \n 2.-Los 3 mosqueteros \n4.-Los =^UwU^= \n4.- webheros \n 5.-Polystation \n 6.- toyotalegacy")
    opcion = int(input("Selecciona un equipo: "))
    
    if opcion == 1:
        pinguinos = pg()
        print(pinguinos.integrantes)
    if opcion == 2:
        mo = mosq()
        print(mosq.integrantes)
    if opcion == 3:
        inn = innombrables()
        print(inn.integrantes)
    if opcion == 4:
        hero = web()
        print(hero.integrantes)
    if opcion == 5:
        cop = poly()
        print(cop.integrantes)
    if opcion == 6:
        toy = toyota()
        print(toy.integrantes)
    
print(fs3)


  
