'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    if word == '':
        print(count)
        return count
    target='th'
    if len(word) < 2:
        print('hi', count)
        return count
    if word[0:2] == target:
        count = count + 1
    word = word[1:]
    return count + count_th(word)
    
  
print(count_th("abcthath"))