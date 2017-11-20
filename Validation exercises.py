print("Do you work part-time or full-time.")
while True:
    PorF = input("Enter P or F.").lower()
    if PorF == 'p' or PorF == 'f':
        print("hello")
        break
    else:
        print("Please enter either P or F.")

print("Please choose a menu 1-5 or 0 to exit.")
while True:
    if input() in range(0,6):
        print("hello")
        break
    else:
        print("Please enter a value 0 to 5")

print("Please enter your hieght")
while True:
    if input() < 1.31 and input() > 0.75:
        print("hello")
        break
    else:
        print("Please anter a hieght between 0.75 to 1.3")
            
    
