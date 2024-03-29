
class wordleGame:
    def __init__(self, guesses, answers, dictionary = 'large', accepts = None):
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
        
        
    def giveGuessesHard(self):
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
            if (self.guesses, self.answers) == ([], []):
                scores = []
                for i in [words.index('trace'), 
                          words.index('least'),
                          words.index('stale'),
                          words.index('crate'),
                          words.index('slant')]:
                    patterns = {}
                    for x in range(len(words)):
                        try:
                            patterns[lookup_table[i][x * 5 : (x + 1) * 5]].append(x)
                        except: 
                            patterns[lookup_table[i][x * 5 : (x + 1) * 5]] = [x]
                    scores.append((words[i], None, patterns))
                return scores
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
                    if p != 'GGGGG':
                        avg_words += len(patterns[p])**2
                avg_words /= len(accepts)
                scores.append((words[i], avg_words, patterns))
                scores.sort(key = lambda x: x[1])                    
            return scores
    
    def giveGuessesNormal(self):
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
            if (self.guesses, self.answers) == ([], []):
                scores = []
                for i in [words.index('trace'), 
                          words.index('least'),
                          words.index('stale'),
                          words.index('crate'),
                          words.index('slant')]:
                    patterns = {}
                    for x in range(len(words)):
                        try:
                            patterns[lookup_table[i][x * 5 : (x + 1) * 5]].append(x)
                        except: 
                            patterns[lookup_table[i][x * 5 : (x + 1) * 5]] = [x]
                    scores.append((words[i], None, patterns))
                return scores
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
            for (i, w) in enumerate(words):
                patterns = {}
                for x in accepts:
                    try:
                        patterns[lookup_table[i][x * 5 : (x + 1) * 5]].append(x)
                    except: 
                        patterns[lookup_table[i][x * 5 : (x + 1) * 5]] = [x]
                avg_words = 0
                for p in patterns:
                    if p != 'GGGGG':
                        avg_words += len(patterns[p])**2
                avg_words /= len(accepts)
                scores.append((w, avg_words, patterns))
            scores.sort(key = lambda x: x[1])
            if scores[0][1] < 1:
                newScores = []
                n = 0
                while scores[n][1] < 1:
                    newScores.append(scores[n])
                    n += 1
                scores = newScores
            return scores
        





            
                            
                    
    
    
                    
                
