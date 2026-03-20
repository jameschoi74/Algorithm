import sys

n = int(sys.stdin.readline().strip())

people = []
for _ in range(n):
    people.append(list(sys.stdin.readline().strip().split()))

people.sort(key=lambda x: int(x[0]))

for person in people:
    print(person[0], person[1])