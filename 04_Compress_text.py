# Реализуйте RLE алгоритм: модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

with open('Input.txt') as input:
    original_str = input.readline()
print(original_str)

code = ''
symbol = original_str[0]
count = 1
for i in range(1,len(original_str)):
    if original_str[i] == symbol:
        count+=1
    else:
        code = code + str(count) + symbol
        symbol = original_str[i]
        count = 1
code = code + str(count) + symbol
print(code)

with open('Output.txt','w') as output:
    output.write(code)

decode = ''
count = code[0]
for i in range(1,len(code)):
    if code[i].isdigit():
        count = count+code[i]
    else:
        decode = decode + code[i]*int(count)
        count = ''
print(decode)