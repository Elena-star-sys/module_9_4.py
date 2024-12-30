# # Функциональное разнообразие
#
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
#
# result = list(map(lambda x, y: x == y, first, second))
# print(result)

# Замыкание

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for element in data_set:
                file.write(str(element) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print(list(write))








