_author_ = 'Rosy'


def sumados():
    print 10 * 20


def divicion(a, b):
    result = a / b
    print result


def cast():
   lista=[1,2,3, "hola"{"key1":"Rosa","key2":"Armando"}(1,2,3)]
   tupla=(1,2,3)
   diccionario={"key1":"Rosa","key2":"Armando"}
    for i in lista:
        print i
   """for k,v in diccionario.items():
       print "%s %s" %(k,v)"""





def main():
    sumados()
    divicion(10, 20)


class Estudiante(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hola(self):
        return self.nombre

    def esMayor(self):
        if self.edad >= 18:
            return True
        else:
            return False
def exception():
    try:
        3 / 0
    except Exception:
        print "Error"


def main():
    e = Estudiante("Rosa", 22)
    print "hola %s"%e.hola()
    if e.esMayor():
        print "Es mayor de edad"
    else:
        print "Es menor de edad"

    contador = 0
    while contador <= 0:
        print contador
        contador +=1
    exception()
    print cast()

if __name__ == "__main__":
    main()

