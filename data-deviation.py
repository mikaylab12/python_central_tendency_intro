import matplotlib.pyplot as plt
import numpy as np
# marks and names of students
student_marks = [70, 45, 90, 12]
student_names = ["Memphis", "Godwin", "Thando", "Thabo"]
# converting lists to arrays
my_student_marks = np.array([70,45,90,12])
my_student_names = np.array(["Memphis", "Godwin", "Thando","Thabo"])
# creating bar graph
plt.bar(my_student_names, my_student_marks)
# bar graph title
plt.title("The marks of my students")
plt.show()