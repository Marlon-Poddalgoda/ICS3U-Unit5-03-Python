#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on January 2021
# This program converts a grade level into a percentage


def grade_level(grade):
    # This function converts a grade level into a percentage

    # process
    if grade == "4+":
        grade_percent = 97
        # output
        return grade_percent
    elif grade == "4":
        grade_percent = 90
        # output
        return grade_percent
    elif grade == "4-":
        grade_percent = 83
        # output
        return grade_percent
    elif grade == "3+":
        grade_percent = 78
        # output
        return grade_percent
    elif grade == "3":
        grade_percent = 75
        # output
        return grade_percent
    elif grade == "3-":
        grade_percent = 71
        # output
        return grade_percent
    elif grade == "2+":
        grade_percent = 68
        # output
        return grade_percent
    elif grade == "2":
        grade_percent = 65
        # output
        return grade_percent
    elif grade == "2-":
        grade_percent = 61
        # output
        return grade_percent
    elif grade == "1+":
        grade_percent = 58
        # output
        return grade_percent
    elif grade == "1":
        grade_percent = 55
        # output
        return grade_percent
    elif grade == "1-":
        grade_percent = 51
        # output
        return grade_percent
    elif grade == "R" or grade == "r":
        grade_percent = 25
        # output
        return grade_percent
    else:
        grade_percent = -1
        return grade_percent


def main():
    # this function receives input
    print("This program converts a grade level into a percentage.")

    # input
    grade_input = input("Enter a grade level (ex: 4+): ")
    print("")

    # call functions
    grade_percentage = grade_level(grade_input)

    # output of percentage
    if grade_percentage == -1:
        print("'{}' is not a valid level, try again."
              .format(grade_input))
    else:
        print("Level {0} is equal to an average of {1}%."
              .format(grade_input, grade_percentage))


if __name__ == "__main__":
    main()
