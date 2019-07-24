#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Задание 1

entered_number = int(input('Введите число: '))
print(entered_number + 2)


# In[2]:


#Задание 2
number = int(input('Введите число от 0 до 10: '))

while number > 10 or number < 0: 
    print('Упс! Число неверно.')
    number = int(input('Введите число от 0 до 10: '))
if 0 < number < 10:
    print(number ** 2)


# In[4]:


#Задание 3
#Медицинская анкета
name_surname = input('Напишите своё имя и фамилию: ')
weight = int(input('Какой у Вас вес?: '))
age = int(input('Сколько Вам лет?: '))
 
print('Хорошее состояние:', 12 < age < 30 and 50 < weight < 120)
print('Следует заняться своим здоровьем:', age > 30 and weight < 50 and weight > 100)     
print('Требуется врачебный осмотр:', age > 40 and weight < 50 and weight > 120)   
print('Требуется помощь специалиста:', age < 12 and weight > 50) 

