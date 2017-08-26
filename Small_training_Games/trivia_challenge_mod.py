# Trivia Challenge
# Trivia game that reads a plain text file

import sys, pickle

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    value = next_line(the_file)
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file) 

    return category, value, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def choose_option(options, options_pool):
    #Check correctness of choosed options
    print(options)
    choice = input ("Your choice: ")
    while choice not in options_pool :
        if choice != None :
            print("This option does not exist\n")
            choice = input ("Your choice: ")
    print()
    return choice

def record_table(table, score):
    """"It operates with table of game record, 
        can add, change, delete, search, show table's content"""

    OPTIONS = ("""
    Input appropriate number of action:
    0\tExit from record table
    1\tAdd new record
    2\tChange record
    3\tDelete record
    4\tSearch record
    5\tShow all records\n """)
    OPTIONS_POOL = ('0','1','2','3','4','5')

    choice = None
    while choice != '0':
        #Check existence of choice
        choice = choose_option (OPTIONS, OPTIONS_POOL)
        
        men = table.keys()
        #Exit from record table
        if choice == "0":
            print("Goodbye")

        #Add new record
        elif choice == "1":
            add_name = input("\nInput gamer's name, example - 'Peter Pen' ")
            if add_name not in men :
                add_score = input("\nInput gamer's score \nor press Enter to skip action: ")
                table[add_name] = add_score
                print("\nRecord added to the game record table")
            else :
                print("\nSuch name is already exist")
        
        #Change record
        elif choice == "2":
            add_name = input("\nInput gamer's name, which record you want to change: ")
            if add_name in men :
                add_score = input("\nInput gamer's score, \nor press Enter to retain current score: ")
                if add_score != '':
                    table[add_name] = add_score
                print("\nRecord was changed")
            else :
                print("\nThere is not such name in the record table")
        
        #Delete record
        elif choice == "3":
            add_name = input("\nInput gamer's name, which record you want to delete: ")
            if add_name in men :
                del table[add_name] 
                print("\nRecord was deleted")
            else :
                print("\nThere is not such name in the record table")
        
        #Search record
        elif choice == "4":
            add_name = input("\nInput gamer's name, which score you want to see : ")
            if add_name in men :
                print("Gamer: ", add_name,"\nScore: ", table[add_name],"\n\n")
            else :
                print("\nThere is not such name in the record table")
        
        #Show all records
        elif choice == "5":
            all_names_sort = sorted(table.keys())
            print()
            for add_name in all_names_sort :
                print("Gamer:  ", add_name,"\nScore:  ", table[add_name])
                print()

    return table

def save_record(table):
    '''save record table in various data format (txt, dat)'''

    OPTIONS = (""" 
    Please choose number which form you want to save record table
    or press Enter to save in default .txt file:
    
    0. Exit without saving (Warning! all unsaved data will be lost)
    1. Save in conserve record_trivia_file.dat file with module pickle
    2. Save in usual record_trivia_file.txt file (default) """)
    OPTIONS_POOL = ('0', '1', '2','')
    choice = choose_option(OPTIONS, OPTIONS_POOL)

    if choice == '0':
        print("Exit without saving any change in table record")

    # save game's record dictionary .txt with 2 line on one record
    elif choice == '' or choice == '2':
        record_file = open('record_trivia_file.txt', 'w', encoding ='utf-8')
        for add_name in table.keys():
            line_uneven = add_name + '\n'
            line_even = table[add_name]+'\n'
            record_file.write(line_uneven)
            record_file.write(line_even)
        record_file.close()
        print("Data was saved in record_trivia_file.txt")

    # save game's record dictionary .dat with pickle
    elif choice == '1':
        record_file = open('record_trivia_file.dat', 'wb')
        pickle.dump(table, record_file)
        record_file.close()
        print("Data was saved in record_trivia_file.dat")

def read_record():
    '''extract game's record dictionary with pickle or read from .txt file'''

    OPTIONS = (""" 
    Please choose number which file with a record table you want to load
    or press Enter to read default .txt file:
    
    0. Exit without reading (Warning! you can rewrite existing game's record on stage "save record" and lose all data)
    1. Read from conserve record_trivia_file.dat file with module pickle
    2. Read in usual record_trivia_file.txt file (default) """)
    OPTIONS_POOL = ('0', '1', '2','')
    choice = choose_option(OPTIONS, OPTIONS_POOL)
    table = {}
    if choice == '0':
        print("Exit without reading existing table record")

    # read game's record dictionary .txt with 2 line on one record
    elif choice == '' or choice == '2':
        try:
            record_file = open('record_trivia_file.txt', 'r')
            table_raw = record_file.readlines()
            for i in range(0, len(table_raw)//2) :
                table[table_raw[2*i].strip('\n')] = table_raw[2*i+1].strip('\n')
            record_file.close()
        except (EOFError, FileNotFoundError):
            print("Can't read record database. Return empty table\n")

    # read game's record dictionary .dat with module pickle
    elif choice == '1':
        try:
            record_file = open('record_trivia_file.dat', 'rb')
            table = pickle.load(record_file)
            record_file.close()
        except (EOFError, FileNotFoundError):
            print("Can't read record database. Return empty table\n")
    
    return table



def main():


    trivia_file = open_file("trivia_mod.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category,  value, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category, "\nValue of the question: ", value)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(value)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n\n\n")

        # get next block
        category,  value, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)

    # extract game's record dictionary with pickle or from .txt file
    table = read_record()

    # work with record table (change, view)
    table = record_table(table, score)

    # save record table in various data format (txt, dat)
    save_record(table)



main()
input("\n\nPress the enter key to exit.")
