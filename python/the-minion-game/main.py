def minion_game(string):
    vowel_score = 0
    consonant_score = 0
    string_len = len(string)
    for i in range(string_len):
        if string[i] in 'AEIOU':
            vowel_score += string_len - i
        else:
            consonant_score += string_len - i

    if consonant_score > vowel_score:
        print('Stuart ' + str(consonant_score))
    elif vowel_score > consonant_score:
        print('Kevin ' + str(vowel_score))
    else:
        print('Draw')


if __name__ == '__main__':
    # s = raw_input()
    minion_game('BANANA')
