def count_word_frequency(text):
    word_frequency = {}
    words = text.split()
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

# Example usage:
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit ipsum"
word_frequency = count_word_frequency(text)
print("Word frequency:", word_frequency)
