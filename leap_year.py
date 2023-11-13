#!/usr/bin/env python3
# Created By: Ishami Sebgoya
# Date: November 12, 2023


def main():
    try:
        year = int(input("Enter a year: "))

        if year < 0:
            print("Invalid input: Year must be a positive integer.")
        else:
            is_leap_year(year)
    except ValueError:
        print("Invalid input: Please enter a valid integer for the year.")


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()
