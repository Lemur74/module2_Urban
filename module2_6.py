key = 0
answer = ''

if __name__ == '__main__':
    key = int(input("Введите ключ от 3 до 20: "))
    for i in range(1, key):
        for j in range(i, key):
            if key % (j + i) == 0 and i != j:
                    answer += str(i)
                    answer += str(j)

    print( f"Ответ - {answer}")