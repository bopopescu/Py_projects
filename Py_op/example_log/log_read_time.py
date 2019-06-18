from datetime import datetime

def ReadWordList():
    """ Loop through each line in english.txt and add it to the list in uppercase.

    Returns:
    Returns array with all the words in english.txt.

    """
    l_words = []
    with open(r'c:\english.txt', 'r') as f_in:
        for line in f_in:
            line = line.strip().upper()
            l_words.append(line)

    return l_words

# Loop through each line in english.txt and add it to the l_words list in uppercase.
l_words = ReadWordList()
l_words = {key: None for key in l_words}
#l_words = set(l_words)
#l_words = tuple(l_words)

t1 = datetime.now()

for i in range(10000):
    #w = 'ZEBRA' in l_words
    w = bi_contains(l_words, 'ZEBRA')

t2 = datetime.now()
print('After: ' + str(t2 - t1))

# list = 41.025293 seconds
# dict = 0.001488 seconds
# set = 0.001499 seconds
# tuple = 38.975805 seconds
# list with bi_contains = 0.014000 seconds


###
