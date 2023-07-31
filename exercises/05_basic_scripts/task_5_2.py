# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
template = '''
Network:
{z0:<8}  {z1:<8}  {z2:<8}  {z3:<8}
{z0:08b}  {z1:08b}  {z2:08b}  {z3:08b}


Mask:
{mask}
{m0:<8}  {m1:<8}  {m2:<8}  {m3:<8}
{m0:08b}  {m1:08b}  {m2:08b}  {m3:08b}
'''
k = input('Введите адрес в формате Х.Х.Х.Х/Х: ')
m = k[:-3].split('.')
d = '1' * int(k[-2:]) + '0' * (32 - int(k[-2:]))
print(template.format(z0 = int(m[0]), z1 = int(m[1]), z2 = int(m[2]), z3 = int(m[3]), mask = k[-3:], m0 = int(d[:8], 2), m1 = int(d[8:16], 2), m2 = int(d[16:24], 2), m3 = int(d[24:], 2)))