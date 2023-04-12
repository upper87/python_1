
# Все алгоритмы сортировки из examples/ оберните в функции
def benchmark(iters=1):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print(f'[*] Среднее время выполнения: {total / iters} секунд.')
            return return_value

        return wrapper

    return actual_decorator

def bubble_sort(nums) -> None:
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            count += 1
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1


def sort_choice(nums) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):

            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1



def quick_sort(nums):

    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def partition(nums, low, high):
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            nums[i], nums[j] = nums[j], nums[i]

    def _quick_sort(items, low, high):
        if low < high:
            # Индекс опорного элемента
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# Напишите функцию для заполнения списка случайными числами

def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    numbers = []
    for _ in range(size):
        numbers.append(random.randint(at, to))

    return numbers
@benchmark
def demo_sort(nums):
    nums.sort()


# data = gen_list(1_000_000)
# quick_sort(data)
# print(f"{count}")

data = gen_list(1000)
demo_sort(data)

#sort_choise
# n / count
# 100 / 4950
# 1000 / 499500
# 10000 / 49995000
# count f(n) = 0.5 * n ** 2
# O n ** 2

#bubblet_choise
# n / count
# 100 / 5000
# 1000 / 500000
# 10000 / 49972845
# count f(n) = 0.5 * n ** 2
# O = n ** 2

#quick_choise
# n / count
# 100 / 260 ~ 2.6 * 100
# 1000 / 3850 ~ 3.8 * 1000
# 10000 / 55000 ~ 5.5 * 10000
# 100000 / 710000
# 1_000_000 / 8_750_000
# count f(n) = 0.5 * n ** 2
# O log(n) * n

# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков