from precription_data import patients

trial_patient = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

while trial_patient:
    patient = trial_patient.pop()
    prescription = patients[patient]
    print(patient, prescription, sep=": ")

print(trial_patient)