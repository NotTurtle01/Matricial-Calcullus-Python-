#Óscar Mirás Sánchez. Joel Rubio González.

#Módulo de Python: class matriz.

class matriz:
    def __init__(self,lista):
        if lista == []:
            self.matriz = lista
        else:
            for fila in lista:
                if len(fila) != len(lista[0]):
                    print('Eso no es una matriz válida')
                    quit()
            self.matriz = lista
            self.filas = len(lista)
            self.columnas = len(lista[0])
    
    def __str__(self):
      cadena = ''
      for i in range(0,len(self.matriz)):
        if i != (len(self.matriz)-1):
          cadena = cadena + str(self.matriz[i]) + '\n'
        else:
            cadena = cadena + str(self.matriz[i])
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
                      defecto[i][j] = float(input('Dime el elemento de la fila ' + str(i+1) + ' ,columna ' + str(j+1) + ': '))
                      valido = True
                  except ValueError:
                      print('Eso no es un número válido, intentelo de nuevo')
      return defecto
      
    def mostrar_objeto(self,n,m):
      return self.matriz[n-1][m-1]
      
    def asignar_elemento(self,n,m,elemento):
      self.matriz[n-1][m-1] = elemento
      return self.matriz
      
    def fila(self,n):
      return self.matriz[n-1]
      
    def columna(self,m):
      lista_columna = []
      for i in self.matriz:
        lista_columna.append(i[m-1])
      return lista_columna
      
    def diagonal(self,d):
        #OJO. Hacer la comprobación de ES_CUADRADA
      if d == 1:
        lista_diagonal_1 = []
        for i in range(self.columnas):
          lista_diagonal_1.append(self.matriz[i][i])
        return lista_diagonal_1
      if d == 2:
        lista_diagonal_2 = []
        for i in range(self.columnas):
          lista_diagonal_2.append(self.matriz[self.filas -1 - i][i])
        return lista_diagonal_2
        
    def escalar_matriz(self,escalar):
      for fila in range(self.columnas):
        for columna in range(self.filas):
          self.matriz[fila][columna] = escalar * self.matriz[fila][columna]
      return self.matriz
      
    def opuesta(self):
      return self.escalar_matriz(-1) #Uso recursivo de la función escalar_matriz
      
    def identidad(self,n):
      M = []
      for i in range(n):
        M.append([0] * n )
      for i in range(n):
        M[i][i] = 1
      return M
      
    def nula(self,n,m):
      lista_nula = [[0]]
      for i in range(n-1):
          lista_nula.append([0])
      for i in range(n):
          for j in range(m-1):
              lista_nula[i].append(0)
      return lista_nula

    def __add__(self,otro):
        if otro.filas != self.filas:
            print('Como las matrices no tienen las mismas dimensiones no se pueden sumar')
        elif otro.columnas != self.columnas:
            print('Como las matrices no tienen las mismas dimensiones no se pueden sumar')
        else:
            suma = []
            for i in range(self.filas):
                fila = []
                for j in range(self.columnas):
                    fila.append(self.matriz[i][j] + otro.matriz[i][j])
                suma.append(fila)
        return suma

    def __sub__(self,otro):
        if otro.filas != self.filas:
            print('Como las matrices no tienen las mismas dimensiones no se pueden sumar')
        elif otro.columnas != self.columnas:
            print('Como las matrices no tienen las mismas dimensiones no se pueden sumar')
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
      for i in range (self.filas):
        for j in range (self.columnas):
          lista_nula[i][j] = self.matriz[j][i]
      return lista_nula
    
    def is_cuadrada(self):
      if self.filas == self.columnas:
        return True
      else:
        return False
    
    def is_fila(self):
      if self.filas == 1:
        return True
      else:
        return False
    
    def is_columna(self):
      if self.columnas == 1:
        return True
      else: 
        return False
    
    def is_simetrica(self):
      if self.transposicion() == self.matriz:
        return True
      else:
        return False
    
    def __mul__(self,otro):
    if self.columnas != otro.filas:
        print('Esas matrices no tienen dimensiones validas para multiplicar')
        quit()
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
    

A = matriz([[2,3,4], [1,2,5], [9,2,3]])
B = matriz([[5,2,3], [3,2,3], [9,2,4]])
C = matriz([[1],[2],[7]])
print(A-B)
print(A.is_cuadrada())
print(B.is_columna())
