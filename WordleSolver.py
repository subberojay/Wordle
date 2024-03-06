
from WordleGame import wordleGame

def solveWordle(wordle, gameMode = 'hard', guessesDisplayed = 5):
    if type(wordle) != wordleGame:
        raise TypeError('solveWordle must take a wordleGame as argument')
    if wordle.dictionary == 'small':
        wordsFile = 'Files\wordle-answers-alphabetical.txt'
    elif wordle.dictionary == 'large':
        wordsFile = 'Files\sgb-words.txt'
    game, answer = wordle, None
    if gameMode == 'hard':
        while answer != 'GGGGG':
            scores = game.giveGuessesHard()
            guesses = [score[0] for score in scores] 
            print(guesses[:guessesDisplayed])
            with open(wordsFile, 'r') as file:
                words = [w[:5] for w in file.readlines()]
                guess = input('guess: ')
                while guess not in words:
                    print('guess not in current dictionary')
                    guess = input('guess: ')
            answer = input('answer: ')
            while len(answer) != 5 or set(answer) - {'X', 'Y', 'G'} != set():
                print('please enter valid answer')
                answer = input('answer: ')
            if guess in guesses:
                accepts = scores[guesses.index(guess)][2][answer]
            else:
                accepts = []
            game = wordleGame(game.guesses + [guess], 
                              game.answers + [answer],
                              game.dictionary,
                              accepts)
    elif gameMode == 'normal':
        while answer != 'GGGGG':
            scores = game.giveGuessesNormal()
            guesses = [score[0] for score in scores] 
            print(guesses[:guessesDisplayed])
            with open(wordsFile, 'r') as file:
                words = [w[:5] for w in file.readlines()]
                guess = input('guess: ')
                while guess not in words:
                    print('guess not in current dictionary')
                    guess = input('guess: ')
            answer = input('answer: ')
            while len(answer) != 5 or set(answer) - {'X', 'Y', 'G'} != set():
                print('please enter valid answer')
                answer = input('answer: ')
            if guess in guesses:
                accepts = scores[guesses.index(guess)][2][answer]
            else:
                accepts = []
            game = wordleGame(game.guesses + [guess], 
                              game.answers + [answer],
                              game.dictionary,
                              accepts)
  
if __name__ == "__main__":
    dictSize, gameMode, guessesDisplayed = 'large', 'hard', 5
    print('Please enter your guesses so far as a comma separated list, e.g. grain, after, spear. If you are solving a new game prior to making any guesses, leave the prompt blank and hit enter. You can also view and change settings options by entering "settings".')
    guesses = input('guesses: ')
    while guesses == 'settings':
        print('Settings that may be altered are:'
              '\n\nDictionary size - This can either be "small" or "large". Small contains only the 2315 that are potential wordles. Rarer words, plurals and more will never be the solution to a wordle and are excluded from this dictionary. Large contains 5755 words, but still not all five letter words. The default size is large.'
              '\nGame mode - This can be "normal" or "hard". Wordle offers both regular and "Hard Mode" in its settings. In Wordle\'s Hard Mode, only guesses that fit the current pattern may be given. For example if we\'ve guessed TRACE and the T has turned yellow, our next guess must contain a T. Hard mode here obeys the same convention. The default mode is hard. Note that the solver runs quicker in hard mode, as it has less words to check.'
              '\nGuesses displayed - This governs the maximum amount of suggestions the solver will give at a time. The default setting is 5.')
        settingToChange = None
        while settingToChange != '':
            settingToChange = input('Setting to change (leave blank to exit): ')
            if settingToChange.casefold() == 'dictionary size':
                dictSize = None
                while dictSize not in ['small', 'large']:
                    print('Please select either "small" or "large" dictionary size.')
                    dictSize = input('Dictionary size: ').casefold()
            elif settingToChange.casefold() == 'game mode':
                gameMode = None
                while gameMode not in ['normal', 'hard']:
                    print('Please select either "normal" or "hard" game mode.')
                    gameMode = input('Game mode: ').casefold()
            elif settingToChange.casefold() == 'guesses displayed':
                guessesDisplayed = None
                isInt = False
                while isInt is False:
                    print('Please give an integer value for the number of guesses to be displayed.')
                    guessesDisplayed = input('Guesses displayed: ')
                    try:
                        guessesDisplayed = int(guessesDisplayed)
                        isInt = True
                    except ValueError:
                        isInt = False
            elif settingToChange != '':
                print('Please enter "Dictionary size", "Game mode", or "Guesses displayed" to change one of these settings. Leave blank to exit.')
        guesses = input('guesses: ')
    print('\nNow give the responses given by Wordle, again as a comma separated list. For each guess, please give a five character string. The colours given to a letter by Wordle should be inputted as follows: '
    '\n\n    grey = X, yellow = Y, green = G'
    '\n\nSo if "after" was guessed and f, t were not in the hidden word, a and e were, but we had them in the wrong place and r was in the word and was in the right place, we would input YXXYG')
    answers = input('answers: ')
    guesses = [g.strip() for g in guesses.split(',')]
    answers = [a.strip() for a in answers.split(',')]
    if guesses == ['']:
        guesses = []
    if answers == ['']:
        answers = []
    solveWordle(wordleGame(guesses, answers, dictSize), gameMode, guessesDisplayed)
        