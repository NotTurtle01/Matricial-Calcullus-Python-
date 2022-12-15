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

A = matriz([[2,3,4], [1,2,5], [9,2,3]])
print(A.nula(3,4))
