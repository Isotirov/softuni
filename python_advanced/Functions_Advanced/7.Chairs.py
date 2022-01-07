def chairs_comb(name, count, current_name=[]):
    if len(current_name) == count:
        print(', '.join(current_name))
        return
    for i in range(len(name)):
        current_name.append(name[i])
        chairs_comb(name[i+1:], count, current_name)
        current_name.pop()


names = input().split(", ")
n = int(input())
chairs_comb(names, n)
