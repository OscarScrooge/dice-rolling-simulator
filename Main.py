from Dice import Dice

def main():

    dice = Dice(1,6)
    rolling = int(input("Do you want to roll de the dice?  1==\"YES\" 0==\"NO\" "))

    if rolling == 1:

        while rolling ==1:
            #dice.roll()
            print("\ndice says: " + str(dice.roll()))

            rolling =int(input("\nDo you want try again? 1==\"YES\" 0==\"NO\" "))

    else:

        print(":( Come back soon")


if __name__ == "__main__":
    main()

