### Задача 2. Написать функцию/метод, которая на вход получает массив положительных целых чисел произвольной длины. 
### Например [42, 12, 18]. На выходе возвращает массив чисел, которые являются общими делителями для всех указанных числе. В примере это будет [2, 3, 6].

def count_dupl(lst_in): # На входе список, на выходе список с кортежами, вторым элементом количество повторов
    lst_out = []
    filter_lst = []
    for i in lst_in:
        if i not in filter_lst:
            filter_lst.append(i)
            lst_out.append((i, lst_in.count(i)))
        pass
    # print(lst_out)
    return lst_out
        
def common_deviders(lst_in):
    lst_out_all = []
    for i in lst_in:
          for j in range(1, i+1):
            if i%j == 0:
                lst_out_all.append(j)
    print('lst_out_all', lst_out_all)
    print('lst_in', lst_in)
    lst_with_dub = count_dupl(lst_out_all)
    print('lst_with_dub', lst_with_dub)
    lst_result = [i[0] for i in lst_with_dub if i[1] == len(lst_in) and i[0] != 1]
    print(lst_result)

if __name__ == "__main__":
     common_deviders([42, 12, 18])