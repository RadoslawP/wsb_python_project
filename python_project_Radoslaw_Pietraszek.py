# copyright by Radoslaw_Pietraszek_(R4um) for the Python programming project at WSB Wroclaw

import csv
import random
import math


users = {"user1": "password1", }
diary = ""


def run_function(number):
    if number == 1:
        is_it_palindrome()
    elif number == 2:
        sign_up()
    elif number == 3:
        sign_in()
    elif number == 4:
        rock_paper_scisors()
    elif number == 5:
        count_vowels_in_word()
    elif number == 6:
        fibonacci_string_expression()
    elif number == 7:
        separating_digits_in_number()
    elif number == 8:
        beer_song()
    elif number == 9:
        surface_areas()
    elif number == 10:
        perimeter_of_figure()
    elif number == 11:
        game_of_dices()
    elif number == 12:
        write_diary()
    elif number == 13:
        read_diary()
    elif number == 14:
        update_diary()
    elif number == 15:
        shopping_list_write()
    elif number == 16:
        shopping_list_read()
    elif number == 17:
        shopping_list_update()
    elif number == 18:
        shopping_list_searching()
    elif number == 19:
        thought_about_number()
    elif number == 20:
        hello_n_times()
    elif number == 21:
        do_you_know_the_pi()
    elif number == 22:
        removing_punctuation_marks()
    elif number == 23:
        make_my_hacker_nick()
    elif number == 24:
        favourites_letter()
    elif number == 25:
        count_age()
    elif number == 26:
        knock_knock()
    elif number == 27:
        print_word_vertical()
    elif number == 28:
        print_sentence_vertical()
    elif number == 29:
        is_a_leap_year()
    elif number == 30:
        exit("Thank you for your attention.\n Bye! ;D")
    else:
        print("I don't udnerstand. Please, try again.")
        main()


def is_a_leap_year():
    year = int(input("Enter a year: "))
    if (year % 400 == 0) and (year % 100 == 0):
        print(year, " is a leap year.")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(year, " is a leap year.")
    else:
        print(year, " is not a leap year.")


def print_sentence_vertical():
    sentence = input("Enter a sentence: ")
    for word in sentence.split():
        print(word)
    main()


def print_word_vertical():
    word = input("Enter a word: ")
    for letter in word:
        print(letter)
    main()


def knock_knock():
    print("Knock, knock!\n")
    whois = input()
    while whois != "Who's there?":
        print("Do not break the joke!\n")
        print("Knock, knock!\n")
        whois = input()
    else:
        print("Boo!")
        who = input()
        while who != "Boo Who?":
            print("Try again!")
            print("Boo!")
            who = input()
        else:
            print("Do't cry. It's only a joke! XD")
    main()


def count_age():
    year = int(input("What year is today? "))
    birthday = int(input("In which year you were born? "))
    age = year - birthday
    print("You are ", age, "years old.")
    main()


def favourites_letter():
    word = input("Enter your word: ")
    length = len(word)
    number = int(input("Enter your favourite number lower than word: "))
    start = length - number
    end = 2 * start
    favourite_letters = (word[start:end])
    print("Your favourite letters are: ", favourite_letters)
    main()


def make_my_hacker_nick():
    hacker_letters = {"a": "4", "A": "4", "b": "8", "B": "8", "e": "3", "E": "3", "g": "6", "G": "6", "i": "1",
                      "I": "1", "o": "0", "O": "0", "s": "5", "S": "5", "z": "2", "Z": "2"}
    nick = input("Please, enter your name: ")
    hacker_nick = ""
    for letter in nick:
        if letter in hacker_letters:
            hacker_nick = hacker_nick + hacker_letters[letter]
        else:
            hacker_nick = hacker_nick + letter
    print("Your hacker nick will be: ", hacker_nick)
    main()


def removing_punctuation_marks():
    characters = ",. !@#$%^&*()_+=-][}{;:'<>?/|"
    sentence = input("Plecase, enter a sentence:\n")
    for i in sentence.lower():
        if i in characters:
            sentence = sentence.replace(i, "")
    print(sentence)
    return sentence


def do_you_know_the_pi():
    user_pi = str(input("Please, tell mi, How well do you know the pi number? "))

    def removing_punctuation_marks(sentence):
        characters = ",. !@#$%^&*()_+=-][}{;:'<>?/|"
        for i in sentence.lower():
            if i in characters:
                sentence = sentence.replace(i, "")
        return sentence

    user_pi_len = len(removing_punctuation_marks(user_pi))
    pi = round(math.pi, user_pi_len - 1)

    print(type(float(user_pi)))
    print(user_pi_len)
    print(type(pi))

    if pi == float(user_pi):
        print("Congratulation, you know the pi number to ", user_pi_len - 1, " decimal places.")
        print("Your pi: ", user_pi, " | The pi number: ", pi)
    else:
        print("Unfortunately wrocg.")
        print("Your pi: ", user_pi, " | The pi number: ", pi)
    main()


def hello_n_times():
    decision = "y"
    while decision == "y":
        name = input("What is your name? ")
        n = int(input("Tell me, how many times tell you Hello? "))
        for i in range(n):
            print("Hello ", name, "! ;D")

        decision = input("Do you want to try again? y/n ")
    print("Ok, it was nice to play with you. Bye ;)")
    main()


def thought_about_number():
    decision = "y"
    while decision != "n":
        computer_number = random.randint(0, 100) + 1
        print(computer_number)
        count = 0
        print(count)
        print("Hello user. Let's play a game.\n"
              "I thought about number. Can you guess what number it is?\n")
        user_number = 0
        while user_number != computer_number:
            count += 1
            user_number = int(input("Tell me: "))
            if user_number > computer_number:
                print("Oh, no, it's too high.")
            elif user_number < computer_number:
                print("Oh, no, it's to low")
        print("Great job! My number is equal to: ", computer_number)
        print("You did it in ", count, " try.")
        decision = input("Do you want to play again? y/n ")
    print("Ok, it was nice to play with you. Bye ;)")
    main()


def decision_shoppig_list():
    decision = input("Do you want to read your shopping list? y/n ")
    if decision == "y":
        shopping_list_read()
    elif decision == "n":
        print("Oh, ok, that is no problem. You can do it later. Bye")
        main()
    else:
        print("Not expected answer. Please, try again.")
        decision_shoppig_list()


def shopping_list_searching():
    file = open("My shopping list.csv", "r")
    search = input("Tell me, what do you looking for? ")
    reader = csv.reader(file)
    for row in file:
        if search in str(row):
            print(row)
    file.close()
    decision_shoppig_list()


def shopping_list_update():
    file = open("My shopping list.csv", "a")
    adding = "y"
    while adding == "y":
        what = str(input("Please, tell me what do you want to buy? "))
        amount = str(input("How much do you want to buy it? "))
        excepted_price = str(input("How much should it cost? "))
        checked = input("Did you buy it? V/- ")
        new_record = what + "," + amount + "," + excepted_price + "," + checked + "\n"
        file.write(str(new_record))
        adding = input("Do you want to buy something else? y/n ")
    else:
        print("Ok, no problem. If you want, you can read now your shopping lis.")

    file.close()
    decision_shoppig_list()


def shopping_list_read():
    file = open("My shopping list.csv", "r")
    print("Here is your shopping list. Please, check is it all what do you need:\n")
    for row in file:
        print(row)
    file.close()

    def decision():
        dec = input("Do you want to update your shopping list? y/n ")
        if dec == "y":
            shopping_list_update()
        elif dec == "n":
            print("Oh, ok, that is no problem. You can do it later. Bye")
            main()
        else:
            print("Not expected answer. Please, try again.")
            decision()
    decision()


def shopping_list_write():
    print("Hello user. Welcome in your shopping lis creator. In a moment I will ask you for some details.")
    file = open("My shopping list.csv", "w")
    file.write("My shopping list:\n")
    file.close()
    shopping_list_update()


def update_diary():
    file = open(diary, "a")
    file.write("\n")
    text = input("Ok, so now, You can add something.\n"
                 "If you want to stop, write the: 'The end.'\nStart here:    ")
    while text != "The end.":
        file.write("\n")
        file.write(text)
        file.write("\n")
        text = input()
    file.close()
    read_diary.read_something()


def read_diary():
    name = input("Please, enter your name honey: ")
    print("Oh, great. Let me begin again... ;) ")
    print("Hello dear ", name, " I am so glaad to see you. ^^")

    def adding_question(diary):
        adding_question = input("So, what do you think? Do you want, add something? y/n ")
        if adding_question == "y":
            update_diary(diary)
        elif adding_question == "n":
            print("Oh, ok, that is no problem. You can do it later.")
            read_something()
        else:
            print("Not expected answer. Please, try again.")
            adding_question(diary)

    def read():
        date = input("Please, enter date which you want to read: ")
        diary = "Diary day " + date + ".txt"
        file = open(diary, "r")
        print(file.read())
        print("\n")
        adding_question(diary)

    def read_something():
        read_question = input("Do you want read smoething interesting? y/n ")
        if read_question == "y":
            read()
        elif read_question == "n":
            print("Oh, ok, that is no problem. You can do it later. Bye")
            main()
        else:
            print("Not expected answer. Please, try again.")
            adding_question()

    read_something()


def write_diary():
    name = input("Please, enter your name honey: ")
    print("Oh, great. Let me begin again... ;) ")
    print("Hello dear ", name, " I am so glaad to see you. ^^")
    date = input("Please, enter today's date: ")

    diary = "Diary day " + date + ".txt"
    file = open(diary, "w")
    file.write("My dear diary...\n")
    print("Oh, today is ", date)

    text = input(
        "Ok, so now, please, tell me about your day.\nIf you wnt to stop, write the: 'The end.'\nStart here:    ")
    while text != "The end.":
        file.write("\n")
        file.write(text)
        file.write("\n")
        text = input()

    file.close()

    def decision():
        decision = input("Do you want to read your diary? y/n")
        if decision == "y":
            read_diary()
        elif decision == "n":
            print("Oh, ok, that is no problem. You can do it later. Bye")
            main()
        else:
            print("Not expected answer. Please, try again.")
            decision()

    decision()


def game_of_dices():
    winner = ""
    computer_dices = {}
    user_dices = {}

    for i in range(1, 6):
        result = random.randint(1, 6)
        computer_dices[i] = result
    print("The computer throws: ", computer_dices)

    def throw_d():
        throw = input("Please, throw the dices! (d)")
        if throw == "d":
            for i in range(1, 6):
                result = random.randint(1, 6)
                user_dices[i] = result
        else:
            print("No, you should throw the D-ices! (d)")
            throw_d()

    throw_d()

    for key, value in computer_dices.items():
        print(key, "Computer: ", value, " | User: ", user_dices[key])

    user_score = sum(user_dices.values())
    computer_score = sum(computer_dices.values())

    if user_score == computer_score:
        winner = 'Draw'
    elif user_score > computer_score:
        winner = 'User'
    elif user_score < computer_score:
        winner = 'Computer'

    if winner == 'Draw':
        print('Hurray, we win together. Our score is equal to: ', user_score)

    else:
        print('The winner is ', winner, "! | Your score: ", user_score, " | Computer score: ", computer_score)
    main()


def perimeter_of_figure():
    pi = round(math.pi, 2)
    first = float(input("Please, enter the length of first side: "))
    second = float(input("Please, entner a length of second side: "))
    third = float(input("Please, entner a length of third side: "))

    square = 4 * first
    second_square = 4 * second
    third_square = 4 * third
    rectangle = 2 * (first + second)
    triangle = first + second + third
    first_circle = 2 * pi * first
    second_circle = 2 * pi * second
    third_circle = 2 * pi * third

    print("With your length or hight, the perimeter of figures are equal to:")
    print("square: ", square, " or ", second_square, " with second dimension segment, or ", third_square,
          "with third dimension segment.")
    print("rectangle: ", rectangle)
    print("triangle: ", triangle)
    print("circle: ", first_circle, " with pi rounded to two decimal places equal to: ", pi)
    print(" or ", second_circle, " with second dimension segment.")
    print(" or ", third_circle, " with third dimension segment.")
    main()


def surface_areas():
    pi = round(math.pi, 2)
    length = float(input("Please, enter the length of segment: "))
    height = float(input("Please, entner a length of another dimension: "))

    square = math.pow(length, 2)
    second_square = math.pow(height, 2)
    rectangle = length * height
    triangle = (length * height)/2
    circle = pi * (length ** 2)
    second_circle = pi * (height ** 2)

    print("With your length or hight, the surface areas of the figures are equal to:")
    print("square: ", square, " or ", second_square, " with second dimension segment.")
    print("rectangle: ", rectangle)
    print("triangle: ", triangle)
    print("circle: ", circle, " with pi rounded to two decimal places equal to: ", pi)
    print(" or ", second_circle, " with second dimension segment.")
    main()


def beer_song():
    word = 'butelki'
    word2 = 'butelek'
    digits_ek = (0, 1, 5, 6, 7, 8, 9)
    digits_ki = (2, 3, 4)

    def digits_in_number(number):
        digits = []
        while number > 0:
            digits.insert(-1, number % 10)
            number //= 10
        return digits[-1]

    for beer_num in range(99, 0, -1):
        if beer_num == 1:
            print('Ostatnia butelka piwa na ścianie.')
            print(beer_num, 'butelka piwa na ścianie.')
            print('Jedną weź.')
            print('Podaj w koło.')
            print('Chlup, ach jak wesoło!')
        elif digits_in_number(beer_num) in digits_ek:
            print(beer_num, word2, 'piwa na ścianie.')
            print(beer_num, word2, 'piwa.')
            print('Jedną weź.')
            print('Podaj w koło.')
            print('Chlup, ach jak wesoło!')
        elif digits_in_number(beer_num) in digits_ki:
            print(beer_num, word, 'piwa na ścianie.')
            print(beer_num, word, 'piwa.')
            print('Jedną weź.')
            print('Podaj w koło.')
            print('Chlup, ach jak wesoło!')
        else:
            new_num = beer_num - 1
            if new_num == 1:
                word = 'buteleka'
                print(new_num, word, 'piwa na ścianie')
    main()


def separating_digits_in_number():
    digits = []
    number = int(input("Please, enter a number: "))
    while number > 0:
        digits.insert(-1, number % 10)
        number //= 10
    return print("Your digits in number are: ", digits)
    main()


def fibonacci_string_expression():
    choice = int(input("Please, tell me. Which fibonacci string expression do you want to count? "))

    def fibonacci(number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return fibonacci(number-1) + fibonacci(number-2)

    result = fibonacci(choice)
    print("Your fibonacci string expression is ", result)
    print("Thanks ;)")
    main()


def count_vowels_in_word():
    number = 0
    vowels = "aąeęiouy"
    word = input("Please, enter the word. I will count how many vowels is in the word: ").lower()

    for character in word:
        if character in vowels:
            number += 1
    return print("In your word is ", number, " vowels.")
    main()


def rock_paper_scisors():
    computer_choice = random.choice(("rock", "paper", "scisors"))

    def decision():
        decision = str(input('Do you want to play again? y/n'))
        if decision == "y":
            rock_paper_scisors()
        elif decision == "n":
            main()
        else:
            print("Oh, i do not understand.")
            decision()

    user_choice = ''
    while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scisors':
        user_choice = input('Rock, paper, scisors? ')

    print("Your choice " + user_choice + " and computers choice " + computer_choice + " !")

    if computer_choice == user_choice:
        winner = 'Draw'
    elif computer_choice == 'paper' and user_choice == 'rock':
        winner = 'Computer'
    elif computer_choice == 'rock' and user_choice == 'scisors':
        winner = 'Computer'
    elif computer_choice == 'scisors' and user_choice == 'paper':
        winner = 'Computer'
    else:
        winner = 'User'

    if winner == 'Draw':
        print('Hurray, we win together.', computer_choice, 'You can play again. ;)')
        decision()
    else:
        print('The winner is ', winner)
        decision()
    main()


def sign_in():

    def check_password():
        user_name = input("Please, enter your user name: ")
        user_password = input("Please, enter now your password: ")

        while user_name in users.keys():
            password = users[user_name]
            if password == user_password:
                print("Great job! Welcome in!")
                break
            else:
                print("Oh no, something goes wrong.\n Please, try again.")
                check_password()
                break
        else:
            print("Oh no, something goes wrong.\n Please, try again.")
            check_password()

    print("You chose: Sign ip function. Let's try this one.")
    print("Welcome! It is so nice that you want to sign ip here!")
    check_password()
    main()


def sign_up():
    print("You chose: Sign up function. Let's try this one.")
    print("Welcome! It is so nice that you want to sign up here!")

    user_name = input("Please, enter your user name: ")
    user_password = input("Please, enter now your password: ")
    users[user_name] = user_password

    choice = input("Great! Do you want to sign in now? y/n ")
    if choice == "y":
        sign_in()
    elif choice == "n":
        print("Ok, it was nice to met you, thanks for colaborate.")
    else:
        choice = input("Oh, sorry. It is wrong choice.\n Please, try again.\nGreat! Do you want to sign in now? y/n ")
    main()


def is_it_palindrome():
    print("You chose: Is it palindrome function. Let's try this one.")
    choice = "y"
    while choice == "y":
        word = list(input("Please, enter the word for me: ").lower())
        reversed_word = []

        for i in range(len(word)):
            reversed_word.append(word[-i-1])

        if word == reversed_word:
            print("Yes, your entered word is a palindrome! Look:\n", word, " == ", reversed_word)
        else:
            print("No, unfortunately your word is not a palindrome. Look:\n", word, " != ", reversed_word)

        choice = input("Do you want to try again? y/n ")
    else:
        choice = input("Unfortunately it is unexpected choice. Please, try again.\nDo you want to try again? y/n ")
    main()


def main():
    menus_dictionary = {1: "Is_it_palindrome()", 2: "Sign up()", 3: "Sign in()", 4: "Rock paper scisors game()",
                        5: "count_vowels_in_word()", 6: "fibonacci_string_expression()",
                        7: "separating_digits_in_number()", 8: "beer_song()", 9: "surface_areas()",
                        10: "perimeter_of_figure()", 11: "game_of_dices()", 12: "write_diary()", 13: "read_diary()",
                        14: "update_diary()", 15: "shopping_list_write()", 16: "shopping_list_read()",
                        17: "shopping_list_update()", 18: "shopping_list_searching()", 19: "thought_about_number()",
                        20: "hello_n_times()", 21: "do_you_know_the_pi()", 22: "removing_punctuation_marks()",
                        23: "make_my_hacker_nick()", 24: "favourites_letter()", 25: "count_age()", 26: "knock_knock()",
                        27: "print_word_vertical()", 28: "print_sentence_vertical()", 29: "is_a_leap_year()",
                        30: "Exit"}
    print("\n----------------------------------------------------------------------------------")
    print("\nWelcome in my programming in Python project!")
    for key, value in menus_dictionary.items():
        print(key, ": ", value)
    choice = int(input("Which function do you want to join?\nPlease, enter your choice: "))
    run_function(choice)


if __name__ == '__main__':
    main()


# copyright by Radoslaw_Pietraszek_(R4um) for the Python programming project at WSB Wroclaw
