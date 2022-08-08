# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
# то в итоге будет, 3*x^3 + 12*x^2+10*x+66

# ЗАДАЧА ВЫПОЛНЕНА ТОЛЬКО ПРИ УСЛОВИИ ПОЛОЖИТЕЛЬНЫХ ЧЛЕНОВ В ИСХОДНЫХ МНОГОЧЛЕНАХ

from posixpath import split
import re

path = r'folder/file22_1.txt'
with open (path, 'r') as f:
    data1 = list(f.read().split())
    print(data1)    
path = r'folder/file22_2.txt'
with open (path, 'r') as f:
    data2 = list(f.read().split())
print(data2) 

def udal (data): # удаление +
    data3 = []
    for i in range (len(data)):
        if '+' not in data[i]:
            data3.append(data[i])
    return data3

data1 = (udal(data1))       
data2 = (udal(data2)) 
print (udal(data1))       
print (udal(data2))        


def pre1 (data): # добавление степени 1  
    for i in range (len(data)):
        if '^' not in data[i] and 'x' in data[i] and data[i] != '+':
            data[i] += '^1'
    return data

data1 = (pre1(data1))       
data2 = (pre1(data2)) 
print (pre1(data1))       
print (pre1(data2))     

def pre (data): # добавление x^0 к числовому значению
    for i in range (len(data)):
        if 'x' not in data[i] and data[i] != '+' and data[i] != '-':
            data[i] += 'x^0'
    return data

data1 = pre(data1)       
data2 = pre(data2)   
print(data1)
print(data2)


def spli (data): # разделение по x^
    for i in range(len(data)):
        data[i] = data[i].split('x^')
    return(data)    

data1 = spli (data1) 
print(data1)   
data2 = spli (data2) 
print(data2)  


def dic (data): # перевод списка в словарь
    all = {}
    for i in range(len(data)):
        all[data[i][1]] = int(data[i][0]) 
    return all

di1 = dic (data1) 
print(di1)   
di2 = dic (data2) 
print(di2)  


def su1 (di1, di2): #сложение словарей по ключам (при их совпадении)
    di3 = di1
    for key, value in di2.items():
        if key in di1:
            di3[key] += value
        else:
            di3.update({key: value})
    return(di3)

su = su1(di1, di2)
print(su)  


def res (su):
    result = ''
    for key, val in su.items():
        if(int(val) > 0):
            result += "+" + str(val) + "x^" + key 
        elif(int(val) < 0):
            result += str(val) +"x^" + key   
    return (result)

print(res (su))   

f = open('folder/file22_4.txt', 'w')
f.writelines(su)
f.close