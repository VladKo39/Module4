from math import inf

def divide(fiest, second):
    if second == 0:
        result = inf
    else:
        result = fiest / second
    return result
if __name__=="__main__":
    result1 = divide(69, 3)
    result2 = divide(3, 0)
    result3 = divide(49, 7)
    result4 = divide(15, 0)
    print(f'Результат inf {inf}')
    print(f'Результат1 true_math {result1}')
    print(f'Результат2 true_math {result2}')
    print(f'Результат3 true_math {result3}')
    print(f'Результат4 true_math {result4}')
