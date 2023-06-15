from cosas import Alumno, Perro

def main():
    al1 = Alumno("Jose", 19, "ICO")
    print(vars(al1))
    al1.__nombre = "Diego"
    print(vars(al1))

    al1.set_nombre("María")
    print(vars(al1))
    print("-----to string------")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(4)
    print("------Perro-----")

    perro1 = Perro("Chihuaha", 2, 1.4)
    print(vars(perro1))
    perro1.raza = "De la calle" #set notacion pythonic
    print(vars(perro1))
    perro1.__raza = "Pug"
    print(vars(perro1))
    print(vars(perro1))
    print(perro1)

    perro1.raza = "Doberman"
    perro1.edad = 3
    perro1.estatura = 1.9
    print(perro1)

    perro2= Perro("Boxer", 5, 1.2)
    print(perro2)

    cachorr= Perro.es_cachorro(1)
    print(cachorr)
    Perro.dormir()

    Danes= Perro.perro_grande(0.8)
    print(Danes)

main()