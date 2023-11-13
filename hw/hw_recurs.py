def recursive_search(lst, target, index=0):
    if target in lst:
        if lst[index] == target:
            print(index)
        else:
            recursive_search(lst, target, index+1)
    else:
        print(-1)
    return
lst_1 = [1, 2, 3, 4, 5, 6, 7]
recursive_search(lst_1, 4)
