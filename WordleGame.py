
class wordleGame:
    def __init__(self, guesses, answers, dictionary = 'small', accepts = None):
        if accepts is None:
            accepts = []
        if type(guesses) != list or type(answers) != list:
            raise TypeError('guesses and answers must be provided as lists')
        if len(answers) != len(guesses):
            raise ValueError('please provide an answer for each guess')
        if dictionary not in ['small', 'large']:
            raise ValueError("dictionary argument must either be 'small' or 'large'")
        self.guesses = guesses
        self.answers = answers
        self.dictionary = dictionary
        self.accepts = accepts
        
        
    def giveGuesses(self):
        if self.dictionary == 'small':
            wordsFile = 'Files\wordle-answers-alphabetical.txt'
            lookupTableFile = 'Files\lookup-table.txt'
        else:
            wordsFile = 'Files\sgb-words.txt'
            lookupTableFile = 'Files\lookup-table-sgb.txt'
        with open(wordsFile, 'r') as file:
            words = [w[:5] for w in file.readlines()]
            table =  open(lookupTableFile, 'r')
            lookup_table = table.readlines()
            table.close()
            
            # if (self.guesses, self.answers) == ([], []):
            #      return [('trace', None),
            #              ('least', None),
            #              ('slate', None),
            #              ('crate', None),
            #              ('slant', None)]
                         
            
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
        





            
                            
                    
    
    
                    
                
