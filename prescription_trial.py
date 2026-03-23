from precription_data import *

trial_patient = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

for patient in trial_patient:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin")
        print(f"Please remove {patient} from the trial")
    # print()
    print(patient, prescription)