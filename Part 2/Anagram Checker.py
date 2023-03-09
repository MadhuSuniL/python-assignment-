def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

s1 = input('Enter 1st string:')
s2 = input('Enter 2nd string:')

print(is_anagram(s1, s2))

