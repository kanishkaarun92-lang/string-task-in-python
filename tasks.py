"""
# count charaters
#with using built in function
a = "hello world"
print(len(a))
# without using built in function
a = "hello world"
count=0
for i in a:
    count = count + 1
print(count)

#Reverse a string
a="python"
print(a[::-1])
#without using bulit in function
a="python"
result=""
for i in a:
    result = i + result
print(result)
#palindrome
a="madam"
print(a[::-1])
#without built in function
a="madam"
rev_string=a
if a==rev_string :
    print("palindrome")
else:
    print("it is not palindrome")
#count vowels
a="interview"
count=0
for i in a:
    if i in "aeiou":
        count = count+1
print(count)

# count consonants
a="coding"
count=0
for i in a:
    if i in "aeiou":
        pass
    else:
        count = count + 1
print(count)
#count digits
a="py123th4"
count=0
for i in a:
    if i.isdigit():
        count=count+1
print(count)

a="python is fun"
count=0
for i in a:
    if i==" ":
        count =count + 1
print(count)
#without using built in function
a="py123th4"
count=0
for i in a:
    if i>= "0" and i<="9":
        count = count + 1
print(count)
#character occurrenc
a="banana"
count=0
target="a"
for i in a:
    if i == target:
        count = count + 1
print(count)
#remove space
a="p y t h o n"
result=""
for i in a:
    if i!=" ":
        result=result+i
print(result)

#Swap case
a="PyThOn"
result=""
for i in a:
    if i>="A" and i<="Z":
        result=result+chr(ord(i)+32)
    else:
         result=result+chr(ord(i)-32)
print(result)

#Count words
a="Data Structure and Algorithm"
total=0
for i in a:
    if i==" ":
        total=total+1
print(total+1)

#longest word
a="Machine learning is powerful"
words=a.split()
longest=""
for i in words:
    if len(i)>len(longest):
        longest = i
print(longest)

#remove duplicate characters
a="programming"
checked=""
for i in a:
    if i in checked:
        print(i)
    else:
        checked=checked + i
print(checked)

#character frequency
a="code"
checked=""
for i in a:
    if i not in checked:
        count = a.count(i)
        print(i,count)
    else:
        checked = checked + i
print(checked)

#fist repeated character
a="programming"
checked=""
for i in a:
    if i in checked:
        print(i)
        break
    else:
        checked = checked+i

# first non repeating character
a = "swiss"
for i in a:
    if a.count(i) == 1:
        print(i)
        break

#anagram check
a="listen"
b="silent"
for i in a:
    if a.count(i) != b.count(i):
        print("Not Anagram")
        break
else:
    print("Anagram")
    
#reverse words
a = "python is easy"
words = a.split()
for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")

#reverse each  word
a = "python is easy"
word = a.split()
result=""
for i in word :
    reversed_word = ""
    for j in i:
        reversed_word = j + reversed_word
    result = result + reversed_word + ""
print(result)

#remove  vowels
a="education"
result=""
for i in a:
    if i  not in "aeiou":
        result = result  + i
print(result)

#string rotaion
a = "ABCD"
b = "CDAB"
if len(a) == len(b) and b in (a + a):
    print("Rotation")
else:
    print("Not Rotation")

#most frequent charcter
a = "success"
max_count = 0
max_char = ""
for i in a:
    if a.count(i) > max_count:
        max_count = a.count(i)
        max_char = i

print(max_char)

# string compression
a = "aaabbc"
result = ""
count = 1
for i in range(1, len(a)):
    if a[i] == a[i-1]:
        count = count + 1
    else:
        result = result + a[i-1] + str(count)
        count = 1

result = result + a[-1] + str(count)

print(result)

#password validation
a="Pass1234"
upper=False
lower=False
digit=False
for i in a:
    if i.isupper():
        upper= True
    if i.islower():
        lower=True
    if i.isdigit():
        digit=True
if len(a)>=8 and upper and lower and digit:
    print("valid password")
else:
    print("invalid password")
"""
#email validation
a = "user@gmail.com"

if "@" in a and "." in a and a.index("@") < a.index(".") and a.index("@") > 0:
    print("Valid Email")
else:
    print("Invalid Email")
