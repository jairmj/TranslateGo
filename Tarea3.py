# Integrantes: César Jair Moraña
#             Cesar Alonso Rojas Guevara


#   El programa funciona generando dos listas llenas de objetos principales , una de ellas genera los alumnos y otra genera
#   Los cursos ambas son activadas por funciones, como se debe evitar clonar los objetos de tipo curso, la función
#   Encargada de generar los cursos es invocada cada vez que van a ser asignados a un alumno.

#   Como extra al trabajo, se ha añadido el modo administrador, en el cual se permite cambiar notas, nombres y apellidos
#   De los alumnos, para poder ingresar se debe poner la contraseña que por defecto es 123456. Aunque esta puede ser
#   Modificada dentro del propio programa.

import getpass
import csv
import time
import random as r


######### Funciones de la generación de objetos tipo estudiantes / alumnos #########

def GeneraCodigo(Lista):
    '''
    Genera un código único y aleatorio del formato A123456
    '''
    while True:
        a = r.randint(1000000, 9999999)
        if not a in Lista:
            return "A{}".format(a)


def GeneraCursos():
    '''
    Genera una lista con 8 cursos (cada curso es un objeto)
    '''
    ListaCursos = []
    with open("cursos.csv") as file:
        reader = csv.reader(file)
        next(reader)
        cursos = []
        creditos = []
        pesos = []
        aulas = []
        for row in reader:
            if row == []:
                break
            else:
                lista_pesos = []
                cursos.append(row[0])
                creditos.append(row[1])
                aulas.append(row[-1])
                lista_pesos.append(row[2])
                lista_pesos.append(row[3])
                lista_pesos.append(row[4])
                lista_pesos.append(row[5])
                pesos.append(lista_pesos)

        for i in range(8):
            pesosNotas = []
            for l in range(8):
                pesosNotas.append(
                    [int(pesos[i][0]) / 100, int(pesos[i][1]) / 100, int(pesos[i][2]) / 100, int(pesos[i][3]) / 100])
            ListaCursos.append(Curso(cursos[i], int(creditos[i]), [0, 0, 0, 0], aulas[i], pesosNotas[i]))
        return ListaCursos


def GeneraAlumnos():
    '''
    Genera un lista con 30 alumnos (cada alumno es un objeto)
    '''
    Alumnos = []
    Codigos = []
    nombres = ["Jair", "Vanessa", "Elisa", "Roberto", "Francisco", "Teodoro", "Miriam", "Mario", "José", "Rosa",
               "Andrea", "Alma", "Luis", "Alba", "Micaela", "María", "Lidia", "Carlos", "Francisco", "Delia",
               "Katherine", "Rubén", "David", "Claudia", "Marina", "Héctor", "Óscar", "Desiré", "Silvia", "Juan", ]
    apellidos = ["Camacho", "Rivas", "Campos", "García", "Quispe", "Martínez", "García", "Delgado", "Díaz", "Álvarez"
        , "Nima", "Pérez", "Arroyo", "Jiménez", "Vásquez", "Valdivia", "López", "Sánchez", "Soto", "Mendoza",
                 "Quijano", "Chávez", "Flores", "Manrique", "Ramírez", "Puerta", "Mejía", "Guitérrez", "Gómez", "Silva"]
    Nombres_Apellidos = []
    Combinac_nombres = []
    Conjunto_NombresFiltrados = []
    ListaExpandida = []

    while True:  # Lista de alumnos y apellidos filtrados
        x = r.randrange(30)
        y = r.randrange(30)
        if not str(x) + str(y) in Combinac_nombres:
            Nombres_Apellidos.append(nombres[x] + " " + apellidos[y])
            Combinac_nombres.append(str(x) + str(y))
        if len(Nombres_Apellidos) == 30:
            break
    for i in Nombres_Apellidos:  # Modifico la lista para que al pasarla a conjunto no dé erorres
        nombre, apellido = i.split(" ")
        anadir = [nombre, apellido]
        ListaExpandida.append(anadir)
    for i in ListaExpandida:
        Conjunto_NombresFiltrados.append(set(i))
    for i, j in Conjunto_NombresFiltrados:
        if i in nombres:  # Al pasarlo a conjunto las parejas de nombres y apellidos a veces se desordenan
            EdadAleatoria = r.randint(18,
                                      26)  # así que verifico dónde está el nombre para mandarlo al objeto estudiante correctamente
            code = GeneraCodigo(Codigos)
            cd = int(code[1:8])
            Codigos.append(cd)
            Alumnos.append(Estudiante(i, j, EdadAleatoria, codigo=code))
        else:
            EdadAleatoria = r.randint(18, 26)
            code = GeneraCodigo(Codigos)
            cd = int(code[1:8])
            Codigos.append(cd)
            Alumnos.append(Estudiante(j, i, EdadAleatoria, codigo=code))
    return Alumnos


def GeneraListaCursos():
    '''
    Genera una lista de cuatro cursos diferentes
    '''
    ListaCursos = []
    Cursos = GeneraCursos()
    for i in range(0, 1):
        NumsDif = []
        while True:  # While infinito para generar aleatorios diferentes y que los cursos sean distintos
            a = r.randint(0, 7)
            if not a in NumsDif:
                NumsDif.append(a)
            if len(NumsDif) == 4:
                break
        for l in NumsDif:
            ListaCursos.append(Cursos[l])
    return ListaCursos


def RefrescaPromedio(Alumnos):
    '''
    Actualiza el promedio de los alumnos ingresados, retorna una lista con todos los alumnos.
    '''
    for i in Alumnos:
        for l in i.cursos:
            l.promedio = GeneraPromedio(l.notas, l.PesoNotas)
    return Alumnos


def AsignaCursos(Alumnos):
    '''
    Asigna 4 cursos aleatorios y diferentes de una lista de cursos que se pase a los diferentes alumnos que hayan sido enviados a través de otra lista
    '''
    for i in Alumnos:
        Cursoss = GeneraListaCursos()  # Se van generando objetos tipo curso nuevos cada vez para que no haya objetos duplicados
        i.cursos = Cursoss[:]


def AsignaNotas(Alumnos):
    '''
    Asigna notas aleatorias entre 7 y 20
    '''
    for i in Alumnos:
        for l in i.cursos:
            notas = []
            for i in range(0, 4):
                a = r.randint(7, 20)
                notas.append(a)
            l.notas = notas[:]
    return Alumnos


def GeneraPromedio(lista, pesonotas):
    '''
    Genera el promedio de la lista enviada
    '''
    promedio = 0
    sumador = 0
    for i in lista:
        promedio = i * pesonotas[
            sumador] + promedio  # Como los pesos están ingresados en porcentajes solamente hace falta
        sumador += 1  # ir multiplicando por cada uno y sumar
    return promedio


###################     Funciones del funcionamiento del menú principal  #############################

def ListaAl(ListaAlumnos):
    '''
    Genera una lista con todos los alumnos. Su Nombre, apellido, código y edad (Opción 1 menú principal)
    '''
    print("Nombre     Apellido     Código     Edad")
    print("---------------------------------------")
    for alumnos in ListaAlumnos:
        print("{:11}{:13}{:12}{}".format(alumnos.nombre, alumnos.apellido, alumnos.codigo, alumnos.edad))


def ReporteCurso(ListaCursos, ListaAlumnos):
    '''
    Imprime el listado de alumnos con sus notas y promedio para un curso que se ingrese (Opcion 2 menú principal)
    '''

    print("")
    CursoInput = input("Ingrese el curso: ")
    CursoInput = CursoInput.upper()
    ListaDeCursos = GeneraListaDeCursos(ListaCursos)
    NoDetectaCurso = True
    for ln in ListaDeCursos:
        if ln == CursoInput.upper():
            NoDetectaCurso = False
            CursoAct = ln
            break
    if CursoInput in ListaDeCursos:
        for crso in ListaCursos:
            if crso.nombreCurso.upper() == CursoAct:
                CursoAct = crso
        print(
            "\nCurso: {}\nCréditos: {}\nAula: {}".format(CursoAct.nombreCurso, CursoAct.numeroCreditos, CursoAct.aula))
        print("\n\nAlumno                        PC       EC      EA       EB      PROM")
        print("-----------------------------------------------------------------------")
    for alumn in ListaAlumnos:
        A = GeneraCursosAlumno(alumn)
        if CursoInput in A:
            índice = A.index(CursoInput)
            print("{:12}{:10}{:10}{:10}  {:5}{:10}{:10.2f}".format(alumn.nombre, alumn.apellido,
                                                                   alumn.cursos[índice].notas[0],
                                                                   alumn.cursos[índice].notas[1],
                                                                   alumn.cursos[índice].notas[2],
                                                                   alumn.cursos[índice].notas[3],
                                                                   alumn.cursos[índice].promedio))
    if NoDetectaCurso:
        print("\nCurso no encontrado")


def Opcion_Adm_CambiarNotas(curso, alumno):
    '''
    Genera un menu para modificar las notas. (Opción 4 Administrador - Modificar notas)
    '''
    print("\nNotas actuales:\nPC: {}\nEC: {}\nEA: {}\nEB: {}\nPromedio: {:.2f}\n".format(alumno.cursos[curso].notas[0],
                                                                                         alumno.cursos[curso].notas[1],
                                                                                         alumno.cursos[curso].notas[2],
                                                                                         alumno.cursos[curso].notas[3],
                                                                                         alumno.cursos[curso].promedio))
    print("[1] Modificar PC\n[2] Modificar EC\n[3] Modificar EA\n[4] Modificar EB")
    oc = int(input(""))
    if oc == 1:
        while True:
            try:
                while True:
                    notaNueva = float(input("Ingrese la nueva nota: "))
                    if notaNueva >= 0 and notaNueva <= 20:
                        break
                    else:
                        print("La nota debe estar entre 0 y 20")
            except ValueError:
                print("\nDebe ingresar un número.")

            save = alumno.cursos[curso].notas[0]  # Guardo la nota por si luego quiere cancelar
            alumno.cursos[curso].notas[0] = notaNueva
            alumno.cursos[curso].promedio = GeneraPromedio(alumno.cursos[curso].notas,
                                                           alumno.cursos[curso].PesoNotas)  # Actualizo el promedio
            print(
                "\nEl nuevo promedio del alumno sería: {:.2f}\n¿Desea continuar?\n[1] Si\n[2] No\n[3] Ingresar Otra nota".format(
                    alumno.cursos[curso].promedio))
            SubOpcionConfirmacionPromedio = input("")
            if SubOpcionConfirmacionPromedio == "1":
                print("\nNota cambiada con éxito!")
                break
            elif SubOpcionConfirmacionPromedio == "2":
                alumno.cursos[curso].notas[0] = save
                break
    if oc == 2:
        while True:
            try:
                while True:
                    notaNueva = float(input("Ingrese la nueva nota: "))
                    if notaNueva >= 0 and notaNueva <= 20:
                        break
                    else:
                        print("La nota debe estar entre 0 y 20")
            except ValueError:
                print("\nDebe ingresar un número.")
            save = alumno.cursos[curso].notas[1]
            alumno.cursos[curso].notas[1] = notaNueva
            alumno.cursos[curso].promedio = GeneraPromedio(alumno.cursos[curso].notas, alumno.cursos[curso].PesoNotas)
            print(
                "El nuevo promedio del alumno sería: {:.2f} Desea continuar?\n[1] Si\n[2] No\n[3] Ingresar Otra nota".format(
                    alumno.cursos[curso].promedio))
            SubOpcionConfirmacionPromedio = input("")
            if SubOpcionConfirmacionPromedio == "1":
                print("\nNota cambiada con éxito!")
                break
            elif SubOpcionConfirmacionPromedio == "2":
                alumno.cursos[curso].notas[1] = save
                break
    if oc == 3:
        while True:
            try:
                while True:
                    notaNueva = float(input("Ingrese la nueva nota: "))
                    if notaNueva >= 0 and notaNueva <= 20:
                        break
                    else:
                        print("La nota debe estar entre 0 y 20")
            except ValueError:
                print("\nDebe ingresar un número.")
            alumno.cursos[curso].notas[2] = notaNueva
            save = alumno.cursos[curso].notas[2]
            alumno.cursos[curso].promedio = GeneraPromedio(alumno.cursos[curso].notas, alumno.cursos[curso].PesoNotas)
            print(
                "El nuevo promedio del alumno sería: {:.2f} Desea continuar?\n[1] Si\n[2] No\n[3] Ingresar Otra nota".format(
                    alumno.cursos[curso].promedio))
            SubOpcionConfirmacionPromedio = input("")
            if SubOpcionConfirmacionPromedio == "1":
                print("\nNota cambiada con éxito!")
                break
            elif SubOpcionConfirmacionPromedio == "2":
                alumno.cursos[curso].notas[2] = save
                break
    if oc == 4:
        while True:
            try:
                while True:
                    notaNueva = float(input("Ingrese la nueva nota: "))
                    if notaNueva >= 0 and notaNueva <= 20:
                        break
                    else:
                        print("La nota debe estar entre 0 y 20")
            except ValueError:
                print("\nDebe ingresar un número.")
                alumno.cursos[curso].notas[3] = notaNueva
                save = alumno.cursos[curso].notas[3]
                alumno.cursos[curso].promedio = GeneraPromedio(alumno.cursos[curso].notas,
                                                               alumno.cursos[curso].PesoNotas)
                print(
                    "El nuevo promedio del alumno sería: {:.2f} Desea continuar?\n[1] Si\n[2] No\n[3] Ingresar Otra nota".format(
                        alumno.cursos[curso].promedio))
                SubOpcionConfirmacionPromedio = input("")
                if SubOpcionConfirmacionPromedio == "1":
                    print("\nNota cambiada con éxito!")
                    break
                elif SubOpcionConfirmacionPromedio == "2":
                    alumno.cursos[curso].notas[3] = save
                    break

                    ############## Funciones para validar entradas en mayus y en minúscula ##############


def GeneraCursosAlumno(Lista):
    '''
    Retorna una lista con los nombres de los cursos (Para el alumno ingresado) en mayúsculas
    '''
    a = []
    a = [Lista.cursos[0].nombreCurso.upper(), Lista.cursos[1].nombreCurso.upper(), Lista.cursos[2].nombreCurso.upper(),
         Lista.cursos[3].nombreCurso.upper()]
    return a


def GeneraListaDeCursos(Lista):
    '''
    Retorna una lista con los nombres de los cursos en mayúsculas
    '''
    return [Lista[0].nombreCurso.upper(), Lista[1].nombreCurso.upper(), Lista[2].nombreCurso.upper(),
            Lista[3].nombreCurso.upper(), Lista[4].nombreCurso.upper(), Lista[5].nombreCurso.upper(),
            Lista[6].nombreCurso.upper()
        , Lista[7].nombreCurso.upper()]


# Funciones estéticas

def PointAnimation():
    '''
    Escribe 3 puntos uno por uno con 1 segundo de delay
    '''
    print(". ", end="")
    time.sleep(1)
    print(". ", end="")
    time.sleep(1)
    print(".")
    time.sleep(1)

    #############     Objetos     ###############


class Curso(object):
    '''
    Clase curso, crea un curso en base a su nombre, su número de créditos, notas, el aula y el peso de cada nota
    '''

    def __init__(self, nombreCurso="", numeroCreditos=0, notas=[0, 0, 0, 0], aula="", PesoNotas=[]):
        self.nombreCurso = nombreCurso
        self.numeroCreditos = numeroCreditos
        self.notas = notas
        self.promedio = GeneraPromedio(notas, PesoNotas)
        self.PesoNotas = PesoNotas
        self.aula = aula

    @property
    def nombreCurso(self):
        return self.__nombreCurso

    @nombreCurso.setter
    def nombreCurso(self, Validado1):
        if isinstance(Validado1, str):
            self.__nombreCurso = Validado1
        else:
            print("Ingrese el nombre del curso correctamente, por favor.")

    @property
    def numeroCreditos(self):
        return self.__numeroCreditos

    @numeroCreditos.setter
    def numeroCreditos(self, Validado2):
        if isinstance(Validado2, int):
            self.__numeroCreditos = Validado2
        else:
            print("Ingrese el número de créditos únicamente con un dígito.")

    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, notaValidada):
        if isinstance(notaValidada, list):
            self.__notas = notaValidada
        else:
            print("La nota debe estar entrre 0 y 20.")

    @property
    def aula(self):
        return self.__aula

    @aula.setter
    def aula(self, aulaValidada):
        if isinstance(aulaValidada, str):
            self.__aula = aulaValidada
        else:
            print("Ingrese el aula correctamente, entre comillas.")

    def Genera_Pc(self, nota):
        self.notas[0] = nota
        self.promedio = GeneraPromedio(self.notas)

    def Genera_Ec(self, nota):
        self.notas[1] = nota
        self.promedio = GeneraPromedio(self.notas)

    def Genera_Ea(self, nota):
        self.nota[2] = nota
        self.promedio = GeneraPromedio(self.notas)

    def Genera_EB(self, nota):
        self.nota[3] = nota
        self.promedio = GeneraPromedio(self.notas)

    def __str__(self):
        return "Curso: {}\nNumero de creditos: {}\nNotas: {}\nPromedio del curso: {}\nAula: {}".format(self.nombreCurso,
                                                                                                       self.numeroCreditos,
                                                                                                       self.notas,
                                                                                                       self.promedio,
                                                                                                       self.aula)


class Estudiante(object):
    '''
    Clase estidante, para crear estudiantes en base a su nombre, apellido, edad, cursos que lleva y el código
    '''

    def __init__(self, nombre="", apellido="", edad=0, cursos=[], codigo=""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cursos = cursos
        self.codigo = codigo

    def __str__(self):
        return "Alumno: {} {}\nEdad: {}\nCódigo: {}\nCursos:\n\t- {}\n\t- {}\n\t- {}\n\t- {}".format(self.nombre,
                                                                                                     self.apellido,
                                                                                                     self.edad,
                                                                                                     self.codigo,
                                                                                                     self.cursos[
                                                                                                         0].nombreCurso,
                                                                                                     self.cursos[
                                                                                                         1].nombreCurso,
                                                                                                     self.cursos[
                                                                                                         2].nombreCurso,
                                                                                                     self.cursos[
                                                                                                         3].nombreCurso)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombreValidado):
        if isinstance(nombreValidado, str):
            self.__nombre = nombreValidado
        else:
            print("Intrduzca un nombre válido.")

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellidoConfirmado):
        if isinstance(apellidoConfirmado, str):
            self.__apellido = apellidoConfirmado
        else:
            print("Ingrese un apellido válido.")

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edadConfirmada):
        if isinstance(edadConfirmada, int):
            self.__edad = edadConfirmada
        else:
            print("Ingrese su edad con un número sin decimales por favor.")


def Main():
    # Generando los alumnos con sus cursos y sus notas
    ListaCursos = GeneraCursos()
    ListaAlumnos = GeneraAlumnos()
    AsignaCursos(ListaAlumnos)
    AsignaNotas(ListaAlumnos)
    ListaAlumnos = RefrescaPromedio(ListaAlumnos)

    AdmPass = "123456"  # Se establece la contraseña de administrador por defecto
    Comprobador = 1  # Se establece una variable para limitar los intentos de acceso al modo administrador

    # Menú principal
    while True:
        try:
            print("\n\n  Menú Principal")
            print("------------------")
            print(
                "[1] Listado de alumnos\n[2] Reporte por Alumno\n[3] Reporte por curso\n[4] Ingresar como administrador\n[0] Salir")
            Opción = int(input("\n"))
            if Opción == 0:
                print("\nHasta pronto!")
                break
            elif Opción == 1:
                ListaAl(ListaAlumnos)
            elif Opción == 2:
                print("")
                Alumno = input("Ingrese el nombre del alumno: ")
                AlumnoMiss = True  # Establezco una variable para ver si se ha encontrado el alumno o no.
                for Nombres in ListaAlumnos:
                    if Nombres.nombre.upper() == Alumno.upper() or Nombres.apellido.upper() == Alumno.upper():
                        AlumnoMiss = False
                        print("\nNombre: {} {}\nCódigo: {}\nEdad: {}".format(Nombres.nombre, Nombres.apellido,
                                                                             Nombres.codigo, Nombres.edad))
                        print("\n\n Curso                     PC    EC   EA    EB     PROM")
                        print("----------------------------------------------------------")
                        for cursos in Nombres.cursos:
                            print("{:23}{:6}{:6}{:5}{:6}{:9.2f}".format(cursos.nombreCurso, cursos.notas[0],
                                                                        cursos.notas[1], cursos.notas[2],
                                                                        cursos.notas[3],
                                                                        GeneraPromedio(cursos.notas, cursos.PesoNotas)))
                            print("")
                if AlumnoMiss:  # Compruebo
                    print("\nAlumno no encontrado")

            elif Opción == 3:
                ReporteCurso(ListaCursos, ListaAlumnos)
            elif Opción == 4 and Comprobador == 1:
                tries = 4  # Establezco el número de intentos
                while True:
                    contraseña = input("Ingrese la contraseña: ")
                    if contraseña == AdmPass:
                        print("\n\n[1] Modificar notas\n[2] Modificar perfiles\n[3] Modificar contraseña")
                        opc = int(input(""))
                        if opc == 1:
                            alumnoAModificar = input("Ingrese el codigo del alumno: ")
                            NoEncontrado = True
                            for alumno in ListaAlumnos:
                                if alumno.codigo == alumnoAModificar:
                                    NoEncontrado = False
                                    print("\nAlumno: {} {}".format(alumno.nombre, alumno.apellido))
                                    print("\n[1] {}\n[2] {}\n[3] {}\n[4] {}".format(alumno.cursos[0].nombreCurso,
                                                                                    alumno.cursos[1].nombreCurso,
                                                                                    alumno.cursos[2].nombreCurso,
                                                                                    alumno.cursos[3].nombreCurso))
                                    ex = int(input(""))
                                    if ex == 1:
                                        Opcion_Adm_CambiarNotas(0, alumno)
                                    if ex == 2:
                                        Opcion_Adm_CambiarNotas(1, alumno)

                                    if ex == 3:
                                        Opcion_Adm_CambiarNotas(2, alumno)

                                    if ex == 4:
                                        Opcion_Adm_CambiarNotas(3, alumno)
                            if NoEncontrado:
                                print("\nAlumno no encontrado")
                            break
                        elif opc == 2:
                            Opcion = int(
                                input("\n\n[1] Modificar nombre\n[2] Modificar apellido\n[3] Modificar edad\n\n"))
                            if Opcion == 1:
                                alumnoAModificar = input("Ingrese el codigo del alumno a modificar: ")
                                NoEncontrado = True
                                for alumnos in ListaAlumnos:
                                    if alumnos.codigo == alumnoAModificar:
                                        NoEncontrado = False
                                        print(alumnos)
                                        New = input("\nIngrese el nuevo nombre: ")
                                        PointAnimation()
                                        alumnos.nombre = New
                                        print("Listo!\n")
                                if NoEncontrado:
                                    print("\nAlumno no encontrado")
                                break
                            elif Opcion == 2:
                                alumnoAModificar = input("Ingrese el codigo del alumno a modificar: ")
                                NoEncontrado = True
                                for alumnos in ListaAlumnos:
                                    if alumnos.codigo == alumnoAModificar:
                                        NoEncontrado = False
                                        print(alumnos)
                                        New = input("\nIngrese el nuevo apellido: ")
                                        PointAnimation()
                                        alumnos.apellido = New
                                        print("Listo!\n")
                                if NoEncontrado:
                                    print("\nAlumno no encontrado")
                                break
                            elif Opcion == 3:
                                alumnoAModificar = input("Ingrese el codigo del alumno a modificar: ")
                                NoEncontrado = True
                                for alumnos in ListaAlumnos:
                                    if alumnos.codigo == alumnoAModificar:
                                        NoEncontrado = False
                                        print(alumnos)
                                        New = int(input("\nIngrese la nueva edad: "))
                                        PointAnimation()
                                        alumnos.edad = New
                                        print("Listo!")
                                if NoEncontrado:
                                    print("\nAlumno no encontrado")
                                break
                        elif opc == 3:
                            Pass1 = input("Ingrese la contraseña actual: ")
                            if Pass1 == AdmPass:
                                while True:
                                    NewPass = getpass.getpass("Ingrese la nueva contraseña: ")
                                    NewPassConfirmation = getpass.getpass("Ingrese de nuevo la contraseña: ")
                                    if NewPass == NewPassConfirmation:
                                        AdmPass = NewPass
                                        print("Contraseña cambiada con éxito")
                                        break
                                break
                    else:
                        if tries != 1 and tries != 2:
                            print("\nContraseña incorrecta, le quedan {} intentos.\n".format(tries - 1))
                        elif tries == 2:
                            print("\nContraseña incorrecta, le queda {} intento.\n".format(tries - 1))
                        else:
                            print("\nNo le quedan intentos.")
                        tries = tries - 1
                    if tries == 0:
                        Comprobador = 10
                        break
            elif Opción == 4 and Comprobador == 10:
                print("\nHa fallado demasiadas veces.")
            else:
                print("\nIngrese un número válido")

        except ValueError:
            print("\nIngrese una opción válida")
Main()