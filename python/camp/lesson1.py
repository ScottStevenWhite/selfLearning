maxNumber = 100
minNumber = 1

secret = input("Enter a number between " + str(minNumber)
               + " and " + str(maxNumber) + " and I will guess it! ")
secret = int(secret)
#harry is the best student = False


guess = int((maxNumber + minNumber) / 2)

while secret != guess:
    if guess < secret:
        print("Your number is greater than " + str(guess) + ".")
        minNumber = guess + 1

    elif guess > secret:
        print("Your number is less than " + str(guess) + ".")
        maxNumber = guess - 1

    guess = int((maxNumber + minNumber) / 2)


print("Your number is " + str(guess) + "!!! Haha, I am smart.")

    
