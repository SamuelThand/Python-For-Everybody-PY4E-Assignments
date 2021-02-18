#Assignment
#
#Write a program that reads a file and prints the letters in decreasing order of frequency.
#Your program should convert all the input to lower case and only count the letters a-z.
#Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
#Find text samples from several different languages and see how letter frequency varies between languages.
#Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

fhand = open('mbox-short.txt')

letters=dict()
for line in fhand :
    words = line.strip().split()
    for word in words :
        for letter in word :
            if letter.isalpha() :
                letter = letter.lower()
                letters[letter] = letters.get(letter,0) + 1

lst = list()
for k,v in sorted(letters.items()) : lst.append((v,k))
lst = sorted(lst, reverse=True)

for letter in lst :
    print(letter)
