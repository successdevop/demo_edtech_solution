# morning = {"Java", "C", "Ruby", "Lisp", "C#"}
# afternoon = {"Python", "C#", "Java", "C", "Ruby"}

morning = ["Java", "C", "Ruby", "Lisp", "C#"]
afternoon = ["Python", "C#", "Java", "C", "Ruby"]

# possible_courses = morning.symmetric_difference(afternoon)
# possible_courses = set(morning) ^ set(afternoon)
possible_courses = set(morning).symmetric_difference(afternoon)

print(possible_courses)