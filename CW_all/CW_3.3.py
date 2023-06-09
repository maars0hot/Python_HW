# №3.3[21]. Напишите программу для печати всех уникальных значений в списке словарей.

# Примечание: Список словарей задан изначально. Пользователь его не вводит

# Обратите внимание, что в словарях может быть один или несколько элементов

# Примеры/Тесты:

# Input: [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, 
#{"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ":" S009 "}, 
#{" VIII ":" S007 ", "XII": "D001"}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list1=[{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ":" S009 "}, 
{" VIII ":" S007 ", "XII": "D001"}]

# result=set()
# for item in list1:
#     for key,value in item.items():
#         result.add(value.strip())
# print(result)

result ={value.strip():key for item in list1 for key,value in item.items()}
print(result)