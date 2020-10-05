while True:
    inp = input("Welcome to the equipment troubleshooter! Please answer all questions with 'y' or 'n'\nSo, first off, does it move?\n")
    inp = inp.lower()

    if inp == "y" or inp == "yes":
        inp2 = input("Should it?\n")
        inp2 = inp2.lower()
        if inp2 == "y" or inp2 == "yes":
            print("So there's no problem. Thank you for using the equipment troubleshooter. Goodbye.")
            quit()
        elif inp2 == "n" or inp2 == "no":
            print("Fix it with gaffer tape. Thank you for using the equipment troubleshooter. Goodbye.")
            quit()
        else:
            print("Sorry, I didn't understand you. Please only answer with 'y' or 'n'.\n")
        continue
    elif inp == "n" or inp == "no":
        inp3 = input("Should it?\n")
        inp3 = inp3.lower()
        if inp3 == "y" or inp3 == "yes":
            print("Fix it with WD40. Thank you for using the equipment troubleshooter. Goodbye")
            quit()
        elif inp3 == "n" or inp3 == "no":
            print("So there's no problem. Thank you for using the equipment troubleshooter. Goodbye")
            quit()
        else:
            print("Sorry, I didn't understand you. Please only answer with 'y' or 'n'.\n")
            continue
    else:
        print("Sorry, I didn't understand you. Please only answer with 'y' or 'n'.\n")
        continue
