
'''
This program counts the distribution of the hour of the day for each of the messages.
You can pull the hour from the “From” line by finding the time string and
then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts,
one per line, sorted by hour as shown below.

   python timeofday.py
   Enter a file name: mbox-short.txt
   04 3
   06 1
   07 1
   09 2
   10 3
   11 6
   14 1
   15 2
   16 4
   17 2
   18 1
   19 1
'''

fhand = open('mbox-short.txt')

d=dict()
for line in fhand :
    if not line.startswith('From ') :
        continue
    words=line.split()
    hsplit = words[5].split(':')
    for word in hsplit[0:1] :
        d[word] = d.get(word,0) + 1

for k,v in sorted(d.items()) :
    print(k,v)
