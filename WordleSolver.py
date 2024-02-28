
from WordleGame import wordleGame

def solveWordle(wordle):
    if type(wordle) != wordleGame:
        raise TypeError('solveWordle must take a wordleGame as argument')
    game, answer = wordle, None
    while answer != 'GGGGG':
        scores = game.giveGuesses()
        guesses = [score[0] for score in scores] 
        guessesDisplayed = 5
        print(guesses[:guessesDisplayed])
        # while True == True:
        #     moreGuesses = input('Show more guesses [Y/N]?: ')
        #     while moreGuesses != 'Y' and moreGuesses != 'N':
        #         moreGuesses = input('Show more guesses [Y/N]?: ')
        #     if moreGuesses == 'N':
        #         break
        #     if guessesDisplayed == 30:
        #         print(guesses[:30])
        #         print('max number of guesses to be displayed is 30')
        #         break
        #     else:
        #         guessesDisplayed += 3
        #         print(guesses[:guessesDisplayed])
        
        with open('Files\wordle-answers-alphabetical.txt', 'r') as file:
            words = [w[:5] for w in file.readlines()]
            guess = input('guess: ')
            while guess not in words:
                print('please enter a valid wordle solution')
                guess = input('guess: ')
                
        answer = input('answer: ')
        while len(answer) != 5 or set(answer) - {'X', 'Y', 'G'} != set():
            print('please enter valid answer')
            answer = input('answer: ')
        
        if guess in guesses:
            accepts = scores[guesses.index(guess)][2][answer]
        else:
            accepts = []
        game = wordleGame([game.guesses] + [guess], 
                          [game.answers] + [answer],
                          game.dictionary,
                          accepts)
  
if __name__ == "__main__":
    print('Please enter your guesses so far as a comma separated list, e.g. grain, after, spear. If you are solving a new game prior to making any guesses, leave the prompt blank and hit enter.')
    guesses = input('guesses: ')
    print('\nNow give the responses given by Wordle, again as a comma separated list. For each guess, please give a five character string. The colours given to a letter by Wordle should be inputted as follows: ')
    print('grey = X, yellow = Y, green = G')
    print('So if "after" was guessed and f, t were not in the hidden word, a and e were, but we had them in the wrong place and r was in the word and was in the right place, one would input YXXYG')
    answers = input('answers: ')
    guesses = [g.strip() for g in guesses.split(',')]
    answers = [a.strip() for a in answers.split(',')]
    solveWordle(wordleGame(guesses, answers))
        