def main():
    print(checkLeapYear)

def checkLeapYear():
    userInput = input("Enter a year: ")
    isLeapMsg = "is a leap year."
    notLeapMsg = "is not a leap year."

    userInt = int(userInput)
    if userInt % 4 == 0:
        if userInt % 400 == 0:
            print(userInt, isLeapMsg)
        else:
            if userInt % 100 == 0:
                print(userInt, notLeapMsg)
            else:
                print(userInt, isLeapMsg)

    else:
        print(userInt, notLeapMsg)


if __name__ == "__main__":
    main()
