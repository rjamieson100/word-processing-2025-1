import getkey

#keep version number within 2 sig-digs (eg. v3.22)
version = "1.34"

words_list = []

#opens a text file called "words"
words_file = open("words.txt", "r")
while True:
    line = words_file.readline().strip()
    if line == "":
        break
    else:
        words_list.append(line)
words_file.close()

title = [" __    _            _ __                                ",
         "( /   /         /  ( /  )                    o          ",
         " / / /__ _   __/    /--'_   __ _, _  (   (  ,  _ _   _, ",
         "(_/_/(_)/ (_(_/_   /   / (_(_)(__(/_/_)_/_)_(_/ / /_(_)_",
         "                                                     /| ",
         "                    Version: " + version + "                   (/  "]

f_button = ["╔═╗┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐",
            "╠╣ │ │││││   │ ││ ││││└─┐",
            "╚  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘"]

w_button = ["╦ ╦┌─┐┬─┐┌┬┐┌─┐",
            "║║║│ │├┬┘ ││└─┐",
            "╚╩╝└─┘┴└──┴┘└─┘"]

c_button = ["╔═╗┬─┐┌─┐┌┬┐┬┌┬┐┌─┐",
            "║  ├┬┘├┤  │││ │ └─┐",
            "╚═╝┴└─└─┘─┴┘┴ ┴ └─┘"]

functions = ["All Vowels", "Most Letters", "'Merica", "Backwards", "Odd/Even",
             "Wordle Panic","Crossword Solver", "Minus One", "Plus One", "Anagram",
             "Anagrams Minus One", "Here or There"]

authors = ["Farhan Mohammad", "Jun Li & Keith Marley", "Everett Campbell & Jasper Duff", 
           "Everett Campbell & Jasper Duff", "Everett Campbell & Jasper Duff", 
           "Olivia Chezzi", "Luca & Qui Loi Tran", 
           "Luca & Qui Loi Tran", "Luca & Qui Loi Tran",
           "Jun Li & Keith Marley", "Jun Li & Keith Marley", "Aidan McFadden"]


def here_or_there(word_list, letter, num_1, num_2):
    """
    Given a list, letter x, and two indecies, determines
    which index x occurs at most for each word in
    the list.

    O(n)

    @param: word_list = The list of words word_list will scan.
    @param: letter = the letter to check indecies for.
    @param: num_1 = the first index to check.
    @param: num_2 = the second index to check.
    @return: the index of the given two which x occurs most,
        if the two indecies have equal occurances of x
        -1 will be returned, if one of the given indecies
        is out of range for all words (word length: 7, index 7)
        (negative indecies as well) 2 is returned. If more than
        a single letter is entered, -3 is returned.
    """
    num_1_counter = 0
    num_2_counter = 0
    invalid_index = True
    invalid_letters = True

    if (num_1 >= 0) & (num_2 >= 0) & ((len(letter)) == 1):
        invalid_letters = False
        for x in (word_list):
            if (len(x) >= 5) & (num_1 < len(x)) & (num_2 < len(x)):
                invalid_index = False
                if x[num_1] == letter:
                    num_1_counter += 1

                if x[num_2] == letter:
                    num_2_counter += 1
    if invalid_letters:
        return -3
    elif invalid_index:
        return -2
    elif num_1_counter > num_2_counter:
        return num_1
    elif num_1_counter < num_2_counter:
        return num_2
    else:
        return -1

def crosswordSolver(pattern: str) -> list:
    """
    Returns a list of words from a wordlist that match the given pattern.
    
    The pattern can include '?' as a wildcard that matches any letter.
    
    @param pattern: The pattern to match, with '?' as a wildcard.
    @return: A list of valid words matching the pattern, in lowercase.

    Runtime: O(nk), where 'n' is the number of words in the wordlist and 'k' is the length of word.
    """
    __words__ = open('./words.txt', 'r', encoding = 'utf-8').read().splitlines()
    valid_words = set()

    for word in __words__:
        if len(word) != len(pattern):
            continue

        match = True
        for i in range(len(pattern)):
            if pattern[i] != '?' and pattern.lower()[i] != word.lower()[i]:
                match = False
                break
        if match:
            valid_words.add(word.lower())
    return list(valid_words)

def minusOne(word: str) -> list:
    """
    Returns a list of words from a wordlist that can be formed by removing one character from `word`.
    
    @param word: The word from which a character will be removed.
    @return: A list of valid words formed by removing one character from the input word, in lowercase.

    Runtime: O(nk), where 'n' is the number of words in the wordlist and 'k' is the length of word.
    """
    __words__ = open('./words.txt', 'r', encoding = 'utf-8').read().splitlines()
    valid_words = set()
    word_variations = set()

    for i in range(len(word)):
        word_variations.add(word.lower()[:i] + word.lower()[i + 1:])

    for word in __words__:
        if word.lower() in word_variations:
            valid_words.add(word.lower())
    return list(valid_words)

def plusOne(word: str) -> list:
    """
    Returns a list of words from a wordlist that can be formed by adding one letter to `word`.
    
    @param word: The word to which a single letter will be added.
    @return: A list of valid words formed by adding one letter to the input word.
        
    O(26 * nk), where 'n' is the number of words in the wordlist, 'k' is the length of the word, 
    and 26 accounts for the number of letters in the alphabet.
    """
    __words__ = open('./words.txt', 'r', encoding = 'utf-8').read().splitlines()
    valid_words = set()

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        for i in range(len(word) + 1):
            altered_word = word.lower()[:i] + letter + word.lower()[i:]

            if altered_word in __words__:
                valid_words.add(altered_word)
    return list(valid_words)

def menu_phase(phase):
    
    for x in range(100):
        print("\n")
        
    print("𝐈𝐂𝐒𝟒𝐔𝟏'𝐬".center(53))
    
    for x in title:
        print(x.center(50))
    
    print("\n")

    if phase == 1:
        for x in f_button:
            print(x.center(53))
        print("Words".center(53))
        print("Credits".center(53))
        
    if phase == 2:
        print("Functions".center(53))
        for x in w_button:
            print(x.center(53))
        print("Credits".center(53))

    if phase == 3:
        print("Functions".center(53))
        print("Words".center(53))
        for x in c_button:
            print(x.center(53))

def print_function_selection(selection):
    for x in f_button:
        print(x.center(53))

    print("\n")
    
    for x in range(len(functions)):
        if x == selection - 1:
          print(("| " + functions[x] + " |").center(53))
        else:
          print(functions[x].center(53))

def function_menu():
    selection = 1
    moves = ["w", "s"]
    move = "s"
    if move in moves:
        while move != "\n":
          for x in range(100):
            print("\n")
          print_function_selection(selection)
          move = getkey.getkey()
          if move == "s" and selection < len(functions):
            selection += 1
          elif move == "w" and selection > 1:
            selection -= 1
    for x in range(100):
        print("\n")
    if selection == 1:
        ##Instert call for All vowels
        print("All Vowels")
    elif selection == 2:
        ##Instert call for 'Merica
        print("Merica")
    elif selection == 3:
        ##Instert call for Backwards
        print("Merica")
    elif selection == 4:
        ##Instert call for Odd/Even
        print("Merica")
    elif selection == 5:
        ##Instert call for Wordle Panic
        print("Merica")
    elif selection == 6:
        word_to_solve = input('Word to Solve: ')
        matched_words = crosswordSolver(word_to_solve)\
        print(matched_words)
        ##Instert call for Crossword Solver
    elif selection == 7:
        word = input('Word to Minus One: ')
        matched_words = minusOne(word)
        print(matched_words)
        ##Instert call for Minus One
    elif selection == 8:
        word = input('Word to Plus One: ')
        matched_words = plusOne(word)
        print(matched_words)
        ##Instert call for Plus One
    elif selection == 9:
        ##Instert call for Anagram
        print("Merica")
    elif selection == 10:
        ##Instert call for Anagrams Minus One
        print("Merica")
    elif selection == 11:
        letter = input("letter: ")
        num_1 = int(input("Index 1: "))
        num_2 = int(input("Index 2: "))
        common_index = here_or_there(words_list, letter, num_1, num_2)
        #print(letter + " appears most at index " + str(common_index))
        print(common_index)
        

def words():
    for x in range(100):
        print("\n")
    
    print("(m) return to menu")
    print("\n")
    
    for x in w_button:
        print(x.center(53))
    print("\n")
    for x in range(len(words_list)):

        for y in range(20):
            print(" ", end = "")

        print(str(x + 1) + ".  " + words_list[x])

    while True:
        exit = getkey.getkey()
        if exit == "m":
          break
    menu()

def credits():
    
    for x in range(100):
        print("\n")
    
    print("(m) return to menu")
    print("\n")
    
    for x in c_button:
        print(x.center(53))
    print("\n")

    print("𝐖𝐨𝐫𝐝 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠")
    print("\n")

    print("𝐂𝐥𝐢𝐞𝐧𝐭: " + "Monarch Park Collegiate")
    print("𝐕𝐞𝐫𝐬𝐢𝐨𝐧: " + version)
    print("𝐂𝐥𝐢𝐞𝐧𝐭 𝐏𝐨𝐢𝐧𝐭 𝐎𝐟 𝐂𝐨𝐧𝐭𝐚𝐜𝐭: " + "Mr. Jamieson")
    print("𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐌𝐚𝐧𝐚𝐠𝐞𝐫𝐬: " + "Olivia Chezzi, Aidan McFadden")
    print("")

    for g in range(55):
        print("_", end = "")
    print("\n")
    print("𝐅𝐮𝐧𝐜𝐭𝐢𝐨𝐧".center(8), end = "")
    print("𝐀𝐮𝐭𝐡𝐨𝐫𝐬".center(32))
    for g in range(55):
        print("_", end = "")
    
    print("\n")
    
    for x in range(len(functions)):
        print(functions[x], end = "")
        
        for y in range(20 - (len(functions[x]))):
            print(" ", end = "")
            
        print(authors[x], "\n")
    
    while True:
        exit = getkey.getkey()
        if exit == "m":
          break
    menu()

def menu():
    option = 1
    moves = ["w", "s"]
    move = "s"
    if move in moves:
        while move != "\n":
            menu_phase(option)
            move = getkey.getkey()
            if move == "s" and option < 3:
                 option += 1
            elif move == "w" and option > 1:
                option -= 1
    if option == 1:
        function_menu()
    elif option == 2:
        words()
    elif option == 3:
        credits()

menu()
