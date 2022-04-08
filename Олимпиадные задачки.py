#!/usr/bin/env python
# coding: utf-8

# # Модуль 1: Сортировки и бинарный поиск

# ## A. Квадратичные сортировки

# Отсортируйте массив по неубыванию. (сделал встроенной сортировкой)

# In[ ]:


fin  = open("input.txt")
fout = open("output.txt","w")

f1 = fin.readline()
M = fin.readline()
print(f1)
print(f2)

Mas = []
dop=''
for i in range(len(M)):
    if(M[i] == ' '):
        Mas.append(int(dop))
        dop = ''
    else:
        dop += M[i]
Mas.append(int(dop))
Mas.sort()
print(Mas)


for i in Mas:
    fout.write(str(i))
    fout.write(" ")
        
fin.close()
fout.close()


# ## B. Сортировка слиянием

# Отсортируйте данный массив, используя сортировку слиянием.
# 
# ##### Входные данные
# Первая строка содержит число n (1≤n≤105). Далее идет n целых чисел, не превосходящих по абсолютной величине 109.
# 
# ##### Выходные данные
# Выведите числа в порядке неубывания.

# In[2]:


n = int(input())
M = [int(x) for x in input().split()]

def merge(M1, M2): #на вход ОТСОРТИРОВАННЫЕ массивы
    
    M = [] # результат слияния
    i = 0 # бежим по M1
    j = 0 # проход по M2
    
    while i < len(M1) and j < len(M2):
        if M1[i] < M2[j]:
            M.append(M1[i])
            i += 1
        else:
            M.append(M2[j])
            j += 1
    
    if i == len(M1):
        while j < len(M2):
            M.append(M2[j])
            j += 1
    if j == len(M2):
        while i < len(M1):
            M.append(M1[i])
            i += 1
    return M # конец функции merge

def merge_sort(M):
    if len(M) > 1:
        l = len(M) // 2
        return merge( merge_sort(M[:l]), merge_sort(M[l:]) ) 
    else: 
        return M

ANS = merge_sort(M)    
print(' '.join(map(str, ANS)))


# In[19]:


def merge_sort(M):
    if len(M) > 1:
        l = len(M) // 2
        return merge( merge_sort(M[:l]), merge_sort(M[l:]) ) 
    else: 
        return M
    
print(merge_sort(M))


# ## I. Дипломы

# Когда Петя учился в школе, он часто участвовал в олимпиадах по информатике, математике и физике. Так как он был достаточно способным мальчиком и усердно учился, то на многих из этих олимпиад он получал дипломы. К окончанию школы у него накопилось n дипломов, причём, как оказалось, все они имели одинаковые размеры: w — в ширину и h — в высоту. Сейчас Петя учится в одном из лучших российских университетов и живёт в общежитии со своими одногруппниками. Он решил украсить свою комнату, повесив на одну из стен свои дипломы за школьные олимпиады. Так как к бетонной стене прикрепить дипломы достаточно трудно, то он решил купить специальную доску из пробкового дерева, чтобы прикрепить её к стене, а к ней — дипломы. Для того чтобы эта конструкция выглядела более красиво, Петя хочет, чтобы доска была квадратной и занимала как можно меньше места на стене. Каждый диплом должен быть размещён строго в прямоугольнике размером w на h. Дипломы запрещается поворачивать на 90 градусов. Прямоугольники, соответствующие различным дипломам, не должны иметь общих внутренних точек. Требуется написать программу, которая вычислит минимальный размер стороны доски, которая потребуется Пете для размещения всех своих дипломов.
# 
# ##### Входные данные
# Входной файл содержит три целых числа: w, h, n (1≤w,h,n≤109).
# 
# ##### Выходные данные
# В выходной файл необходимо вывести одно целое число — ответ на поставленную задачу.
#     

# In[29]:


M = [int(x) for x in input().split()]
w, h, n = M

n1 = int(math.sqrt(n*h / w))
n2 = int(math.sqrt(n*w / h))
a1 = n1*2
a2 = n2*2

while (n1*w // w) * (n1*w // h) < n:
    n1 += 1
while (n2*h // w) * (n2*h // h) < n:
    n2 += 1
    
print(min(n2*h, n1*w))


# ## J. Провода

# Дано n (1≤n≤104) отрезков провода длиной l1, l2, ..., ln (100≤li≤107) сантиметров. Требуется с помощью разрезания получить из них k (1≤k≤104) равных отрезков как можно большей длины, выражающейся целым числом сантиметров. Если нельзя получить k отрезков длиной даже 1 см, вывести 0.
# 
# ##### Входные данные
# На первой строке заданы числа n и k. В следующих n строках заданы li по одному в строке. Все числа целые.
# 
# ##### Выходные данные
# Выведите одно число — полученную длину отрезков.

# In[50]:


N = input().split()
n = int(N[0])
k = int(N[1])
M = []
 
for i in range(n):
    M.append(int(input()))
hight = 0
for i in range(n):
    hight = hight + M[i] 
hight = hight // k
 
 
def func(a): 
    sum = 0
    for i in range(n):
        sum = sum + M[i] // a
    return sum 
 
low = hight 
while low > 0 and func(low) < k:
    low = low // 2
 
if low == 0:
    print(0)
else:
    low = low
    hight = hight
    ans = low
    while hight - low > 1:
        ans = (low + hight) // 2
        if func(ans) < k: 
            hight = ans
        else:
            low = ans
    print(low)


# # Модуль 2: Динамика

# ## A. Числа Фибоначчи

# f1=f2=1, fn+1=fn+fn−1 при n>2.
# 
# Входные данные
# В единственной строке входных данных записано натуральное число n (1≤n≤45).
# 
# Выходные данные
# Выведите число fn.

# In[4]:


n = int(input())

def fib(n):
    if n <= 2:
        return 1
    else:
        fib1 = 1
        fib2 = 1
        for i in range(n-2):
            fib1, fib2 = fib2, fib1+fib2
        return fib2

print(fib(n))


# ## B. Платная лестница

# Мальчик подошел к платной лестнице. Чтобы наступить на любую ступеньку, нужно заплатить указанную на ней сумму. Мальчик умеет перешагивать на следующую ступеньку, либо перепрыгивать через ступеньку. Требуется узнать, какая наименьшая сумма понадобится мальчику, чтобы добраться до верхней ступеньки.

# (переформулировали задачу о кузнечике в других терминах)

# In[14]:


n = int(input())
Costs = [int(x) for x in input().split()]
if n > 1:
    Solve = [Costs[0], Costs[1]]
    for i in range(2, n, 1):
        Solve.append( min(Solve[i-1]+Costs[i], Solve[i-2]+Costs[i]) )
    print(Solve[n-1])
else:
    print(Costs[0])


# ## L. Без трех единиц

# Определите количество последовательностей из нулей и единиц длины n, в которых никакие три единицы не стоят рядом.

# In[19]:


n = int(input())
Solve = [2, 4, 7]
if n < 3:
    print(Solve[n-1])
else:
    for i in range(3, n, 1):
        Solve.append(Solve[i-1] + Solve[i-2] + Solve[i-3])
    print(Solve[n-1])


# ## K. НВП с восстановлением

# ##### Входные данные
# В первой строке входных данных задано число N  — длина последовательности (1≤N≤1000). Во второй строке задается сама последовательность (разделитель — пробел). Элементы последовательности — целые числа, не превосходящие 10000 по модулю.
# 
# ##### Выходные данные
# В первой строке выведите длину НВП. В следующей строке требуется вывести наибольшую возрастающую подпоследовательность данной последовательности. Если таких подпоследовательностей несколько, необходимо вывести одну (любую) из них.

# In[1]:


print(2)
print("1 2 3 4")


# In[21]:


n = int(input()) # длина входной последовательности
M = [int(x) for x in input().split()] # данная последовательность

dM = [1]*n # длина максимальной подпоследовательности, заканчивающейся в M[i]
ddM = [-1]*n # предыдущий индекс для максимальной последовательности, заканчивающейся в i-ом элементе

for i in range(1, n, 1):
    for j in range(i):
        if M[i] > M[j] and dM[j]+1 > dM[i]:
            dM[i] = dM[j]+1
            ddM[i] = j
            
len_max = 0
max_ind = 0
for i in range(n):
    if dM[i] > len_max:
        len_max = dM[i]
        max_ind = i
        
Result = [0]*len_max
ind = max_ind
for i in range(len_max):
    Result[len_max - 1 -i] = M[ind]
    ind = ddM[ind]
        
print(len_max)
print(' '.join(map(str, Result)))


# ## M. Маршрут максимальной стоимости

# В левом верхнем углу прямоугольной таблицы размером n⋅m находится черепашка. В каждой клетке таблицы записано некоторое число. Черепашка может перемещаться вправо или вниз, при этом маршрут черепашки заканчивается в правом нижнем углу таблицы.
# 
# Подсчитаем сумму чисел, записанных в клетках, через которую проползла черепашка (включая начальную и конечную клетку). Найдите наибольшее возможное значение этой суммы и маршрут, на котором достигается эта сумма.
# 
# ###### Входные данные
# В первой строке входных данных записаны два натуральных числа n и m, не превосходящих 100 — размеры таблицы. Далее идет n строк, каждая из которых содержит m чисел, разделенных пробелами — описание таблицы. Все числа в клетках таблицы целые и могут принимать значения от 0 до 100.
# 
# ###### Выходные данные
# Первая строка выходных данных содержит максимальную возможную сумму, вторая – маршрут, на котором достигается эта сумма. Маршрут выводится в виде последовательности, которая должна содержать n−1 букву D, означающую передвижение вниз, и m−1 букву R, означающую передвижение направо. Если таких последовательностей несколько, необходимо вывести ровно одну (любую) из них.

# In[82]:


M_n_m = [int(x) for x in input().split()]
n = M_n_m[0]
m = M_n_m[1]
M = [[]]*n
for i in range(n):
    M[i] = [int(x) for x in input().split()]
    
dM = []
ddM = []
for i in range(n):
    M_1 = []
    M_2 = []
    for j in range(m):
        M_1.append(M[i][j])
        M_2.append('S')
    dM.append(M_1)
    ddM.append(M_2)

for i in range(1, m, 1):
    dM[0][i] = dM[0][i-1] + M[0][i]
    ddM[0][i] = 'L' #откуда пришли в эту клетку
for i in range(1, n, 1):
    dM[i][0] = dM[i-1][0] + M[i][0]
    ddM[i][0] = 'U' #откуда пришли в эту клетку    
    
for i in range(1, n, 1): #по строкам - D
    for j in range(1, m, 1): #по столбцам - R
        if dM[i][j-1] > dM[i-1][j]:
            dM[i][j] = M[i][j] + dM[i][j-1]
            ddM[i][j] = 'L'
        else:
            dM[i][j] = M[i][j] + dM[i-1][j]
            ddM[i][j] = 'U'
    
Result = [0]*(n-1+m-1)
i = n-1
j = m-1
while i > 0 or j > 0:
    if ddM[i][j] == 'U':
        Result[i+j-1] = 'D'
        i = i -1
    if ddM[i][j] == 'L':
        Result[i+j-1] = 'R'
        j = j - 1
    
print(dM[n-1][m-1])
print(' '.join(map(str, Result)))


# # Модуль 3: Графы. DFS, BFS

# ### B. Дерево?
# 
# Имеется неориентированный граф, состоящий из N вершин и M ребер. Необходимо проверить, является ли граф деревом. Напомним, что дерево  — это связный граф, в котором нет циклов (следовательно, между любой парой вершин существует ровно один простой путь). Граф называется связным, если от одной вершины существует путь до любой другой.
# 
# ##### Входные данные
# Во входном файле в первой строке содержатся два целых числа N и M (1≤N≤100, 0≤M≤1000), записанные через пробел. Далее следуют M различных строк с описаниями ребер, каждая из которых содержит два натуральных числа Ai и Bi (1≤Ai,Bi≤N), где Ai и Bi  — номера вершин, соединенных i-м ребром.
# 
# ##### Выходные данные
# В выходной файл выведите слово «YES», если граф является деревом, или «NO» в противном случае.

# In[10]:


n, m = input().split()
n = int(n)
m = int(m)
M = []


if m != n-1:
    print('NO')
else:
    for i in range(n):
        M.append([])
    
    for i in range(m):
        a_i, b_i = input().split()
        a_i, b_i = int(a_i), int(b_i)
        M[a_i - 1].append(b_i-1)
        M[b_i - 1].append(a_i-1)

    used = [False]*n

    def dfs(v):
        used[v] = True
        for u in M[v]:
            if used[u] == False:
                dfs(u)
    dfs(0)
    
    if False in used:
        print('NO')
    else:
        print('YES')


# # D. Есть ли цикл?

# Дан ориентированный граф. Требуется определить, есть ли в нем цикл.
# 
# ##### Входные данные
# В первой строке вводится число n - количество вершин и m - количество ребер. (1≤n,m≤105). Далее в m строках следует по 2 числа u, v - вершины графа, соединенные ребром.
# 
# ##### Выходные данные
# Выведите 0, если в заданном графе нет цикла, и 1, если он есть.

# In[37]:


n, m = input().split()
n = int(n)
m = int(m)
M = []
stack = []

for i in range(n):
    M.append([])
    
for i in range(m):
    a_i, b_i = input().split()
    a_i, b_i = int(a_i), int(b_i)
    M[a_i - 1].append(b_i-1)

used = [1]*n

def dfs(v):
    used[v] = 2
    for u in M[v]:
        if used[u] == 2:
            res[0] = 1
            return res
        if used[u] == 1:
            dfs(u)
    used[v] = 3
    
used = [1]*n    
flag = False
res = [0]
    
for v in range(n):
    if used[v] == 1:
        dfs(v)
    
print(res[0])


# # F. Компоненты связности

# Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их.
# 
# ##### Входные данные
# Во входном файле записано два числа N и M (0<N≤100000,0≤M≤100000). В следующих M строках записаны по два числа i и j(1≤i,j≤N), которые означают, что вершины i и j соединены ребром.
# 
# ##### Выходные данные
# В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности в следующем формате: в первой строке количество вершин в компоненте, во второй - сами вершины в отсортированном порядке.

# In[49]:


n, m = input().split()
n = int(n)
m = int(m)
M = []

for i in range(n):
    M.append([])
    
for i in range(m):
    a_i, b_i = input().split()
    a_i, b_i = int(a_i), int(b_i)
    M[a_i - 1].append(b_i-1)
    M[b_i - 1].append(a_i-1)
    

used = [False]*n
Res = []

def bfs(v, New_comp):
    used[v] = True
    while len(stack) > 0:
        for u in M[v]:
            if used[u] == False:
                used[u] = True
                stack.append(u)
                New_comp.append(u+1)
        stack.remove(v)
        if len(stack) > 0:
            v = stack[0]

            
for ver in range(n):
    if used[ver] == False:
        stack = [ver]
        New_comp = [ver+1]
        bfs(ver, New_comp)
        New_comp.sort()
        Res.append(New_comp)

print(len(Res))
for comp in Res:
    print(len(comp))
    print(' '.join(map(str, comp)))


# # I. Путь в графе

# В неориентированном графе требуется найти длину минимального пути между двумя вершинами.
# 
# ##### Входные данные
# Первым на вход поступает число N  — количество вершин в графе (1≤N≤100). Затем записана матрица смежности (0 обозначает отсутствие ребра, 1  — наличие ребра). Далее задаются номера двух вершин  — начальной и конечной.
# 
# ##### Выходные данные
# Необходимо вывести длину пути в ребрах. Если пути нет, нужно вывести −1.

# In[70]:


n = int(input())
M = []
for i in range(n):
    dop = input().split()
    dop_dist = []
    for i in range(len(dop)):
        dop[i] = int(dop[i]) 
    M.append(dop)
    
start, finish = input().split()
start = int(start)
finish = int(finish)

M_dist = [-1] * n
M_dist[start - 1] = 0

used = [False]*n
stack = [start-1]

def bfs(v):
    used[v] = True
    for u in range(n):
        if M[v][u] == 1:
            if used[u] == False:
                used[u] = True
                stack.append(u)
                M_dist[u] = M_dist[v] + 1
    stack.remove(v)
    if len(stack) > 0:
        bfs(stack[0])
        
bfs(start-1)        
    
print(M_dist[finish - 1])


# # Модуль 6: Комбинаторика и теория чисел

# ## A. Двоичные строки заданной длины

# По данному числу N выведите все строки длины N из нулей и единиц в лексикографическом порядке.
# 
# ##### Входные данные
# Задано единственное число N. (натуральное, 1≤N≤10)
# 
# ##### Выходные данные
# Необходимо вывести все строки длины N из нулей и единиц в лексикографическом порядке, по одной на строке.

# In[50]:


n = int(input())

kol = 2**n

for num in range(kol):
    b = bin(num)
    b = b[2::]
    b = '0'*(n-len(b)) + b
    print(b)
    


# ## B. Все перестановки заданной длины

# По данному числу N выведите все перестановки чисел от 1 до N в лексикографическом порядке.
# 
# ##### Входные данные
# Задано 1 число: N (0<N<10).
# 
# ##### Выходные данные
# Необходимо вывести все перестановки чисел от 1 до N в лексикографическом порядке. Перестановки выводятся по одной в строке, числа в перестановке выводятся без пробелов.

# In[93]:


import sys
sys.setrecursionlimit(10000000)

n = int(input())

def func(M, s):
    
    if len(M) == 1:
        print(s + str(M[0]))
    else:
        for x in M:
            s_next = s + str(x)
            M_next = []
            for y in M:
                M_next.append(y)
            M_next.remove(x)
            func(M_next, s_next)

M = [x+1 for x in range(n)]
func(M, '')            


# In[92]:


n = int(input())

from itertools import permutations
perm = permutations([x+1 for x in range(n)])
for p in perm:
    print(''.join(map(str, p)))


# In[ ]:





# ## E. Проверка на простоту

# Проверьте, является ли число простым.
# 
# ##### Входные данные
# Вводится одно натуральное число $n <= 2⋅10^9$ и не равное 1.
# 
# ##### Выходные данные
# Необходимо вывести строку «prime», если число простое, или «composite», если число составное.

# In[9]:


n = int(input())

k = 2
flag = False

while k*k <= n:
    if n % k == 0:
        flag = True
        break
    k += 1
    
if flag:
    print('composite')
else:
    print('prime')
    


# ## G. Простые числа

# Вывести все простые числа от m до n включительно.
# 
# ##### Входные данные
# В первой строке находятся разделённые пробелом m и n. 1≤m≤n≤$10^7$.
# 
# ##### Выходные данные
# Вывести числа в порядке возрастания, по одному в строке. Если между m и n включительно нет простых  — вывести -1

# In[59]:


m, n = input().split()
m, n = max(2, int(m)), int(n)

if n == 1:
    print(-1)
else:
    prime = [True]*(n+1)

    flag = 1
    for i in range(2, n+1, 1):
        if prime[i]:
            j = 2*i
            for j in range(2*i, n+1, i):
                prime[j] = False
            if i >= m:
                print(i)
                flag = 0
    
    if flag == 1:
        print(-1)


# In[51]:


m, n = input().split()
m, n = max(2, int(m)), int(n)

if n == 1:
    print(-1)
else:
    prime = [True]*(n+1)

    flag = 1
    for i in range(2, n+1, 1):
        if prime[i]:
            j = 2*i
            for j in range(2*i, n+1, i):
                prime[j] = False
            if i >= m:
                print(i)
                flag = 0
    
    if flag == 1:
        print(-1)


# In[13]:


M = [1, 2, 3]
print(M[2::])


# ## H. Алгоритм Евклида

# По данным натуральным числам n и m найдите их наибольший общий делитель.
# 
# ##### Входные данные
# Программа получает на вход 2 натуральных числа $m, n ≤ 10^9.$
# 
# ##### Выходные данные
# Программа должна вывести наибольший общий делитель двух данных чисел.

# In[35]:


m = int(input())
n = int(input())

a = max(m, n)
b = min(m, n)

def NOD(a, b):
    if b == 0:
        print(a)
    else:
        c = a % b
        a, b = b, c
        NOD(a, b)
        
NOD(a, b)


# # Модуль 5. Продвинутая динамика

# ## A. Сумма длин путей

# Дано дерево на n вершинах. На каждом ребре написан его вес. Требуется посчитать сумму взвешенных длин всех путей в данном дереве. Пути ⟨v,u⟩ и ⟨u,v⟩ считаются различными.
# 
# ##### Входные данные
# Первая строка каждого теста содержит натуральное число n — количество вершин в дереве (1≤n≤100000). Следующие n−1 строк содержат по 3 натуральных числа v,u,w и описывают ребро дерева, соединяющее две вершины v и u и имеющее вес w (1≤v,u≤n, 0≤w≤106).
# 
# ##### Выходные данные
# Выведите единственное число — суммарную длину всех путей в дереве.

# In[23]:


n = int(input())

M = []
for i in range(n):
    M.append([])
    
M_dop = []
    
for i in range(n-1):
    u, v, w = input().split()
    M[int(u) - 1].append(int(v) - 1)
    M[int(v) - 1].append(int(u) - 1)
    M_dop.append([int(u) - 1, int(v) - 1, int(w)])
    


used = [False] * n
w = [-1]*n
stack = [0]

DOP = []

while len(stack) > 0:
    w[stack[0]] = 1
    used[stack[0]] = True
    dop = [stack[0]]
    for u in M[stack[0]]:
        if not used[u]:
            dop.append(u)
            stack.append(u)
    DOP.append(dop)
    stack.remove(stack[0])
    
DOP.reverse()
for mas in DOP:
    v = mas[0]
    mas.remove(v)
    for u in mas:
        w[v] += w[u]

sum_out = 0

for mas in M_dop:
    w_1 = mas[2]
    u = mas[1]
    v = mas[0]
    wei = min(w[u], w[v])
    sum_out += 2*w_1*wei*(n-wei)


print(sum_out)


# In[21]:


used = [False] * n
w = [-1]*n
stack = [0]

def bfs(start):
    used[start] = True
    w[start] = 1
    dop = []
    for u in M[start]:
        if not used[u]:
            dop.append(u)
            stack.append(u)
            
    stack.remove(start)
    if len(stack) > 0:
        bfs(stack[0])
    
    for u in dop:
        w[start] += w[u]


# In[17]:


DOP = []

while len(stack) > 0:
    w[stack[0]] = 1
    used[stack[0]] = True
    dop = [stack[0]]
    for u in M[stack[0]]:
        if not used[u]:
            dop.append(u)
            stack.append(u)
    DOP.append(dop)
    stack.remove(stack[0])
    
DOP.reverse()
for mas in DOP:
    v = mas[0]
    mas.remove[v]
    for u in mas:
        w[v] += w[u]
    
    


# In[29]:


import threading
threading.stack_size(2**27)

n = int(input())
 
M = []
for i in range(n):
    M.append([])
    
M_dop = []
    
for i in range(n-1):
    u, v, w = input().split()
    M[int(u) - 1].append(int(v) - 1)
    M[int(v) - 1].append(int(u) - 1)
    M_dop.append([int(u) - 1, int(v) - 1, int(w)])
    
 
 
used = [False] * n
w = [-1]*n
stack = [0]
 
def bfs(start):
    used[start] = True
    w[start] = 1
    dop = []
    for u in M[start]:
        if not used[u]:
            dop.append(u)
            stack.append(u)
            
    stack.remove(start)
    if len(stack) > 0:
        bfs(stack[0])
    
    for u in dop:
        w[start] += w[u]
                
threading.Thread(target=bfs(0)).start()
 
sum_out = 0
 
for mas in M_dop:
    w_1 = mas[2]
    u = mas[1]
    v = mas[0]
    wei = min(w[u], w[v])
    sum_out += 2*w_1*wei*(n-wei)
 
    
print(sum_out)


# ## C. НВП

# Числовая последовательность задана рекуррентной формулой: $a_{i+1}=(k⋅a_i+b)mod(m)$. Найдите её наибольшую возрастающую подпоследовательность. Если таких последовательностей несколько, можно вывести любую.
# 
# ##### Входные данные
# Программа получает на вход пять целых чисел: длину последовательности n (1≤n≤105), начальный элемент последовательности a1, параметры k,b,m для вычисления последующих членов последовательности (1≤m≤104,0≤k<m,0≤b<m,0≤a1<m).
# 
# ##### Выходные данные
# На первой строке выходного файла вы должны вывести количество чисел в найденной вами наибольшей возрастающей подпоследовательности. На следующей строке выведите элементы подпоследовательности, разделяя их пробелами.

# In[64]:


import math

n, a1, k, b, m = input().split()
n = int(n)
a1 = int(a1)
k = int(k)
b = int(b)
m = int(m)

dp = [0]*n
opt = [1000000]*(n+1)
opt[0] = -1000

a_next= a1 
ans = 1

def func_bin(a):
    first = 0
    last = n
    while last-first > 1:
        middle = (last+first) // 2
        if opt[middle] > a:
            last = middle
        else:
            first = middle
    if opt[first] == a:
        return first
    else: 
        return last

A = []
M_prev = [-1]*(n)

for i in range(n):
    j = func_bin(a_next)
    A.append(a_next)
    opt[j] = a_next
    dp[i] = j
    M_prev[i] = opt[j-1]
    ans = max(ans, j)
    a_next = (k*a_next + b) % m
    
print(ans)

j = 1
Result = [-1]*ans
prev = 10000000
while ans > 0:
    if dp[n-j] == ans:
        if A[n-j] < prev:
            Result[ans-1] = A[n-j]
            prev = A[n-j]
            ans -= 1
    j += 1
    
print(' '.join(map(str, Result)))


# ## E. Максимальный подпалиндром

# Палиндромом называется строка, которая одинаково читается как слева направо, так и справа налево. Подпалиндромом данной строки называется последовательность символов из данной строки, не обязательно идущих подряд, являющаяся палиндромом. Например, «HELOLEH» является подпалиндромом строки «HTEOLFEOLEH.» Напишите программу, находящую в данной строке подпалиндром максимальной длины.
# 
# ##### Входные данные
# На вход подается строка длиной не более 100 символов, состоящая из заглавных букв латинского алфавита.
# 
# ##### Выходные данные
# Выведите на первой строке выходного файла длину максимального подпалиндрома, а на второй строке сам максимальный подпалиндром. Если таких подпалиндромов несколько, то ваша программа должна вывести любой из них.

# In[24]:


strin = input()

str_in = []
str_rev = []

for s in strin:
    str_in.append(s)
    str_rev.append(s)
    
str_rev.reverse()

A = str_in
B = str_rev

n = len(A)
m = len(B)
F = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            F[i][j] = F[i - 1][j - 1] + 1 
        else: 
            F[i][j] = max(F[i - 1][j], F[i][j - 1]) 
print(F[n][m])
               
Ans = []
i = n
j = m
while i > 0 and j > 0:
    if A[i - 1] == B[j - 1]:
        Ans.append(A[i - 1])
        i -= 1
        j -= 1
    elif F[i - 1][j] == F[i][j]:
        i -= 1 
    else: 
        j -= 1
        
print(''.join(map(str, Ans)))


# In[ ]:





# # Модуль 4: Кратчайшие пути во взвешенных графах

# ## A. Дейкстра

# Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние от одной заданной вершины до другой.
# 
# ##### Входные данные
# В первой строке содержатся три числа: N, S и F (1≤N≤100, 1≤S,F≤N), где N  — количество вершин графа, S  — начальная вершина, а F  — конечная. В следующих N строках вводится по N чисел, не превосходящих 100,  — матрица смежности графа, где −1 означает отсутствие ребра между вершинами, а любое неотрицательное число  — присутствие ребра данного веса. На главной диагонали матрицы записаны нули.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




