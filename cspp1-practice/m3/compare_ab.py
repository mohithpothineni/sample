""" compare_AB """
VAR_A = input("Enter value for A: ")
VAR_B = input("Enter value for B: ")

if not(VAR_A.isnumeric() and VAR_B.isnumeric()):
    print("string involved")
elif int(VAR_A) > int(VAR_B):
    print("bigger")
elif int(VAR_A) < int(VAR_B):
    print("smaller")
else:
    print("equal")
