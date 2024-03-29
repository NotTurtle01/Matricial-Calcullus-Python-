
'''

Autores:

*Óscar Mirás Sánchez. 
*Joel Rubio González.

'''

'''

Módulo centrado en las operaciones con matrices y caracterizaciones de las mismas. 


'''

class matriz:
    def __init__(self,lista):
        
#Método de inicialización de la clase matriz. 
#Se consideran matrices las listas de listas que posean como elementos números en punto flotante.
        
        if lista == []:
            self.matriz = lista
        else:
            for fila in lista:
                if len(fila) != len(lista[0]): 
                    
                #En caso de que el número de columnas de una fila no coincidiera con el número de columnas de la primera fila (lista[0]),
                #no se trataría de una matriz de condiciones válidas.
                    
                    print('Eso no es una matriz válida')
                    quit()
                    
            self.matriz = lista #Sea self.matriz la propia lista de listas (es decir, la matriz a tratar).
            self.filas = len(lista) #Sea self.filas el número de filas de la lista.
            self.columnas = len(lista[0]) #Sea self.columnas el número de columnas de la lista.
    
    def __str__(self):
      cadena = ''
      for i in range(0,len(self.matriz)):
        if i != (len(self.matriz)-1):
          cadena = cadena + str(self.matriz[i]) + '\n' #Se añade un salto de línea tras imprimir cada fila de la matriz.
        else:
          cadena = cadena + str(self.matriz[i])
      return cadena
    
    def resize(self): 
        
      '''
      Función que imprime una matriz sin saltos de linea entre sus filas. Permite presentar la matriz de forma apropiada para ser guardada 
      en el sistema de archivos mediante la función guardar_archivo().
      
      '''
    
      cadena = []
      for i in range(len(self.matriz)):
        cadena = cadena + self.matriz[i]
      return cadena
      
    def crearmatriz(self,n,m):
      defecto = [[0]]
      for i in range(n-1):
          defecto.append([0])
      for i in range(n):
          for j in range(m-1):
              defecto[i].append(0)
      for i in range(n):
          for j in range(m):
              valido = False
              while not valido:
                  try:          
                      defecto[i][j] = float(input('Dime el elemento de la fila ' + str(i+1) + ', columna ' + str(j+1) + ': '))
                      valido = True
                  except ValueError:
                      print('Eso no es un número válido, intentelo de nuevo')
      return defecto
      
    def mostrar_elemento(self,n,m):
        
      '''
      Devolución del elemento[n][m] de una matriz.
       
      '''
    
      return self.matriz[n-1][m-1]
      
    def asignar_elemento(self,n,m,elemento):
      
      '''
      Asignación de un elemento a la posición [n][m] de la matriz.
       
      '''
    
      self.matriz[n-1][m-1] = elemento
      return self.matriz
      
    def fila(self,n):
        
      '''
      Devolución de la fila determinada por el usuario.
      
      '''
      
      return self.matriz[n-1]
      
    def columna(self,m):
        
      '''
      Devolución de la columna determinada por el usuario.
       
      '''
    
      lista_columna = []
      for i in self.matriz:
        lista_columna.append(i[m-1])
      return lista_columna
      
    def diagonal(self,d):
      if not self.es_cuadrada(): #Si la matriz no es cuadrada, se obvia la búsqueda de sus diagonales.
        print('La matriz no es cuadrada')
        return False
      else:
        if d == 1: #Para la diagonal principal, se añaden a una lista vacía los elementos [i][i] de la matriz.
            lista_diagonal_1 = []
            for i in range(self.columnas):
                lista_diagonal_1.append(self.matriz[i][i])
            return lista_diagonal_1
        if d == 2: #Para la diagonal secundaria, se añaden a una lista vacía los elementos [self.filas -1 -i] [i] de la matriz.
            lista_diagonal_2 = []
            for i in range(self.columnas):
                lista_diagonal_2.append(self.matriz[self.filas -1 - i][i]) 
                
        #Al número de filas se le resta -1 para adecuarse a los índices de listas de Python. A este número se le substrae el número de 
        #columna en el que está el elemento, de forma que con cada iteración del bucle "for" se aumentará la resta en una unidad, 
        #de forma que se recorrerán las filas de la matriz de forma "ascendente" mientras las columnas se recorren de izquierda a derecha.
                
            return lista_diagonal_2
    
    def dimensiones(self): 
        
      '''
      Devolución de las dimensiones de la matriz a través de una lista.
      
      '''
    
      return [self.filas, self.columnas] 
        
    def escalar_matriz(self,escalar):
      '''
      Multiplicación de cada elemento de la matriz por el escalar dado.
      
      '''
      nuevo = deepcopy(self.matriz)
      for fila in range(len(nuevo[0])):
        for columna in range(len(nuevo)):
          nuevo[fila][columna] = escalar * nuevo[fila][columna]
      return nuevo
      
    def opuesta(self):
      return self.escalar_matriz(-1) #Obtener la matriz opuesta es equivalente a multiplicar la matriz dada por el escalar -1.
      
    def identidad(self,n): 
        
      '''
      Genera la matriz identidad de un orden dado a través de la adición de elementos a una lista vacía.
      
      '''
    
      M = []
      for i in range(n): #Se completa la matriz compuesta por ceros.
        M.append([0] * n )
      for i in range(n):
        M[i][i] = 1 #Se sustituyen los elementos de la diagonal principal por unos.
      return M
      
    def nula(self,n,m): 
        
      '''
      Crea una matriz nula según las dimensiones dadas.
      
      '''
      
      lista_nula = [[0]]
      for i in range(n-1):
          lista_nula.append([0])
      for i in range(n):
          for j in range(m-1):
              lista_nula[i].append(0)
      return lista_nula

    def __add__(self,otro): #Suma de matrices.
        if otro.filas != self.filas:
            print('Las matrices no tienen las mismas dimensiones. No se pueden sumar.')
        elif otro.columnas != self.columnas:
            print('Las matrices no tienen las mismas dimensiones. No se pueden sumar.')
        else:
            suma = []
            for i in range(self.filas):
                fila = []
                for j in range(self.columnas):
                    fila.append(self.matriz[i][j] + otro.matriz[i][j])
                suma.append(fila)
            return suma

    def __sub__(self,otro): #Resta de matrices.
        if otro.filas != self.filas:
            print('Las matrices no tienen las mismas dimensiones. No se pueden restar.')
        elif otro.columnas != self.columnas:
            print('Las matrices no tienen las mismas dimensiones. No se pueden restar.')
        else:
            resta = []
            for i in range(self.filas):
                fila = []
                for j in range(self.columnas):
                    fila.append(self.matriz[i][j] - otro.matriz[i][j])
                resta.append(fila)
            return resta
    
    def transposicion(self):
      lista_nula = [[0]]
      for i in range(self.columnas -1):
          lista_nula.append([0])
      for i in range(self.columnas):
          for j in range(self.filas -1):
              lista_nula[i].append(0)
      for i in range(self.filas):
        for j in range(self.columnas):
          lista_nula[i][j] = self.matriz[j][i] #Se transpone la matriz intercambiando filas por columnas y viceversa.
      return lista_nula
    
    def es_cuadrada(self):
      if self.filas == self.columnas: #Si el número de filas coincide con el número de columnas, la matriz es cuadrada.
        return True
      else:
        return False
    
    def es_fila(self):
      if self.filas == 1: #Si la matriz cuenta con una única fila, se trata de una matriz fila.
        return True
      else:
        return False
    
    def es_columna(self):
      if self.columnas == 1: #Si la matriz cuenta con una única columna, se trata de una matriz columna.
        return True
      else: 
        return False
    
    def es_simetrica(self):
      if self.transposicion() == self.matriz: #Se comprueba si la matriz transpuesta es igual a la original. En ese caso, sería simétrica.
        return True
      else:
        return False
    
    def es_triangular_superior(self):
      flag = True
      for i in range(1, self.filas):
        for j in range(0, i): #Bucle que estudia los elementos inferiores a la diagonal principal.  
          if self.matriz[i][j] != 0: #Si estos elementos son distintos de 0, no se trataría de una matriz triangular superior.
                flag = False
      return flag

    def es_triangular_inferior(self):
        
        '''
        En primer lugar se llama al método transposicion() para tener las columnas como nuevas filas. 
        Llamando al método es_triangular_superior() de la nueva matriz (transpuesta) podemos saber si 
        la matriz original es triangular inferior sin necesidad de programar otro método de comprobación.
        
        '''
        
        self.matriz = self.transposicion() 
        return self.es_triangular_superior()

    def __mul__(self,otro): #Multiplicación de matrices
        if self.columnas != otro.filas: 
        #Para ser multiplicadas, el número de columnas de la primera matriz deberá coincidir con el número de filas de la segunda matriz. 
            print('Las matrices no tienen dimensiones validas para ser multiplicadas.')
        else:
            mul = []
            for i in range(self.filas):
                fila = []
                for j in range(otro.columnas):
                    suma = 0
                    for t in range(otro.columnas):
                        suma += self.matriz[i][t] * otro.matriz[t][j]
                    fila.append(suma)
                mul.append(fila)
            return mul

    
    def es_magica(self): 

#Este método primero comprueba que sea una matriz cuadrada. Después se comprueba que estén presentes todos los numeros del 1 a 
#n al cuadrado, y por ultimo se obtienen todas las sumas de filas, columnas y diagonales, se introducen en una lista y 
#se comprueba que todas son iguales.

      if not self.es_cuadrada():
        return False
      else:
        for i in range(1,(self.filas*self.filas)+1):
            presente = False
            for j in range(self.filas):
                for t in range(self.columnas):
                    if self.matriz[j][t] == i:
                        presente = True
            if not presente:
                return False
        sumas = []
        for i in range(self.filas):
            suma = 0
            for j in range(self.columnas):
                suma += self.matriz[i][j]
            sumas.append(suma)
        for i in range(self.columnas):
            suma = 0
            for j in range(self.filas):
                suma += self.matriz[j][i]
            sumas.append(suma)
        suma = 0
        for i in range(self.filas):
            suma += self.matriz[i][i]
        sumas.append(suma)
        suma = 0
        for i in range(self.filas):
            suma += self.matriz[i][-(i+1)]
        sumas.append(suma)
        for i in range(len(sumas)):
            if sumas[0] != sumas[i]:
                return False
        return True

    def minimo(self):
        minimo = self.matriz[0][0]
        for i in range(self.filas):
            for j in range(self.columnas):
                if minimo > self.matriz[i][j]: 
                    minimo = self.matriz[i][j] #El elemento mínimo de la matriz se ve intercambiado.
        return minimo

    def maximo(self):
        maximo = self.matriz[0][0]
        for i in range(self.filas):
            for j in range(self.columnas):
                if maximo < self.matriz[i][j]: 
                    maximo = self.matriz[i][j] #El elemento máximo de la matriz se ve intercambiado.
        return maximo

    def media(self):
      suma = 0
      for i in range(self.filas):
          for j in range(self.columnas):
              suma += self.matriz[i][j]
      media = suma/(self.filas*self.columnas) #Cálculo de la media aritmética.
      return media

def intmayor0(cadena): #Función de comprobación. Solicita al usuario la introducción de un entero mayor que 0. 
    flag = False
    while flag == False:
        try:
            a = int(input(cadena))
            if a > 0:
                flag = True
            else:
                print('No has introducido un entero positivo. Vuelve a adjuntar el número.')
        except ValueError:
            print('No has introducido un número entero. Inténtalo de nuevo.')
    return a

def floatlibre(cadena): #Función de comprobación. Solicita al usuario la introducción de un número flotante.
    flag = False
    while flag == False:
      a = input(cadena)
      try:
          float(a)
          flag = True
      except ValueError:
          print('No has introducido un número válido. Inténtalo de nuevo.')
    return float(a)

def intlibre(cadena): #Función de comprobación. Solicita al usuario la introducción de un número entero.
    flag = False
    while flag == False:
        a = input(cadena)
        try:
            int(a)
            flag = True
        except ValueError:
            print('No has introducido un número válido. Inténtalo de nuevo.')
    return int(a)


'''
<Programa por defecto>
'''

if __name__ == "__main__": #Comprobaciones de las diferentes funcionalidades del módulo.

    def espera(): #Función que solicita "input" hasta que el usuario pulsa la tecla <ENTER>
        a = 0
        while a != '':
            a = input('\nPulsa <ENTER> para continuar: ')

    matriz1 = matriz([[1,2,3],[0,2,3],[0,0,4]])
    print('\nMatriz 1: \n')
    print(matriz1)
    espera()
    
    matriz2 = matriz([[2,4,3],[4,6,5],[-9,4,-2]])
    print('\nMatriz 2: \n')
    print(matriz2)
    espera()
    
    vacia = matriz([])

    print('\n1) Definición de una matriz de dimensiones dadas\n')

    matriz_nueva = vacia.crearmatriz(3,4)
    print('\nEsta es la nueva matriz: \n')
    print(matriz_nueva)
    espera()

    print('\n2) Asignación de un elemento específico de una matriz\n')

    matriz1.asignar_elemento(2, 2, 28)
    print('Matriz resultante al asignar al elemento 2,2 de la matriz 1 el número 28:\n')
    print(matriz1)
    espera()

    print('\n3) Obtención de un elemento específico de una matriz\n')

    nuevo_elemento = matriz1.mostrar_elemento(2, 2)
    print('Elemento 2,2 de la matriz 1: ', nuevo_elemento)
    espera()

    print('\n4) Presentación de una matriz por pantalla\n')

    print('Esta es la matriz 1:\n')
    print(matriz1)
    espera()
    
    print('\n5) Obtención de una fila\n')

    print('Fila 3 de la matriz 2: ', matriz2.fila(3))
    espera()

    print('\n6) Obtención de una columna\n')

    print('Columna dos de la matriz 1: ', matriz1.columna(2))
    espera()

    print('\n7) Obtención de una diagonal\n')

    print('Diagonal inversa de la matriz 1: ', matriz1.diagonal(2))
    espera()
    print('\nDiagonal principal de la matriz 2: ', matriz2.diagonal(1))
    espera()

    print('\n8) Devolución de dimensiones\n')

    print('Dimensiones de la matriz 1: ', matriz1.dimensiones())
    espera()

    print('\n9) Suma de matrices\n')

    print('Matriz suma de las matrices 1 y 2: ', matriz1 + matriz2)
    espera()

    print('\n10) Resta de matrices\n')

    print('Matriz resta de las matrices 1 y 2: ', matriz1 - matriz2)
    espera()

    print('\n11) Obtener la matriz opuesta\n')

    print('Matriz opuesta de la matriz 2: ', matriz2.opuesta())
    espera()

    print('\n12) Multiplicación de matrices\n')

    print('Matriz multiplicación de las matrices 1 y 2: ', matriz1 * matriz2)
    espera()

    print('\n13) Producto de escalar por matriz\n')

    print('Matriz que resulta de multiplicar la matriz 2 por el escalar 6: ', matriz2.escalar_matriz(6))
    espera()

    print('\n14) Generar matriz nula\n')

    nula = vacia.nula(4,5)
    print('Matriz nula de dimensiones 4 x 5: ', nula)
    espera()

    print('\n15) Generar matriz identidad\n')

    midentidad = vacia.identidad(8)
    print('Matriz identidad de orden 8: ', midentidad)
    espera()

    print('\n16) Transponer una matriz\n')

    print('Matriz transpuesta de la matriz 1: ', matriz1.transposicion())
    espera()

    print('\n17) Caracterización de matrices\n')

    print('Esta es la caracterización de la matriz 1:\n')
    if matriz1.es_magica():
        print('Matriz 1 es mágica')
    if matriz1.es_cuadrada():
        print('Matriz 1 es cuadrada')
    if matriz1.es_fila():
        print('Matriz 1 es una matriz fila')
    if matriz1.es_columna():
        print('Matriz 1 es una matriz columna')
    if matriz1.es_simetrica():
        print('Matriz 1 es una matriz simétrica')
    if matriz1.es_triangular_superior():
        print('Matriz 1 es triangular superior')
    if matriz1.es_triangular_inferior():
        print('Matriz 1 es triangular inferior')
    espera()

    print('\n18 a) Obtención valor máximo\n')

    print('Valor máximo de la matriz 2: ', matriz2.maximo())
    espera()

    print('\n18 b) Obtención valor mínimo\n')

    print('Valor mínimo de la matriz 2: ', matriz2.minimo())
    espera()

    print('\n18 c) Obtención valor medio\n')

    print('Valor medio de la matriz 2: ', matriz2.media())
    espera()

    print('\nPrueba finalizada sin errores en tiempo de ejecución.\n')
