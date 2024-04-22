import numpy as np
import math
# Параметры задачи
Q = 500 #Количество сыра в заказе
K = 40000 #Издержки заказа
H = 5000 #Издержки хранения, 5000 в год
P = 100000 #Упущенная прибыль
td = 10  # в днях, время выполнения заказа
D = 500 #годовой спрос на сыр, 500 головок
W = 250 #Число рабочих дней
print("Q = 500 #Количество сыра в заказе, K = 40000 Издержки заказа, H = 5000 Издержки хранения, 5000 в год, P = 100000 Упущенная прибыль")
print("td = 10  в днях, время выполнения заказа, D = 500 годовой спрос на сыр, 500 головок, W = 250 Число рабочих дней")


#Решение с помощью интернета
# Минимальные общие издержки без дефицита
Q_EOQ = np.sqrt(2*Q*K/H)
print("Количество головок сыра для минимальных общих издержек без дефицита:", Q_EOQ)

# Минимальные общие издержки с допустимым дефицитом
Q_EPQ = np.sqrt(2*Q*K*(H+P)/H/P)
print("Количество головок сыра для минимальных общих издержек с допустимым дефицитом:", Q_EPQ)

# Точка восстановления запаса
R = Q/W*td
print("Точка восстановления запаса:", R)


#Здесь идёт решение уже по теории

# Максимальный размер дефицита
D = Q_EPQ-R
print("Максимальный размер дефицита:", D)
print("")
print("Решение по модели")
QZ = np.sqrt(2 * D * K / H) * np.sqrt((P + H) / P)
print("Рассчитаем оптимальное количество заказываемых головок сыра, так чтобы не допустить дефицита и иметь при этом минимальные общие издержки (EOQ): QZ = np.sqrt(2 * D * K / H) * np.sqrt((P + H) / P)")
print("Ответ: Следует заказывать ", QZ, "головки сыра, чтобы не допустить дефицита и иметь при этом минимальные общие издержки.")

#2.	Рассчитаем количество головок сыра для заказа, если допустим дефицит:
print("Сравним издержки хранения и упущенную прибыль (K/P), получилось: ", K/P, "Так как K / P << 1, то допускать дефицит не выгодно.")
#Так как K / P << 1, то допускать дефицит не выгодно.
Q = D * np.sqrt(K / (2 * P))
print("Оптимальное количество заказа: ", Q)
R = D / W
print("Средний спрос за день", R)

#Максимальный размер дефицита равен разности оптимального размера заказа (Q) и максимального размера запаса (S)
S = np.sqrt(2*D*K/H) * np.sqrt(P/(H+P))
print("Максимальный размер дифицита", S)