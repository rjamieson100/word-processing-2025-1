from getkey import getkey, keys

#keep version number within 2 sig-digs (eg. v3.22)
version = "1.00"

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
           "Olivia Chezzi", "Luca B & Qui Loi Tran", 
           "Luca B & Qui Loi Tran", "Luca B & Qui Loi Tran",
           "Jun Li & Keith Marley", "Jun Li & Keith Marley", "Aidan McFadden"]



def merica(words):
    """
    List all the words that can be spelled using only the 2-letter shortcodes for the 50 American states. (AL, AK, AZ, AR, CA, CO, CT, ...)
    Example: VANDAL (Virginia, North Dakota, Alabama).

    This definition is O(n^3) notation, as it has 3 nested loops.
    """
    list_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT",
                       "DE", "FL", "GA", "HI", "ID", "IL",
                       "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                       "MA", "MI", "MN", "MS", "MO", "MT", "NE",
                       "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
                       "OH", "OK", "OR", "PA", "RI", "SC", "SD",
                       "TN", "TX", "UT", "VT", "VA", "WA", "WV",
                       "WI", "WY"] #50 long
    list_words = words
    list_spelled = [] #list of words that can be spelled using the codes
    for x in range (len(list_words)): #list of words
        success = 0
        if len(list_words[x]) % 2 == 0 and len(list_words[x]) > 0: #even length, not nothing
            for y in range (len(list_words[x])-1): #length of word
                for z in range(len(list_codes)): #list of codes
                    if (list_words[x].lower()[0+y*2:2+y*2]) == list_codes[z].lower(): #check
                        success += 2
            #all pairs in the word have been checked    
            if success == len(list_words[x]):
                list_spelled.append(list_words[x])
        #else, does nothing with it
    return(list_spelled)

# A custom set of valid words to check the word list for
valid_words = {"stressed", "diaper", "repaid", "desserts", "drawer", "reward", "deliver", "reviled", "gateman", "nametag", "dog", "god", "tag", "gat", "live", "evil", "devil", "lived", "now", "won", "parts", "strap", "flow", "wolf", "rat", "tar", "snug", "guns", "lager", "regal", "pat", "tap", "mood", "doom", "diodes", "seodi", "rip", "pir", "pit", "tip", "taps", "spat", "stun", "nuts"}

# Function to find reversible words that are not palindromes, ensuring only one of each pair is included
def find_reversible_non_palindromes():
    """
    Finds words in the predefined list where the reversed version forms a valid word but is not a palindrome.
    Ensures only one word from each reversible pair is included.
    
    Returns:
        list: A list of words that meet the criteria.
    """
    seen = set()  # Makes a set to store words already counted
    # Uses a set rather than list because a set is faster than lists in gathering info as sets have a Big O of O(1) while lists have a Big O of O(n).
    result = []  # List to store valid words
    # Uses a list here so it retains an order.
    
    for word in words:
        reversed_word = word[::-1]  # Reverses the word
        
        # Ensure reversed word is valid, is not a palindrome, and has not already been counted
        if reversed_word in valid_words and word != reversed_word and reversed_word not in seen:
            result.append(word)  # Add to the result list
            seen.add(word)  # Mark this word as counted
            seen.add(reversed_word)  # Also mark the reversed word as counted to avoid duplicates
    
    return result if result else ["No reversible words found"]  # Ensures non-empty output

# List of words to search through
words = ["stressed", "diaper", "deliver", "hello", "world", "drawer", "gateman", "racecar"]

# Call the function and store the results
reversible_words = find_reversible_non_palindromes()
print(reversible_words)  # Output: Words that have a valid reversed counterpart

def backwards(words_list):
    backwards = find_reversible_non_palindromes()
    return(backwards)

valid_word_set = {"dry", "nude", "star", "example", "hello", "bun", "lid", "red", "pen", "cat"}

def find_valid_words(word_list):
    # Create an empty list to store the valid words
    valid_words = []

    # Loop through each word in the provided word list
    for word in word_list:
        
        # Check if the word has at least 5 letters (for odd-numbered letters)
        if len(word) >= 5:
            
            # Extract the odd-numbered letters from the word (1st, 3rd, 5th, ...)
            odd_letters = word[::2]
            
            # Extract the even-numbered letters from the word (2nd, 4th, 6th, ...)
            even_letters = word[1::2]
            
            # Check if either the odd or even letters form a valid word
            if len(odd_letters) >= 3 and odd_letters.lower() in valid_word_set:
                valid_words.append(word)
            elif len(even_letters) >= 3 and even_letters.lower() in valid_word_set:
                valid_words.append(word)

    # After processing all words, return the list of valid words
    return valid_words

def odd_even(word_list):
    valid_words = find_valid_words(word_list)
    return valid_words


def wordle_panic (file_list):
    '''
    this function takes a word from a list and determines if you could guess
    the wordle based off the other words in the list.
    @param file_list: the list of words from the text file
    @return: a list of words
    Big O Notation: O(n^2) - it runs through the list for every element in the list
    '''

    listy = []
    #only gets the five letter words
    for x in file_list:
        if len(x) == 5:
            listy.append(x)

    listy = [x.lower() for x in listy]
    listy = sorted(listy)
    x = 0
    word_list = []
    #this loop goes through all the elements of the list. It's a while loop
    #because it needs to increase by more than just one sometimes.
    while x < len(listy):
        word_count = 0
        word = listy[x]
        n = x+1

        #This loop is used to compare the list @ x to the next position of
        #the list. This makes it so that n can increase while x remains the
        #same.
        while n < len(listy):
            next_word = listy[n]
            incorrect_letters = 0
            #compares the letters of two words
            for i in range(len(listy[x])):
                if word[i] != next_word[i]:
                    incorrect_letters += 1
                    if incorrect_letters == 1 and word_count == 0:
                        letter = i

            #only adds a word if they only have a one letter difference  
            if incorrect_letters == 1:
                word_count += 1
                wrong_letter = letter
            elif incorrect_letters > 1:
                break
            n += 1

        # >= 4 because it doesn't count the starting word
        if word_count >= 4:
            wordle_word = ""
            for i in listy[x]:
                if i == word[wrong_letter]:
                    wordle_word += "_"
                else:
                    wordle_word += i
            word_list.append(wordle_word)

        x += word_count+1

    #this is for words that only have different first letters
    first_let_list = []
    for x in range(len(listy)):
        first_let_list.append(listy[x][1:])
    first_let_list = sorted(first_let_list)
    
    x = 0
    while x < len(first_let_list):
        count = 0
        while first_let_list[x]==first_let_list[count+1]:
            count += 1
            if count+1 > len(first_let_list)-1:
                #break here because otherwise it'll crash as it is out of index
                break

        # >= 4 because it doesn't count the starting word
        if count >= 4:
            wordle_word = "_" + first_let_list[count]
            word_list.append(wordle_word)
            
        x += count+1
        
    
    
    return word_list

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


'''
Finds all the anagrams of a word in a text file
Precondition: word must be a valid word w/ alphanumeric characters only.

# @param word The word of interest that we will return all the possible words with
# @return An array of words that are anagrams of our word
# Runtime: O(nk) where k is the length of the word, and n is the length of the text file.
    Contains 1 nested loop which iterates over the length of the text file and the length
    of the inputted word, thus having O(nk) where n is the size of the text file and k
    is the length of the word inputted.

'''
def Anagram(word):
    f = open("words.txt", "r")

    words = f.read().splitlines()
    word_letters = {} # the dictionary / map containing all freq of letters in word
    arr_of_letters = [] # an array containing maps of all freq of letters in word
    arr_of_valid_words = [] # the valid words that will be returned 

    total_length = len(word)
    for letter in word: # adds up the frequency of each letter in the word
        word_letters[letter] = word_letters.get(letter, 0) + 1 

    for x in words:
        if(len(x) == total_length):
            letters_in_arr = {"original_word": x} # used to keep track of the actual word
            for letter in x: # adds up the frequency of each letter of each word in file
                letters_in_arr[letter] = letters_in_arr.get(letter,0) + 1
            arr_of_letters.append(letters_in_arr)


    for dictionary in arr_of_letters:
        valid_to_push = True
        for key in word_letters: 
            if(dictionary.get(key,0) != word_letters.get(key,0)):
                valid_to_push = False #checks to see if every frequency is the same
                break
        if(valid_to_push):
            arr_of_valid_words.append(dictionary["original_word"])

    return arr_of_valid_words

'''
Finds all the anagrams of a word in a text file
Precondition: word must be a valid word w/ alphanumeric characters only.

# @param word The word of interest that we will return all the possible words with
# @return An array of words that are anagrams of our word
# Runtime: O(nk) where k is the length of the word, and n is the length of the text file.
    Contains 1 nested loop which iterates over the length of the text file and the length
    of the inputted word, thus having O(nk) where n is the size of the text file and k
    is the length of the word inputted.

'''
def Anagrams_Minus_One(word):
    f = open("words.txt", "r")

    words = f.read().splitlines()
    #figure out how to split this instantly
    word_letters = {} # the dictionary / map containing all freq of letters in word
    arr_of_letters = [] # an array containing all dicts of freq of letters in word in txt
    arr_of_valid_words = [] # the valid words that will be returned by the function
    total_length = len(word) 
    for letter in word:
        word_letters[letter] = word_letters.get(letter, 0) + 1

    for x in words:
        if(len(x) == total_length - 1): # ensures that the word in file is valid
            letters_in_arr = {"original_word": x}
            for letter in x:
                letters_in_arr[letter] = letters_in_arr.get(letter,0) + 1
            arr_of_letters.append(letters_in_arr)


    for dictionary in arr_of_letters:
        difference = 0; 
        for key in word_letters:
            difference = difference + abs(dictionary.get(key,0) - word_letters.get(key,0))

        if(difference == 1): # tracks the difference of letters such that if it is off by 1 it is valid
            arr_of_valid_words.append(dictionary["original_word"])

    return arr_of_valid_words


def here_or_there(word_list, letter, num_1, num_2):
    """
    Given a list, letter x, and two indecies, determines
    which index x occurs at most over every word in
    the list.

    O(n)

    @param: word_list = The list of words word_list will scan.
    @param: letter = the letter to check indecies for.
    @param: num_1 = the first index to check.
    @param: num_2 = the second index to check.
    @return: the index of the given two, which x occurs most.
        If the two indecies have equal occurances of x,
        -1 will be returned. If one of the given indecies
        is out of range for all words (word length: 7, index 7)
        (negative indecies as well) -2 is returned. If more than
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

def menu_phase(phase):
    """"
    prints the corresponding phase of the menu
    (which button is being highlighted)"

    @param phase: the button being selected
    """
    for x in range(100):
        print("\n")

    print("(esc) to close program")
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
    """"
    opens the function menu
    """
    selection = 1
    move = None

    while move != "\n" and move != "\r" and move != "m":

        for x in range(100):
            print("\n")

        print("(m) return to menu")
        print("\n")
        print_function_selection(selection)

        move = getkey()
        if move == "s" and selection < len(functions):
            selection += 1
        elif move == "w" and selection > 1:
            selection -= 1

    if move == "m":
        selection = 0
        menu()
    
    for x in range(100):
        print("\n")
    
    if selection == 1:
        ##Instert call for All vowels
        print("All Vowels")

    elif selection == 2:
        ##Instert call for Most Letters
        print("Most Letters")

    elif selection == 3:
        words_merica = merica(words_list)
        print("\n")
        for x in words_merica:
            print(x)

    elif selection == 4:
        backwards_non_palindromes = backwards(words_list)
        print("\n")
        for x in backwards_non_palindromes:
            print(x)

    elif selection == 5:
        ##Instert call for Odd/Even
        valid_words = odd_even(words_list)
        print("\n")
        for x in valid_words:
            print(x)

    elif selection == 6:
        word_list = wordle_panic(words_list)
        print("\n")
        for x in word_list:
            print(x)

    elif selection == 7:
        word_to_solve = input('Word to Solve: ')
        matched_words = crosswordSolver(word_to_solve)
        print("\n")
        for x in matched_words:
            print(x)

    elif selection == 8:
        word = input('Word to Minus One: ')
        matched_words = minusOne(word)
        print("\n")
        for x in matched_words:
            print(x)

    elif selection == 9:
        word = input('Word to Plus One: ')
        matched_words = plusOne(word)
        print("\n")
        for x in matched_words:
            print(x)

    elif selection == 10:
        word = input("Word: ")
        anagrams = Anagram(word)
        print("\n")
        for x in anagrams:
            print(x)

    elif selection == 11:
        word = input("Word: ")
        anagrams = Anagrams_Minus_One(word)
        print("\n")
        for x in anagrams:
            print(x)

    elif selection == 12:
        letter = input("letter: ")
        num_1 = int(input("Index 1: "))
        num_2 = int(input("Index 2: "))
        common_index = here_or_there(words_list, letter, num_1, num_2)
        print(common_index)


def words():
    """
    Opens the words menu
    """
    for x in range(100):
        print("\n")

    for x in w_button:
        print(x.center(53))
    print("\n")
    for x in range(len(words_list)):

        for y in range(20):
            print(" ", end = "")

        print(str(x + 1) + ".  " + words_list[x])

    print("\n")
    print("(m) return to menu")

    while True:
        exit = getkey()
        if exit == "m":
          break
    menu()

def credits():
    """
    Opens the credits
    """

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
    print("𝐔𝐈 / 𝐌𝐞𝐧𝐮: " + "Aidan McFadden")
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
        exit = getkey()
        if exit == "m":
          break
    menu()

def menu():
    """"
    Opens the main menu
    """
    option = 1
    move = None

    while move != "\n" and move != "\r" and move != "\x1b":
        menu_phase(option)
        move = getkey()

        if move == "s" and option < 3:
            option += 1
        elif move == "w" and option > 1:
            option -= 1

    if move == "\x1b":
        quit()

    if option == 1:
        function_menu()
    elif option == 2:
        words()
    elif option == 3:
        credits()

menu()