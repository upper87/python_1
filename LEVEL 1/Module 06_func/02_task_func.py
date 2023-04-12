def palindrome(number):
    return str(number) == str(number)[::-1]
    # u_line = line[::-1]
    # if line == u_line:
    #     return True
    # return False




# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))