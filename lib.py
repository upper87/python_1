def palindrome(number):
    return str(number) == str(number)[::-1]
def distance(x1, y1, x2, y2):
    dist = (((x2-x1)**2)+((y2-y1)**2)) ** 0.5
    return dist