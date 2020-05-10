last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects =["physics","calculus","poetry","history"]
grades =[98,97,85,88]
grade=zip(subjects,grades)
#Add More Subjects:
subjects.append ("computer science")
grades.append (100) 

gradebook=list(grade)
print(gradebook)

gradebook.append(["visual arts", 93])
#One Big Gradebook!

full_gradebook =last_semester_gradebook+gradebook 
print(full_gradebook)