#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random

n = int(input()) # вход - количество массивов
Result = [] # массив с массивами - результат работы программы

list_of_lens = [x for x in range(1, 5*n, 1)] # создадим массив из возможных длин массивов. Будем случайным образом 
                                            #выбирать элемент из этого списка, а затем убирать из него выбранную длину

for i in range(n): # на каждой итерации цикла создаю массив, генерирую его длину, а затем заполняю его
    
    M = []
    rand_len = random.choice(list_of_lens)
    list_of_lens.remove(rand_len) #удяляем выбранный элемент, чтобы не смогли взять его второй раз (хотим массивы разной длины)
    for j in range(rand_len): # заполнение массива
        next_el = random.randint(0, 100*n) #генерация случайного элемента, который будет добавлен в массив
        M.append(next_el)
        
    if i % 2 == 0:
        M = sorted(M) #с четными номерами по Возрастанию 
    else:
        M = sorted(M, reverse = True) #с НЕчетными номерами по Убыванию 
        
    Result.append(M)
    
print(Result)


# In[ ]:





# In[ ]:




