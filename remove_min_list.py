def remove_smallest(numbers):
    sortnum = numbers
    for num in sortnum:
        if num == min(sortnum):
            sortnum.remove(num)
            return sortnum
        
        