


def give_answer(guess, wordle):
    x_spots, g_spots, taken = [], [], []
    for i in range(5):
        if guess[i] == wordle[i]:
            g_spots.append(i)
            taken.append(i)
        else:
            x_spots.append(i)
    y_spots = []
    for i in x_spots:
        for j in range(5): 
            if j in taken:
                continue
            if guess[i] == wordle[j] and i not in y_spots:
                y_spots.append(i)
                taken.append(j)
    answer = ''
    for i in range(5):
        if i in g_spots:
            answer += 'G'
        elif i in y_spots:
            answer += 'Y'
        else:
            answer += 'X'
    return answer


if __name__ == "__main__":
    with open('Files\sgb-words.txt', 'r') as file:
        words = [w[:5] for w in file.readlines()]
        with open('Files\lookup-table-sgb.txt', 'w') as lookup_table:
            for guess in words:
                for wordle in words:
                    lookup_table.write(give_answer(guess, wordle))
                lookup_table.write('\n')
    