course = "Python Programming"

print(course.upper())
# PYTHON PROGRAMMING
print(course.lower())
# python programming
print(course.title())
# Python Programming
print(course.strip())
# removes wides space
print(course.lstrip())
# removes wides space from left
print(course.rstrip())
# removes wides space from right
print(course.find("o"))
# return the index of the argument
new_course = (course.replace("p","c"))
print(new_course)
# removes the first character and adds the second in place