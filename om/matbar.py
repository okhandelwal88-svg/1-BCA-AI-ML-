import matplotlib.pyplot as plt
students=["alice","bob","charlie","om"]
marks=[67,89,34,100]
plt.bar(students,marks,color="blue")
plt.title("student marks")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()