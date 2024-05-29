#                           MountainFX


# creación de la clase
class Departamento:
    # miembros
    Nombre=any #Nombre del departamento al que pertenese.
    BaseConNombres=any #Base de datos con nombres y salarios.
     
    # Metodos ó funciones.
    def LeerBaseDeDatos(self):
        self.Nombre=str(input("\nCual departamento que desea consultar(Marketing,Finanzas,Tecnologia,Gestion_Humana,Gestion_operaciones): "))
        
        A=[i for i in BaseTotal if i[2]==self.Nombre] #creación de una lista,recorre linea por linea y agrega a la lista el registro
        # si el dato ubicado en la posición 2 es identico a la variable self.Nombre
        
        self.BaseConNombres=[[i[0]+" "+i[1],float(i[3])] for i in A] #creación de lista, me va a agregar a la lista
        # el dato en la ubicación 0=Nombre,1=apellido, flotante 3=salario recorriendo la lista llamada A
        print(self.Nombre,self.BaseConNombres) #Muestra las dos listas

    def MostrarSalario(self):
        L=str(input("\nbuscar empleado(nombre apellido): ")) #pide un dato string
        B=[i for i in self.BaseConNombres if i[0]==L  ] #creación de lista, agrega el dato ubicado en la posición 0=Nombre
        # si es identico a la variable L recorriendo la lista self.BaseConNombres
        if len(B): #con esta condición verificamos que el nombre del empleado ingresado este.
          print(B)
        else:
            print("\nNo se encontro empleado")
        
    def ValoresRS(self):
        # media
        S=0
        for i in self.BaseConNombres:
            S+=i[1] #acumulador de salarios corregir i[2]
        media=S/len(self.BaseConNombres) #aca contamos los trabajadores y dividimos el total del salarios con el total de trabajadores
        
        # desviación estándar 
        acuSalarios=0
        for i in self.BaseConNombres:
            acuSalarios+=(i[1]-media)**2 #se hace esta operación a cada trabajador(acumulador de salarios - la media)elevado al cuadrado ^2
        Desv=(acuSalarios/len(self.BaseConNombres))**(1/2)#la desviación es: total del acuSalarios dividido le total
        # de trabajadores elevado a ^1/2 un medio
        print("La media es: ",media)#S/len(self.BaseConNombres) corrección
        print("La desviacion estandar es: ",Desv)

    def CostoTotalDep(self):  
        SumaSalarios=0
        for i in self.BaseConNombres:
            SumaSalarios+=i[1]
            # SumaSalarios=sum(i[1])# otra forma de sumar salarios 
        print("Costos totales son: ",SumaSalarios)
        
    def MostrarEmpAxT(self):
        X=[i for i in self.BaseConNombres if i[1]<2320000] #creando lista que me recorra BaseConNombres si
        # el valor en la posición [1] es menor de 2'320.000
        print(f"Trabajadores con auxilio de transporte: {X}\n")
    
    
with open("employees2.txt",encoding="UTF-8") as archivo: #abrimos el archivo
    contenido=archivo.read()    #leemos el archivo y se lo asignamos a una variable
   
Base=contenido.split('\n') #convertimos el documento a una lista que nos separe cada elemento en cada salto de linea
Base.pop(0) #borrar el elemento ubicado en la posición 0

# print(Base[5].split())

BaseTotal=[i.split() for i in Base if len(i.split())==4]#convertimos cada registro en listas=['nombre','departamento','salario']
# si cada registro contiene 4 datos, si es menor o mayor a este numero lo ignora.
A=Departamento() #asignamos en la variable A la clase departamento()
# Tipo_de_dato = type(A)
# print(Tipo_de_dato)
A.LeerBaseDeDatos() #ingresamos a la clase y utilizamos todas las funciónes.
A.MostrarSalario()
A.ValoresRS()
A.CostoTotalDep()
A.MostrarEmpAxT()

B=Departamento()
B.LeerBaseDeDatos()
B.MostrarSalario()
B.ValoresRS()
B.CostoTotalDep()
B.MostrarEmpAxT()

C=Departamento()
C.LeerBaseDeDatos()
C.MostrarSalario()
C.ValoresRS()
C.CostoTotalDep()
C.MostrarEmpAxT()
    