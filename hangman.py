def print_hangman(num_of_tries):
    """
    Prints the hangman situation depending on the amount of mistakes made
    :param mistake_count: number of mistakes
    :type mistake_count: int
    :return: None
    """
    print(HANGMAN_PHOTOS.get(num_of_tries))

def guess():
    """
    Asks the user to guess a letter and prints it to the screen
    :return: None
    """
    print("Guess a letter")
    print(input())

def board_game(str_length):
    """
    Creates the hangman board game by printing the number of letters needed to guess
    where each letter is reprsented by '_'
    For example: the word 'hello' will be reprsented as '_ _ _ _ _'
    :param str_length: the length of the word needed to guess
    :param type: int
    :return: None
    """
    print("_ " * str_length)

def check_valid_input (letter_guessed, old_letters_guessed):
    """
    Chekcs whether a given character is a valid input letter in the alphabet
    AND whether or not it has been guessed before
    If it is a valid single letter in the alphabet that hasnt been guessed before
    returns True, otherwise returns False
    :param letter_guessed: the guessed letter
    :param type: string
    :param old_letters_guessed: old letters that have been guessed
    :param type: string
    :return: returns True if guessed letter is valid input and hasnt been guessed yet
    Otherwise returns False
    :rtype: bool
    """

    if (len(letter_guessed) > 1):
        if (letter_guessed.isalpha()):
            return False
        else:
            return False

    elif (len(letter_guessed) == 1):
        if (not letter_guessed.isalpha()):
            return False
        elif (letter_guessed in old_letters_guessed):
            return False
    return True

def try_update_letters_guessed (letter_guessed, old_letters_guessed):
    """
    Chekcs whether letter guessed is valid according to the hangman rules of play
    If it is, updates the guessed letters and returns True
    Else, prints 'X', beneath it the old letters guessed and returns False
    :param letter_guessed: the guessed letter
    :param type: string
    :param old_letters_guessed: old letters that have been guessed
    :param type: list
    :return: True if letter guessed is valid and otherwise False
    :rtype: boolean
    """
    if (check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        old_letters_string = ' -> '.join(old_letters_guessed)
        print('X\n' + old_letters_string.lower())
    return False

def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function recieves a secret word and guessed letters.
    It returns a new string made up of letters and '_' such that if a guessed
    letter is in the secret word it would show them in their position
    For example, the secret word being 'otters' and the guessed letters are "'t', 'a', 'm'
    the function will return the string '_ t t _ _ _ '
    :param secret_word: the secret word
    :param typy: string
    :param old_letters_guessed: the guessed letters
    :param type: list
    :return: new string contatining correct letters and '_' in places that havent been guessed
    :rtype: string
    """
    my_list = ['_'] * (len(secret_word))
    for letter in old_letters_guessed:
            count = 0
            for secret_letter in secret_word:
                if (secret_letter == letter):
                    my_list[count] = secret_letter
                count += 1
    new_word = ' '.join(my_list)
    return new_word

def choose_word(file_path, index):
    """
    The functions recieves a file path and an index and returns
    the word at the given index in the file
    :param file_path: the file's path
    :param type: string
    :param index: the given index
    :param type: int
    :return: word at the given index
    :rtype: string
    """
    index -= 1
    with open(file_path, 'r') as input_file:
        txt = input_file.read().split(' ')
        word_count = count_words(txt)
        guess_word = word_from_list(txt, index)
        return guess_word

def word_from_list(my_list, index):
    """
    Returns a word at a given index from a list.
    If the index is larger than the list's length then it returns to the beggining
    and counts on from there.
    For example: the list being ['a', 'b', 'c'] and the index being 4,
    the function will return 'b'
    :param my_list: the given list
    :param type: list
    :param index: the given index
    :param type: int
    :return: word at given index
    :rtype: string
    """
    if (index < len(my_list)):
        return my_list[index]
    else:
       return my_list[index % len(my_list)]

def count_words(my_list):
    """
    Returns the number of words in a list while ignoring doubles
    :param my_list: the given list
    :param type: list
    :return: number of words ignoring doubles
    :rtype: int
    """
    temp_list = []
    for i in range(1, len(my_list)):
        if (not my_list[i] in temp_list):
            temp_list.append(my_list[i])
    return len(temp_list)

HANGMAN_PHOTOS = {0: "x-------x",
                  1: "x-------x\n|\n|\n|\n|\n|",
                  2: "x-------x\n|       |\n|       0\n|\n|\n|",
                  3: "x-------x\n|       |\n|       0\n|\n|\n|",
                  4: "x-------x\n|       |\n|       0\n|      /|\\ \n|\n|",
                  5: "x-------x\n|       |\n|       0\n|      /|\\ \n|      /\n|",
                  6: "x-------x\n|       |\n|       0\n|      /|\\ \n|      / \ \n|"         
                 }

MAX_TRIEX = 6

def main():

   # print("Enter file path")
    file_path = r"" # words file path
    print("Enter index")
    index = int(input())
    f = open(r"", 'r') # opening screen file path
    print (f.read())
    f.close()

    old_letters_guessed = []
    num_of_tries = 0
    secret_word = choose_word(file_path, index)
    print_hangman(num_of_tries)
    print()
    while(num_of_tries < 6):
        print("Guess a letter")
        letter_guessed = input()
        bool_guess = try_update_letters_guessed(letter_guessed, old_letters_guessed)
        if(bool_guess):
            if not letter_guessed in secret_word:
                print (":(")
                num_of_tries += 1
                print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))
        if (not '_' in show_hidden_word(secret_word, old_letters_guessed)):
            break
    print()
    if num_of_tries == 6:
        f = open(r"", 'r') # loose screen file path
        print (f.read())
        f.close()
    else:
        f = open(r"", 'r') # win screen file path
        print (f.read())
        f.close()


if __name__ == "__main__":
    main()


