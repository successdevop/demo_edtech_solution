age = 24
print("I am " + str(age) + " years old today")
print("I am {0} years today".format(age))
print()
print("There are {0} days in {1}, {2}, {3}, {4}, "
      "{5}, {6}, and {7}".format(31, "Jan", "Mar", "May", "jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, June: {1}, July: {2}, Aug: {1}, Sept: {1}, Oct: {2},"
      " Nov: {1} and Dec: {2}".format(28, 30, 31))
print()
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {1}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))

