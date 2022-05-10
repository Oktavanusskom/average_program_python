student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
n += 1

for student in student_heights:
  total += student
print(round(total/n))
