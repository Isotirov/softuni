def palindrome(word, i, new_word=""):
    if i >= len(word):
        if new_word == word:
            return f"{word} is a palindrome"
        return f"{word} is not a palindrome"
    new_word += word[len(word)-1-i]
    return palindrome(word, i+1, new_word)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))