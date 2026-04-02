number = "1924"
temp = list(number.strip())
temp.sort(reverse= True)
print("".join(temp[:-k]))