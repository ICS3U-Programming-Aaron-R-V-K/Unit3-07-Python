# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: March 31, 2025
# A dating program using OR logic gates with an if statements
# If the user is either handsome or rich, they can date the grandparents granddaughter


def main():
    # Initial explanation to the user
    print("\nRequirements to date our granddaughter")

    # Get user status, in wealth and handsomeness
    user_wealth = input("\nAre you rich(y/n): ")
    user_handsomeness = input("Are you handsome (y/n): ")

    # If not statements to validate the user input, either "y" or "no"
    if user_wealth != "y" and user_wealth != "n":
        print("\n{}, is not yes or no".format(user_wealth))

    if user_handsomeness != "y" and user_handsomeness != "n":
        print("\n{}, is not yes or no".format(user_handsomeness))

    # Decision making using OR logic
    # If statement if either of the answer is true
    if user_wealth == "y" or user_handsomeness == "y":
        print("You can date our granddaughter")

    # else statement if both of the answers are false or no
    else:
        print("You can not date our granddaughter")

if __name__ == "__main__":
    main()
