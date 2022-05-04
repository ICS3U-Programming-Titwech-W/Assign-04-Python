#!/usr/bin/env python3

# Created By: Titwech Wal
# Date: April.28. 2022
# Progam asks to input numbers then tells
# them how many postive numbers, negitive
# numbers, and zeros there are

from colorama import Fore


def main():
    postive_count = 0
    negative_count = 0
    zero_count = 0
    while True:
        # user Input
        user_input = input(Fore.YELLOW + "Enter any number('100'to quit): ")
        print("")
        try:
            user_num = int(user_input)
            # if user enter 100 exit loop
            if user_num != 100:
                # determain of user input is bigger than 0
                if user_num > 0:
                    # add to postive count
                    postive_count += 1
                elif user_num < 0:
                    # add to negitive count
                    negative_count += 1
                else:
                    # add to zero count
                    zero_count += 1
                print(Fore.WHITE + "Lets play again")
                print("")
            elif user_num == 100:
                break
        except Exception:
            # if inout is not an intger
            print(Fore.RED + "Invalid input")
            print("")
    # display your postive, negitive numbers and zeros entered
    print(Fore.GREEN + "You inputed {} postive numbers".format(postive_count))
    print("You inputed {} negative numbers".format(negative_count))
    print("You inputed {} zeros".format(zero_count))
    print("")
    print(Fore.WHITE + "Thank you for playing")


if __name__ == "__main__":
    main()
