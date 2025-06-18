import sys
if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1] 
    user_input = input("What was the parmeter? ")
    if user_input == param:
        print("Good jobl")
    else:
        print("Nonp, sorry...")    