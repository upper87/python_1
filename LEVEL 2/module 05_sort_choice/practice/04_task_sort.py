# Сумма наибольших по модулю
# # Дан массив(список) чисел.
# # Найти: сумму 5-ти самых больших элементов по модулю.
# # Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# # В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3
#

#
def nothing(n):
    return n
def sort_choice(nums, reverse=True, key=lambda n: n) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if reverse:
                rule_sort = key(nums[j]) < key(nums[m])
            else:
                rule_sort = key(nums[j]) > key(nums[m])
            if rule_sort:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

sort_choice(numbers)
print(numbers)

print(sum(numbers[:5]))
