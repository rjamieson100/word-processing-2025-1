"""
Crossword Solver: Given a string parameter in the form "??E?R", find all words that fit.

Minus One: Given a String parameter, list all words that can be made by removing
a single letter, and keeping the remaining order intact.

Plus One: The reverse of "minus one"; this should list all words that can be made
by adding a single letter into any position.
"""


class Main:
    def __init__(self) -> None:
        self.words = open('./words.txt', 'r', encoding = 'utf-8').read().splitlines()

    def prepareWordlist(self, uppercase: bool = False) -> list:
        words = set()
        for word in self.words:
            if uppercase:
                words.add(word.upper())
            else:
                words.add(word.lower())
        return list(words)

    def crosswordSolver(self, pattern: str) -> list:
        """
        Returns a list of words from a wordlist that match the given pattern.
    
        The pattern can include '?' as a wildcard that matches any letter.
    
        @param pattern: The pattern to match, with '?' as a wildcard.
        @return: A list of valid words matching the pattern, in lowercase.
        """
        valid_words = set()

        for word in self.words:
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

    def minusOne(self, word: str) -> list:
        """
        Returns a list of words from a wordlist that can be formed by removing one character from `word`.
    
        @param word: The word from which a character will be removed.
        @return: A list of valid words formed by removing one character from the input word, in lowercase.
        """
        valid_words = set()
        word_variations = set()

        for i in range(len(word)):
            word_variations.add(word.lower()[:i] + word.lower()[i + 1:])

        for word in self.words:
            if word.lower() in word_variations:
                valid_words.add(word.lower())
        return list(valid_words)

    def plusOne(self, word: str) -> list:
        """
        Returns a list of words from a wordlist that can be formed by adding one letter to `word`.
    
        @param word: The word to which a single letter will be added.
        @return: A list of valid words formed by adding one letter to the input word.
        """
        valid_words = set()

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            for i in range(len(word) + 1):
                altered_word = word.lower()[:i] + letter + word.lower()[i:]

                if altered_word in self.words:
                    valid_words.add(altered_word)
        return list(valid_words)


if __name__ == '__main__':
    main = Main()

    word_to_solve = '??E'
    matched_words = main.crosswordSolver(word_to_solve)
    ...
