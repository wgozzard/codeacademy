#PRACTICE WITH LOOPS

promise = "I will finish the python loops module!"

#Will print promise data 5x
for temp in range(5):
  print(promise)
  
#****WHILE LOOP Walkthrough****
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Your code below: 
countdown = 10 
while countdown >= 0: print(countdown); countdown-=1 
print("We have liftoff!")

#*****WHILE LOOPS USING RANGE & LEN*****
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0 

while index < length:
  print("I am learning about %s" % python_topics[index])
  index +=1
  
#****USING A LOOP BREAK*****
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]

dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
#When the program hits a break statement it immediately terminates a loop. From where the condition is met. i.e. shihtzu, poodle, and collie are not printed out.

#*****USING A CONTINUE STATEMENT****
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

#All the ages less then 21 will be skipped and not printed due to the continue condition
for age in ages:
  if age < 21:
    continue
  else:
    print(age)
    
 #******NESTED LOOPS*****
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
    
print(scoops_sold) #print out the cummulative of sale data

#***LIST COMPREHENSION USING CONDITIONALS****
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [num for num in heights if num > 161]

print(can_ride_coaster)

#****EXAMPLE OF HOW LIST COMPREHENSION CAN SIMPLIFY CODE****

#create a list 1 - 9
single_digits = range(0, 10)

#Create empty list to append square numbers
squares = []

#loop and append
for num in single_digits:
  squares.append(num**2)
print(squares)

#Or you could do the above code in one line using a list comprehension
cubes = [n**3 for n in range(1, 9)]
print(cubes)
