medical_cause=input("Do you have a medical cause Y or N: ")
atten = int(input("What is the student's attendance: "))
if medical_cause=="Y":
    print("You are allowed to take the exam.")
else:
    if atten>=75:
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed to take the exam.")