
class wordleGame:
    def __init__(self, guesses, answers, accepts = None):
        if accepts is None:
            accepts = []
        if type(guesses) != list or type(answers) != list:
            raise TypeError('guesses and answers must be provided as lists')
        if len(answers) != len(guesses):
            raise ValueError('please provide an answer for each guess')
        self.guesses = guesses
        self.answers = answers
        self.accepts = accepts
        
        
    def giveGuesses(self):
        with open('Files\wordle-answers-alphabetical.txt', 'r') as file:
            words = [w[:5] for w in file.readlines()]
            table =  open('Files\lookup-table.txt', 'r')
            lookup_table = table.readlines()
            table.close()
            
            # if (self.guesses, self.answers) == ([], []):
            #     return 'trace'
            
            if self.accepts == []:
                accepts = range(len(words))
                for (n, guess) in enumerate(self.guesses):
                    new_accepts = []
                    i = words.index(guess)
                    answer = self.answers[n]
                    for x in accepts:
                        if lookup_table[i][x * 5 : (x + 1) * 5] == answer:
                            new_accepts.append(x)
                    accepts = new_accepts.copy()
            else:
                accepts = self.accepts
            scores = []
            for i in accepts:
                patterns = {}
                for x in accepts:
                    try:
                        patterns[lookup_table[i][x * 5 : (x + 1) * 5]].append(x)
                    except: 
                        patterns[lookup_table[i][x * 5 : (x + 1) * 5]] = [x]
                avg_words = 0
                for p in patterns:
                    avg_words += len(patterns[p])**2
                avg_words /= len(accepts)
                scores.append((words[i], avg_words, patterns))
                scores.sort(key = lambda x: x[1])                    
            return scores
        




def solveWordle(wordle):
    if type(wordle) != wordleGame:
        raise TypeError('solveWordle must take a wordleGame as argument')
    game, answer = wordle, None
    while answer != 'GGGGG':
        scores = game.giveGuesses()
        guesses = [score[0] for score in scores] 
        guessesDisplayed = 3
        print(guesses[:guessesDisplayed])
        while True == True:
            moreGuesses = input('Show more guesses [Y/N]?: ')
            while moreGuesses != 'Y' and moreGuesses != 'N':
                moreGuesses = input('Show more guesses [Y/N]?: ')
            if moreGuesses == 'N':
                break
            if guessesDisplayed == 30:
                print(guesses[:30])
                print('max number of guesses to be displayed is 30')
                break
            else:
                guessesDisplayed += 3
                print(guesses[:guessesDisplayed])
        
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
                          accepts)
        
solveWordle(wordleGame([], []))    
        
            
                            
                    
    
    
                    
                
