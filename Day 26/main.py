# numbers = [1, 2, 3, 4, 5]
# name = "Ismael"
# list Comprehension
# new_list = [n+1 for n in numbers]
# my_list = [letter for letter in name]
# print(my_list)
# Range
# num_list = [n*2 for n in range(1,5)]
# names = ["Alex", "Beth", "Caroline"]
# short_names = [name.upper() for name in names if len(name) < 5 ]
# print(short_names)

# Dictionary Comprehension
# import random
# names = ["Alex", "Beth", "Caroline"]
# student_scores = {student:random.randint(1,100) for student in names}
# passed_students = {student:score for (student,score) in student_scores.items() if score > 60}
# print(passed_students)

# Iteration of Dict
student_dict = { "student": ["Angela", "Ismaeel", "Lily"], "score": [56, 76, 98] }
# for (k,v) in student_dict.items():
#     print(k)
#     print(v)
# Iteration of Data Frame
import pandas as pd
df = pd.DataFrame(student_dict)
# for (k,v) in df.items():
#     print(k)
#     print(v)
for (index, row) in df.iterrows():
    # if row.student == "Ismaeel":
    print(row.student)