#Ejercicio 1: Sistema de Gestión de Personal
#Crea un sistema de gestión de personal utilizando herencia múltiple.

#Clase base: Persona
#Atributos: nombre, edad
#Método: mostrar_informacion

#Clase derivada: Empleado (hereda de Persona)
#Atributos adicionales: salario, empresa
#Métodos adicionales: calcular_salario_anual

#Clase derivada: Freelancer (hereda de Persona)
#Atributos adicionales: tarifa_hora, horas_trabajadas
#Métodos adicionales: calcular_ingresos

#Clase derivada: Consultor (hereda de Empleado y Freelancer)
#Métodos: mostrar_informacion_completa (combina información de Empleado y Freelancer)

#Implementa un sistema donde puedas agregar empleados, freelancers y consultores, y calcular sus ingresos anuales.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrarInformacion(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"

class Empleado(Persona):
    def __init__(self, nombre, edad,salario,empresa):
        super().__init__(nombre, edad)
        self.salario = salario
        self.empresa = empresa
    def calcularSalarioAnual(self):
        return f"El salario anual seria S/.{self.salario*12}"

class Freelancer(Persona):
    def __init__(self, nombre, edad,tarifario_hora,horas_trabajadas):
        super().__init__(nombre, edad)
        self.tarifario_hora = tarifario_hora
        self.horas_trabajadas = horas_trabajadas
    def calcularIngresos(self):
        return f"Los ingresos totales es: S/.{self.horas_trabajadas*self.tarifario_hora}"

class Consultor(Empleado, Freelancer):
    def __init__(self, nombre, edad, salario, empresa, tarifario_hora, horas_trabajadas):
        Persona.__init__(self, nombre, edad)
        self.salario = salario
        self.empresa = empresa
        self.tarifario_hora = tarifario_hora
        self.horas_trabajadas = horas_trabajadas

    def mostrarInformacionCompleta(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\n\nEMPLEADO:\n \nSalario: {self.salario} \nEmpresa: {self.empresa}\n\nFRELANCER\n\nTarifario Hora: S/.{self.tarifario_hora}\nHoras trabajadas: {self.horas_trabajadas}"

class Empresa:
    def __init__(self):
        self.lista = []
    def agregarEmpleado(self,empleado):
        self.lista.append(empleado)
    def mostrarTodos(self):
        for persona in self.lista:
            print(persona.mostrarInformacion())
            if isinstance(persona,Empleado):
                print(persona.calcularSalarioAnual())
            if isinstance(persona,Freelancer):
                print(persona.calcularIngresos())
            if isinstance(persona,Consultor):
                print(persona.mostrarInformacionCompleta())
empresa = Empresa()

n=0
while n!=4:
    n = int(input("\nBienvenido al menu de opciones: \n1-Agregar Empleado\n2-Agregar Freelancer\n3-Agregar Consultor\n4-Salir"))
    if n==1:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        salario = float(input("Salario: "))
        empresa_nombre = input("Empresa: ")
        empleado = Empleado(nombre, edad, salario, empresa_nombre)
        empresa.agregarEmpleado(empleado)

    elif n==2:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        tarifario_hora = float(input("Tarifario hora: "))
        horas_trabajadas = input("Horas trabajadas: ")
        freelancer = Freelancer(nombre, edad, tarifario_hora, horas_trabajadas)
        empresa.agregarEmpleado(freelancer)
    elif n == 3:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        salario = float(input("Salario: "))
        empresa_nombre = input("Empresa: ")
        tarifario_hora = float(input("Tarifario por hora: "))
        horas_trabajadas = float(input("Horas trabajadas: "))
        consultor = Consultor(nombre, edad, salario, empresa_nombre, tarifario_hora, horas_trabajadas)
        empresa.agregarEmpleado(consultor)

empresa.mostrarTodos()
