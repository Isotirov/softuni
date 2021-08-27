secret_words = input().split()

decrypted = []

for word in secret_words:
    first_char = ""
    alphas = ""
    current_word = [x for x in word]
    for i in current_word:
        if i.isdigit():
            first_char += i
    first_char = chr(int(first_char))
    rest_of_word = [x for x in current_word if x.isalpha()]
    rest_of_word[0], rest_of_word[-1] = rest_of_word[-1], rest_of_word[0]
    for ii in rest_of_word:
        if ii.isalpha():
            alphas += ii
    current_decrypt = first_char + alphas
    decrypted.append(current_decrypt)
print(" ".join(decrypted))