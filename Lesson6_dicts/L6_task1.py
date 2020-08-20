user_sentence = input('Type any sentence: ').replace(',', '').replace('.', '').lower().split(sep=' ')

unique_words = {}
for word in user_sentence:
    if word in unique_words:
        unique_words[word] += 1
    elif word not in unique_words:
        unique_words[word] = 1

print(unique_words)


