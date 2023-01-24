# list = []

# def func(l):
#     l.append(1)
#     l.append(2)
#     l.append(3)


# y = 7
# def func2():
#     global y
#     y += 1


# func(list)
# func2()

# print(list)
# print(y)

# # from numpy import random

# # print(random.randint(2))

for i in range(3):
    print(i)

print(i)

from datetime import datetime
dt = datetime.now()
print(dt)

# # Record new score
# with open("./resources/high_scores_hard.csv", 'a') as file:
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writerow({'NAME': name, 'LEVELS WON': score, 'TIMESTAMP': timestamp})