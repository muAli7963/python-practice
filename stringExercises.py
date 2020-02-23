# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('test'))  # ---> tes$

# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('drink', 'eat'))

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
 
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('js'))
print(add_string('jskjsjk'))
print(add_string('playing'))


#Write a Python function that takes a list of words and returns the length of the longest one.

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["python", "Exercises", "Backend"]))

#Write a Python program to remove the nth index character from a nonempty string.

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))

#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('abcd'))


#Write a Python program to remove the characters which have odd index values of a given string.

def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('python'))

#Write a Python program to count the occurrences of each word in a given sentence.

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the brown pear slap the white pear on his face lolol lolol'))

#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

print(to_uppercase('Python'))
print(to_uppercase('PyThon'))



