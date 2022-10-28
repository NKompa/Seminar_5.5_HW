# Напишите программу, удаляющую из текста все слова, содержащие "абв".

string1 = 'дадавбвдфв жацэабвдаы абвц дабв фыдлао жаж ждлфывабв'
print(string1)
list1 = string1.split()
list2 = []
for i in range(len(list1)):
    if 'абв' not in list1[i]:
        list2.append(list1[i])
string1 = ' '.join(list2)
print(string1)