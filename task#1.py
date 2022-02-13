"""Задание №1
Так как функция простая - решил использовать лямбда функцию """
import timeit
import random
func=lambda x : x%2==0
if __name__ == "__main__":
    val=random.randint(0,10*8)
    print(val,func(val))
