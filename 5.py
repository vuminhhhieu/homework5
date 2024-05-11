def count_unique_words(sentence):
    
    words = sentence.split()

    
    word_count = {}

  
    for word in words:
        
        if word not in word_count:
            word_count[word] = 1

    
    unique_word_count = len(word_count)

    return unique_word_count


sentence = input("Nhập câu: ")


result = count_unique_words(sentence)
print("Số từ duy nhất trong câu là:", result)
