import time
import random
import xlsxwriter

class Juiz():
    def __init__(self):
        self.algoritimos = ['bubble sort', 'mergesort', 'insertion sort', 'quicksort', 'counting sort']
        self.NumeroDeListas = 10
        self.row = 0
        self.tamanhos = [1000, 10000, 100000, 1000000, 10000000]
        self.comecarXLS()
        print('Iniciando avaliação de algorítimos')
        self.rotina()
    
    
    
    def rotina(self):
        for x in self.algoritimos:
            # self.gerarListas()
            self.testar(x, self.gerarListas())
        self.workbook.close()
    
    
    
    def comecarXLS(self):
        self.workbook = xlsxwriter.Workbook('Resultados2.xls')
        self.worksheet = self.workbook.add_worksheet()
        self.worksheet.write(self.row, 0, 'Algorítimo')
        cell = 1
        for x in self.tamanhos:
            self.worksheet.write(self.row, cell, 'N={}'.format(x))
            cell +=1
        self.row +=1
    
    
    
    def escreverResultados(self, results):
        print(self.row, 'row')
        self.worksheet.write(self.row, 0, results[0])
        cell = 1
        valores = []
        intermediario = []
        contador = 1
        for x in results[1]:
            if contador % self.NumeroDeListas == 0:
                valores.append(sum(intermediario)/self.NumeroDeListas)
                intermediario = []
            else:
                intermediario.append(x)
            contador +=1
        print(valores)
        for y in valores:
            self.worksheet.write(self.row, cell, y)
            cell += 1
        # self.workbook.close()
        self.row += 1
    
    
    
    def gerarListas(self):
        listas = []
        for x in self.tamanhos: # 10 100 1000
            mLista = []
            for y in range(self.NumeroDeListas): # 10
                numeros = []
                for z in range(x): # 1 .. 100 1 .. 1000
                    numeros.append(random.randint(x * -1, x))
                mLista.append(numeros)
            listas.append(mLista)
        # print(len(listas))
        return listas
                

    
    def testar(self, algoritimo, listas):
        tester = Algoritimos(algoritimo, listas)
        results = tester.getResults()
        print("--- Program execution ended with %s seconds ---" % results)
        print("writting results to xml")
        self.escreverResultados(results)
        # print(results[1])
        
                



class Algoritimos():
    def __init__(self, algoritimo, listas):
        self.algoritimo = algoritimo
        self.startTime = 0
        self.endTime = []
        self.listas = listas
        print('algoritimos comecando')
        print('Algoritimo %s' %self.algoritimo)
        self.handleAlgoritimo()
    
    
    
    def handleAlgoritimo(self):
        switcher = {
            'bubble sort': self.bubleSort,
            'mergesort': self.merge_sort,
            'insertion sort': self.insertionSort,
            'quicksort': self.quickSort,
            'counting sort': self.countingSort
        }
        got = switcher.get(self.algoritimo, lambda: False)
        if got != False:
            for x in self.listas:
                for y in x:
                    self.startTime = time.time()
                    got(y)
                    self.endTime.append(time.time() - self.startTime)
                    print('fim')
    
    
    
    def bubleSort(self, nlist):
        for passnum in range(len(nlist)-1,0,-1):
            for i in range(passnum):
                if nlist[i]>nlist[i+1]:
                    temp = nlist[i]
                    nlist[i] = nlist[i+1]
                    nlist[i+1] = temp



    def merge_sort(self, lista):
        # self.startTime = time.time()
        # se a lista tem menos de 2 elementos, 
        # retorna a lista sem fazer nada
        if len(lista) < 2:
            return lista

        #caso contrario a lista é dividida em duas partes
        centro = len(lista) // 2

        #chamadas recursivas para listas da esquerda e direita
        lista_L = self.merge_sort(lista[:centro])
        lista_R = self.merge_sort(lista[centro:])
        
        #juntamos o resultado da partição das duas listas anteriores 
        return self.merge(lista_L, lista_R)
    


    def merge(self, lista_L, lista_R):
        # se uma lista está vazia, então não faço nada
        # e devo retornar a outra lista
        if len(lista_L) == 0:
            return lista_R

        # se a segunda lista está vazia, então não faço nada
        # e retorno a primeira lista
        if len(lista_R) == 0:
            return lista_L

        result = []
        index_L = index_R = 0

        # iremos processar tanto a lista da esquerda quanto
        # a lista da direita, então a lista de resultado deverá
        # terminar com o mesmo numero de elementos do que ambas listas
        while len(result) < len(lista_L) + len(lista_R):
            # realizo a ordenação e vou salvando na nova lista de resultados
            if lista_L[index_L] <= lista_R[index_R]:
                result.append(lista_L[index_L])
                index_L += 1
            else:
                result.append(lista_R[index_R])
                index_R += 1

            # Se alguma das listas é "esvaziada" então
            # copio os elementos restantes da outra lista
            # na lista de resultados e fecho/interrumpo o loop 
            if index_R == len(lista_R):
                result += lista_L[index_L:]
                break

            if index_L == len(lista_L):
                result += lista_R[index_R:]
                break

        return result



    def insertionSort(self, arr):
        # Traverse through 1 to len(arr) 
        for i in range(1, len(arr)): 
    
            key = arr[i] 
    
            # Move elements of arr[0..i-1], that are 
            # greater than key, to one position ahead 
            # of their current position 
            j = i-1
            while j >=0 and key < arr[j] : 
                    arr[j+1] = arr[j] 
                    j -= 1
            arr[j+1] = key 
    


    def quickSort(self, sequence):
        length = len(sequence)
        if length <= 1:
            return sequence
        else:
            pivot = sequence.pop()

        items_greater = []
        items_lower = []

        for item in sequence:
            if item > pivot:
                items_greater.append(item)

            else:
                items_lower.append(item)

        return self.quickSort(items_lower) + [pivot] + self.quickSort(items_greater)
    


    def countingSort(self, unsorted):
        result = [0] * len(unsorted)
        low = min(unsorted)      # we don't care if this is positive or negative any more!
        high = max(unsorted)
        count_array = [0 for i in range(low, high+1)]
        for i in unsorted:
            count_array[i-low] += 1             # use an offset index
        for j in range(1, len(count_array)):
            count_array[j] += count_array[j-1]
        for k in reversed(unsorted):
            result[count_array[k-low] - 1] = k  # here too
            count_array[k-low] -= 1             # and here
        return result 
    
    
    
    def getResults(self):
        return [self.algoritimo, self.endTime]


if __name__ == '__main__':
    x = Juiz()
