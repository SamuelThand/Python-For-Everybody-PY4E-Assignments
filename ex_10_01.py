#Assignment
#
#Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
#Count the number of messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
#Then sort the list in reverse order and print out the person who has the most commits.
#
#Solution


name = input('Enter file name: ')
if len(name) < 1 : name = 'mbox-short.txt'
fhand = open(name)

doms = dict()
for line in fhand :
    if 'From ' not in line :
        continue
    words = line.split()
    email = words[1].split('@')
    person = email[0]
    doms[person] = doms.get(person,0) + 1

lst = list()
for key, val in list(doms.items()) :
    lst.append((val, key))

lst.sort(reverse=True)

print(lst[0])
