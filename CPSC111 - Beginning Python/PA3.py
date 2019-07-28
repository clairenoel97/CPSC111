#assignment 3
'''
Write a quiz program.
the quiz program will quiz the user on a topic of your choosing

your quiz must contain 10 questions. these questions include at least 2 of each of the following different types of questions:
    1. multiple choice
    2. numeric responses
    3. true or false (convert the string into an int and then a bool)

additional requirements
    1. for each question
        a. define a function. the function should return 1 or 0
        b. explicitly tell the user the format in which they should enter their response
        3. number each question
        4. always tell the user if they answer correctly or incorrectly
            use else - if for this
    2. define main that drives the program
        counts the number of correct answers
    3. at the end, make a cute remark on how big a fan they are
'''

def display_welcome():
    print("Welcome to the I Love Music 2019 Quiz!")

def multiple_choice_1():
    answer = str(input("1) Who sings the hit pop song 'Truth Hurts'? Please enter a character a-e.\n"
    "a) Camila Cabello\nb) Billie Eilish\nc) Miley Cyrus\nd) Lizzo\ne) Beyonce\n"))
    if answer == 'd':
        print("Congrats! You got it!")
        return 1
    else:
        print("Sorry, you got it wrong. The answer is d) Lizzo")
        return 0

def numeric_response_2():
    answer = int(input("2) The Jonas Brothers just released a new album called 'Happiness Begins'. How many songs are on the album? Please enter an integer\n"))
    if answer == 14:
        print("Wow, you got it! You really know your trivia.")
        return 1
    else:
        print("Sorry, you got it wrong. The answer is 1995.")
        return 0

def boolean_3():
    answer = int(input("3) Taylor Swift released a single called 'You Need to Calm Down'. Did she include any easter eggs in the music video? Please enter 1 for True or 0 for False.\n"))
    boolean_answer = bool(answer)
    if boolean_answer == True:
        print("You're right! She even put some in her interview with Ellen Degeneres")
        return 1
    else:
        print("Actually, she did! Sorry, you got it wrong.")
        return 0

def multiple_choice_4():
    answer = str(input("4) Which Scottish singer-songwriter had a 2019 hit with 'Someone You Loved'? Please enter a character a-c.\n" +
    "a) Calvin Harris\nb)Lewis Capaldi\nc)Paolo Nutini\n"))

    if answer == 'b':
        print("That's right! It's a beautiful love song.")
        return 1
    else:
        print("Better luck next time.")
        return 0

def numeric_response_5():
    answer = int(input("5) In what year was Sam Smith's song 'How Do You Sleep?' released. Please enter an integer.\n"))
    if answer == 2019:
        print("Correct! I guess the title of the quiz gave it away.")
        return 1
    else:
        print("Oops, that's wrong. Next time, look at the title of the quiz for a hint.")
        return 0

def boolean_6():
    answer = int(input("6) Does the hit singer-songwriter Billie Eilish have a crush on singer Justin Bieber? Please enter 1 for True or 0 or False.\n"))
    boolean_answer = bool(answer)
    if boolean_answer == True:
        print("Yep! I mean, he is good looking :)")
        return 1
    else:
        print("Actually, she does! She has admitted it many times")
        return 0

def multiple_choice_7():
    answer = str(input("7) If I were to take my horse to the old town road, what would I do? Please enter a character a-c.\na) ride til I can't no more\nb) go on a trail ride\nc) sell it for money\n"))
    if answer == 'a':
        print("You got it!")
        return 1
    else:
        print("Sorry, that's wrong")
        return 0

def numeric_response_8():
    answer = str(input("8) Which British group featuring Ton Fletcher, Danny Jones, Dougie Poynter and Harry Judd reformed in 2019? Please enter a name.\n"))
    if answer == 'McFly':
        print("How did you know!?")
        return 1
    else:
        print("Nope, better luck next time.")
        return 0

def boolean_9():
    answer = int(input("9) Is it true that Shawn Mendes and Camilla Cabello are dating? Please enter 1 for True or 0 for False.\n"))
    boolean_answer = bool(answer)
    if boolean_answer == True:
        print("Yes")
        return 1
    else:
        print("No")
        return 0

def multiple_choice_10():
    answer = str(input("10) Sophie Turner appeared in the video of which Jonas Brothers single? Please enter a-c.\na) Sucker\nb) Pom Poms\nc) Cool\n"))
    if answer == 'a':
        print("That's correct!")
        return 1
    else:
        print("Sorry, better luck next time!")
        return 0

def main():
    questions_correct = 0
    if(multiple_choice_1()):
        questions_correct += 1
    if(numeric_response_2()):
        questions_correct += 1
    if(boolean_3()):
        questions_correct += 1
    if(multiple_choice_4()):
        questions_correct += 1
    if(numeric_response_5()):
        questions_correct += 1
    if(boolean_6()):
        questions_correct += 1
    if(multiple_choice_7()):
        questions_correct += 1
    if(numeric_response_8()):
        questions_correct += 1
    if(boolean_9()):
        questions_correct += 1
    if(multiple_choice_10()):
        questions_correct += 1

    if questions_correct <= 3:
        print("You scored %d questions correctly. I guess you don't listen to much music." %(questions_correct))
    elif questions_correct > 3 and questions_correct <= 7:
        print("You scored %d questions correctly. Nice, I can see you like music." %(questions_correct))
    else:
        print("You scored %d questions correctly. Wow, you are a music master!" %(questions_correct))

main()
