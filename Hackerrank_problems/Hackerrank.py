# List comprehension:
# I have to generate a list of all possible coordinates on a 3D grid where the sum of Xi + Yi + Zi is not equal to N. If X=2, the possible values of Xi can be 0, 1 and 2. The same applies to Y and Z.

x = 1
y = 1
z = 1
n = 2

new_list = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                b = i,j,k
                c = list(b)
                new_list.append(c)
# print(new_list)

li = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i+j+k != n ]
print(li)


#Get the second highest number in the list
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The first line contains . The second line contains an array   of  integers each separated by a space.
#
# Constraints
#
# Output Format
#
# Print the runner-up score.
#
# Sample Input 0
#
# 5
# 2 3 6 6 5

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())  list the o/p of map and use the below code

n = 5
arr = [2, 3, 6, 6, 5]

new_list = set(arr)
# print(new_list)
new_list.remove(max(new_list))
# print(new_list)
print(max(new_list))


# Nested List : Print the names with the second lowest grade
# Input: {5
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21
# }

# no_of_students = int(input())
# records = []
# scores = []
# for i in range(no_of_students):
#     name = input()
#     score = float(input())
#     records.append([name, score])
#     print(records)
#     scores.append(score)
# b = sorted(set(scores))
# b.remove(min(b))
# low = min(b)
# print(low)
# second_lowest_students = [name for name,score in records if score== low]
# second_lowest_students.sort()
# for name in second_lowest_students:
#     print(name)


'Prob'
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
#
# Example
#
#
#
#
# The query_name is 'beta'. beta's average score is .
#
# Input Format
#
# The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
#
# Constraints
#
# Output Format
#
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#
# Sample Input 0
#
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0
#
# 56.00




if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map((float), line))
        length = len(scores)
        student_marks[name] = sum(scores)/length
        print(student_marks[name])

    query_name = input('Pick one among the three '
                       '1. Krishna 2. Arjun 3. Malika: ')
    print("{:.2f}".format(student_marks[query_name]))



