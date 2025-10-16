s = input("enter string, like hello_world: ")

list_s = list(s)

flag = 0
for i in range(0, len(list_s)):
    if list_s[i] == '_':
        list_s[i] = ''
        flag = 1
    else:
        if flag == 1:
            list_s[i] = list_s[i].upper()
            flag = 0

print("".join(list_s))