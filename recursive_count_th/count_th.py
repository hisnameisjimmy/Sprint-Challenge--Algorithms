'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # split the word into individual letters, using loop
    # once you get down to a single letter, you can start doing comparison
    # because h is always preceded by t, you can purely search for t, and if you find it, check the next letter in list
    # if the next letter is h, increment the number of matches
    # matches = 0
    # word_array = list(word)
    # print(f'{word_array}')
    # for i in range(len(word_array)):
    #     letter_t = "t"
    #     letter_h = "h"
    #     if word_array[i] == letter_t and word_array[i + 1] == letter_h:
    #         matches += 1
    # return matches

    # now let's do recursion
    # base case is there needs to be at least two characters and they need to be th. If it's less than 2, there are no matches.

    matches = 0
    if len(word) < 2:
        # no matches possible with less than 2 characters
        return matches
    # else start recursing
    elif (word[0] + word[1]) == 'th':
        # if first two letters match, increment matches
        matches += 1
        # then return matches along with a recursive call that moves through the word
        # letter by letter
        # the equation will come out to 1+1+1+1 type thing
    return count_th(word[1:]) + matches


print(count_th("python"))

print(count_th("thethethethe"))
