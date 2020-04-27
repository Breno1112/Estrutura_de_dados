import time
import random
import xlsxwriter

class Juiz():
    def __init__(self):
        self.algoritimos = ['bubble sort', 'mergesort', 'insertion sort', 'quicksort', 'counting sort']
        self.NumeroDeListas = 10
        self.row = 0
        # self.tamanhos = [1000, 10000, 100000, 1000000, 10000000]
        self.tamanhos = [1, 10, 100, 1000, 10000]
        self.comecarXLS()
        print('Iniciando avaliação de algorítimos')
        self.rotina()
    def rotina(self):
        for x in self.algoritimos:
            # self.gerarListas()
            self.testar(x, self.gerarListas())
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
        for x in results[1]:
            self.worksheet.write(self.row, cell, x)
            cell += 1
        self.workbook.close()
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
            'mergesort': self.mergesort,
            'insertion sort': self.insertionSort,
            'quicksort': self.quickSort,
            'counting sort': self.countingSort
        }
        got = switcher.get(self.algoritimo, lambda: False)
        if got != False:
            for x in self.listas:
                for y in x:
                    got(y)
                    print('fim')
    def bubleSort(self, nlist):
        self.startTime = time.time()
        for passnum in range(len(nlist)-1,0,-1):
            for i in range(passnum):
                if nlist[i]>nlist[i+1]:
                    temp = nlist[i]
                    nlist[i] = nlist[i+1]
                    nlist[i+1] = temp
        self.endTime.append(time.time() - self.startTime)
    def mergesort(self, arr, l, r):
        if l < r: 
            # Same as (l+r)//2, but avoids overflow for 
            # large l and h 
            m = (l+(r-1))//2
    
            # Sort first and second halves 
            self.mergesort(arr, l, m) 
            self.mergesort(arr, m+1, r) 
            self.merge(arr, l, m, r) 
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r- m 
  
        # create temp arrays 
        L = [0] * (n1) 
        R = [0] * (n2) 
    
        # Copy data to temp arrays L[] and R[] 
        for i in range(0 , n1): 
            L[i] = arr[l + i] 
    
        for j in range(0 , n2): 
            R[j] = arr[m + 1 + j] 
    
        # Merge the temp arrays back into arr[l..r] 
        i = 0     # Initial index of first subarray 
        j = 0     # Initial index of second subarray 
        k = l     # Initial index of merged subarray 
    
        while i < n1 and j < n2 : 
            if L[i] <= R[j]: 
                arr[k] = L[i] 
                i += 1
            else: 
                arr[k] = R[j] 
                j += 1
            k += 1
    
        # Copy the remaining elements of L[], if there 
        # are any 
        while i < n1: 
            arr[k] = L[i] 
            i += 1
            k += 1
    
        # Copy the remaining elements of R[], if there 
        # are any 
        while j < n2: 
            arr[k] = R[j] 
            j += 1
            k += 1
    
    # l is for left index and r is right index of the 
    # sub-array of arr to be sorted 
    def insertionSort(self, valores):
        print('insertion sort')
        for x in self.listas:
            self.startTime = time.time()
            # print(x)
            self.endTime.append(time.time() - self.startTime)
    def quickSort(self, valores):
        print('quicksort')
        for x in self.listas:
            self.startTime = time.time()
            # print(x)
            self.endTime.append(time.time() - self.startTime)
    def countingSort(self, valores):
        print('counting sort')
        for x in self.listas:
            self.startTime = time.time()
            # print(x)
            self.endTime.append(time.time() - self.startTime)
    def getResults(self):
        return [self.algoritimo, self.endTime]


if __name__ == '__main__':
    x = Juiz()