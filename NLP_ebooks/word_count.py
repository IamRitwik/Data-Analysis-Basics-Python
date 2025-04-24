word_list = ['chapter', 'before', 'it', 'was', 'friday', 'the', 'thirteenth', 'of', 'october', 'we', 'it', 'was', 'the', 'the']

def max_word_occurence(word_list):
    word_counts = {}

    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    max_word = None
    max_count = 0

    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            max_word = word

    return max_word, max_count


w, c = max_word_occurence(word_list)
print(type(c))
print(f"max occurrence of word: '{w}' with {c} number of times")