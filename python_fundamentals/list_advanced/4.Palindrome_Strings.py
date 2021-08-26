palindrome_string = input().split()
palindrome = input()

palindromes = [x for x in palindrome_string if x == x[::-1]]
searched_palindrome = palindromes.count(palindrome)

print(palindromes)
print(f"Found palindrome {searched_palindrome} times")