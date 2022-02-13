import os
os.sysconf('SC_CLK_TCK')
def sort_func(array:list[int])->list[int]:
    """Быстрая сортировка
    Высокая скорость обеспечена за счет только лишь рекурсивных затрат"""
    if len(array) <= 1:
        return array
    else:
        barrier=array[0]
    l_vals = [n for n in array if n < barrier]

    m_vals = [barrier] * array.count(barrier)
    r_vals = [n for n in array if n > barrier]
    return sort_func(l_vals) + m_vals + sort_func(r_vals)

if __name__ == "__main__":
    #примеры
    vals_l=[1,0,14,3,2,7,6,9,1,4,2,5,8]
    print(sort_func(vals_l))
    os.sysconf(sort_func(vals_l))