import random
user_bingo = []
user_number = []
points = 0


def main():
    welcome()

    while True:
        print_menu()
        user_choice = input("Val: ")
        if user_choice == "1":
            user_guess = bingo()
            random_numbers = bingo_list()
            statistik(user_guess, random_numbers)
        elif user_choice == "2":
            view_statitics(user_bingo)
        elif user_choice == "0":
            break
        else:
            print("Du valde inte ett giltigt alternativ, försök igen")

    goodbye()

def view_statitics(user_bingo):
    print("*"*40)
    print("Statistik")
    print("*"*40)
    print("Spel 1: {} poäng".format(user_bingo))
    

def welcome():
    print("*"*40)
    print("Välkommen till Bingo!")
    print("*"*40)

def goodbye():
    print("*"*40)
    print("Tack för den här gången!")
    print("*"*40)

def print_menu():
    print("Menu:")
    print("1) Spela bingo!")
    print("2) Visa statistik")
    print("0) Avsluta")


def bingo():
    while True:  
        user_guess = input("Ange fem olika siffror [1-25] (avgränsa med ',') ").split(',')
        if not if_digit(user_guess):
            continue
        if not if_user_number(user_guess):
            continue
        if not user_count(user_guess):
            continue
        if not number_range(user_guess):
            continue
        break
    user_number.append(user_guess)
    return user_guess
        

def if_digit(user_guess):
    for guess in user_guess:
        if not guess.isdigit():
            print("Ange en siffra")
            return False
    return True
                  
def if_user_number(user_guess):
    for amount in user_guess:
        if len(user_guess) == 5:
            return True
        elif len(user_guess) > 5:
            print("Du måste ange 5 siffror avgränsa med ','")
            return False
        elif len(user_guess) < 5:
            print("Du måste ange 5 siffror avgränsa med ','")
            return False
        else:
            return False
    return True
        
def user_count(user_guess):
    for guess in user_guess:
        if user_guess.count(guess) == 1:
            return True
        else:
            print("Du kan inte ange samma tal 2 gånger!")
            return False
             
def number_range(user_guess):
    for guess in user_guess:
        if int(guess) < 1:
            print("du måste ange ett tal som är större än 0")
            return False
        elif int(guess) > 25:
            print("du måste ange ett tal som är mindre än 26")
            return False
    return True

def bingo_list():
    nested_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
    print("*"*20, "Dragning", "*"*20)
    random_numbers = random.sample(range(1,26),10)
    for i in nested_list:
        for number in i:
            if number in random_numbers:
                print("[{:^2}]".format(number), end="")
            else:
                print("{:^4}".format(number), end="")
        print()
    return random_numbers


def statistik(user_guess, random_numbers):
    global points
    for i in user_guess:
        if int(i) in random_numbers:
            points = points + 1 
        else:
            print()
    user_bingo.append(points)
    return user_bingo

main()



