l = [1, 2, 3, 2, 3]
temp = [1] * (len(l)+1)

for i in range(len(l)):
    start = 0
    if start <= len(l):
        while l[i] <= l[start]:
            start += 1
            temp[i] += 1
print(temp)

