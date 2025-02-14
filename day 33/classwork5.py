def replace_word_in_sentence():
    sentence = input("Enter a sentence: ")

    old_word = input("Enter the word you want to replace: ")

    new_word = input("Enter the new word: ")

    modified_sentence = sentence.replace(old_word, new_word)

    print("Modified sentence:", modified_sentence)

replace_word_in_sentence()