#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Задание1
lst1 = [1, 3, 5, 7, 9, 19, 11, 41, 4]
lst2 = [3, 8, 6, 5, 11]
res = []
for i in lst1:
    if i not in lst2:
        res.append(i)
lst1 = res

print(res)


# In[ ]:


str_data = '12.02.2000'
list_data = str_data.split('.')

dict_days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвёртое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвёртое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое',
}

dict_months = {
    '01': 'января',
    '02': 'февраль',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря',
}

print(dict_days.get(list_data[0]) + ' ' + dict_months.get(list_data[1]) + ' ' + list_data[2] + ' года')

