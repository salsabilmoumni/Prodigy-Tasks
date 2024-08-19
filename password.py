import string

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation

def checker(password):
    score = 0
    contains_upper_case = any(char in upper_case for char in password)
    contains_lower_case = any(char in lower_case for char in password)
    contains_digits = any(char in digits for char in password)
    contains_special_characters = any(char in special_characters for char in password)
    
    if contains_upper_case:
        score += 1
    if contains_lower_case:
        score += 1
    if contains_digits:
        score += 1
    if contains_special_characters:
        score += 1
    
    length = len(password)
    if length == 8:
        score += 1
    elif length > 8:
        score += 2

    if score == 6:
        print('Strong password')
    elif 4 < score < 6:
        print('Good password')
    else:
        print('Weak password')
    
    return score

print()
print("****** Password Checker Program ******")
print()

password = input('Enter your password: ')
print()

result = checker(password)
print(f'Your password score is: {result}')


