def my_max(*args):
    max_el = args[0]
    for el in args:
        if el > max_el:
            max_el = el
            
    return max_el


my_max(3, 5)
my_max(3, 5, 8)
my_max(3, 5, 8, 12, -6)