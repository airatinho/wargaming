"""Задание №2 класса циклического буффера"""
import timeit
class Buffer_1:
    """Первый класс - включает себя множество проверок,
     возможность итерироваться, имеется возможность вывода текущего буфера,
      добавление новых элементов в конец и удаление старых элементов с начала.
       Число переменных и размер буфера ограничены

       "+" : Множество проверок, возможность итерироваться, защита от перегрузки класса,
            возможность изьятия буффера
       "-": ограничен тип входного контейнера данных - только list
            ограничен тип входных данных - только int,float, str

       """
    __slots__ = ("size","enter_container","__size","__num","__container")
    def __init__(self,size:int=0,enter_container:list=None):
        self.__size=size if not enter_container else len(enter_container)
        self.__num=0
        self.__container=enter_container if enter_container else []

    def __check_container(self):
        if not isinstance(self.__container,list):
            raise TypeError("Enter container should be list")

    def __check_val(self,value):
        if not (isinstance(value,int) or isinstance(value,float) or isinstance(value,str)):
            raise ValueError("Value should be int or float")
    def append(self,value):
        self.__check_val(value)
        if len(self.__container)>=self.__size:
            self.__container.pop(0)
            self.__container.append(value)
        else:
            self.__container.append(value)

    @property
    def container(self):
        return self.__container


    def __iter__(self):
        return iter(reversed(self.__container))

    def __next__(self):
        if self.__num>=self.__size:
            raise StopIteration
        self.__num+=1
        return self.__container[self.__num]
class Buffer_2:
    """Второй класс - включает себя множество проверок,
      имеется возможность вывода текущего буфера,
      добавление новых элементов в начало и удаление старых элементов с конца.
       Число переменных ограничено

       "+" : Множество проверок,  защита от перегрузки класса,
            возможность изьятия буффера
       "-": ограничен тип входного контейнера данных - только list
            ограничен тип входных данных - только int,float, str,
       """
    __slots__ = ("size","enter_container","__size","__container")
    def __init__(self,size:int=0,enter_container:list=None):
        self.__size=size if not enter_container else len(enter_container)
        self.__container=enter_container if enter_container else []

    def __check_container(self):
        if not isinstance(self.__container,list):
            raise TypeError("Enter container should be list")

    def __check_val(self,value):
        if not (isinstance(value,int) or isinstance(value,float) or isinstance(value,str)):
            raise ValueError("Value should be int or float")
    def append(self,value):
        self.__check_val(value)
        if len(self.__container)>=self.__size:
            self.__container.pop()
            self.__container.insert(0,value)
        else:
            self.__container.insert(0,value)

    @property
    def container(self):
        return self.__container

if __name__ == "__main__":
    b1 = Buffer_1(size=10)
    for i in range(0, 15):
        b1.append(i)
    print(b1.container)
    b2 = Buffer_2(size=10)
    for i in range(0, 15):
        b2.append(i)
    print(b2.container)