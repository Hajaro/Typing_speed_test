from english_words import english_words_lower_set

count = 0
string_of_words = ""
for element in english_words_lower_set:
    string_of_words += element
    string_of_words += " "
    count += 1
    if count == 216:
        break

print(string_of_words)