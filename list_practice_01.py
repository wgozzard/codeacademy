last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["physics", "calculus", "Poetry", "history"]

grades = [98, 97, 85, 88]

#use a list comprehension to combine two lists manually
gradebook = [[grades, subject] for (grades, subject) in zip(grades, subjects)]

#print(gradebook)

gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])
gradebook[-1][-1] = 98

gradebook[2].remove(85)
gradebook[2].append("Pass")

#combining two gradebooks 
full_gradebook = gradebook + last_semester_gradebook


print(full_gradebook)
