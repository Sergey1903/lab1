# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=','):
    # Создаём множества участников первой и второй группы
    group1_set = set(participants_first_group.split(separator))
    group2_set = set(participants_second_group.split(separator))

    # Находим общие элементы
    common_elements = group1_set & group2_set

    # Возвращаем список общих участников, отсортированных в алфавитном порядке
    return sorted(common_elements)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", result)