<<<<<<< HEAD
secret = 10
guess = input("try guess the secret number betweeb 1 and 10: ")

if int(guess) > 10:
    print("I told you a number between 1 and 10")
elif int(guess) == secret:
    print("you are a magician")
else:
=======
secret = 10
guess = input("try guess the secret number betweeb 1 and 10: ")

if int(guess) > 10:
    print("I told you a number between 1 and 10")
elif int(guess) == secret:
    print("you are a magician")
else:
>>>>>>> 813ceef727a7071e78afcf6531bc2eeb82e5236e
    print("sorry your guess is wrong the right number is: " + str(secret))