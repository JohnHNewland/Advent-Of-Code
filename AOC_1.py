file = open("input_AOC_1.txt", "r")
list1 = []
list2 = []
for x in file:
    list1.append(int(x[0:5])) 
    list2.append(int(x[8:13]))
file.close()

similarity = 0
for iterator in list1:
    similarity += iterator * list2.count(iterator)
print(similarity)

total = 0
while list1:
    total += abs(min(list1)-min(list2))
    list1.remove(min(list1))
    list2.remove(min(list2))
print(total)