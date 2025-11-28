import math
n, k, m = 26, 6, 4

total = math.comb(n, k) # общее кол-во способов выбрать k карточек из n

win = 0
for i in range(m, k+1):
    win += math.comb(k, i) * math.comb(n-k, k-i)
    #(k,i) - выбираем совпавшие числа из билета
    #(n-k, k-i) - выбираем остальные карточки из других чисел

percent = win / total * 100 
print('Вероятность выигрыша в такую лотерею:', round(percent, 4), '%')
