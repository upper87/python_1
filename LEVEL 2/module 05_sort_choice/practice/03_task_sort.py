# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов
def sort_choice(nums, reverse=False) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if reverse:
                rule_sort = nums[j] < nums[m]
            else:
                rule_sort = nums[j] > nums[m]
            if rule_sort:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
sort_choice(numbers, reverse=True)
print(sum(numbers[:5]))
# summ = 0
# for num in numbers[:5]:
#     summ += num
# print(summ)
