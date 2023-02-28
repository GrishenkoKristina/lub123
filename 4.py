
r='красный'
y='желтый'
b='синий'
color1=input('Введите первый цвет ')
color2=input('Введите второй цвет ')
if(color1!=r and color1!=y and color1!=b or color2!=r and color2!=y and color2!=b): print('Ошибка. Повторите ввод')
else:
    if (color1==r and color2==y or color2 == r and color1 == y): print('Оранжевый')
    if (color1==r and color2==b or color2 == r and color1 == b): print('Фиолетовый')
    if (color1==b and color2==y or color2 == b and color1 == y): print('Зеленый')