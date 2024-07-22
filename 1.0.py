print("Welcome to my computer quiz!")

playing = input("Do you want to play my game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does the CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does the SSD stand for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " out of 5 questions correct!")
print("You got " + str((score / 5) * 100) + "%.")