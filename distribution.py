"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

string=input('Please enter a string of text (the bigger the better): ')
characters=list(string)

uppercase=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabet=list('abcdefghijklmnopqrstuvwxyz')

for x in range(len(characters)):
    for n in range(len(uppercase)):
        if uppercase[n]==characters[x]:
            characters[x]=alphabet[n]

frequency=[]
for x in alphabet:
    frequency.append(characters.count(x))

distribution=list(zip(frequency, alphabet))
distribution.sort()

ans=[]
guide=[]
for x in range(0, distribution[-1][0]):
    guide.append(distribution[-1][0]-x)
for x in guide:
    for n in range(len(distribution)):
        if distribution[n][0]==x:
            ans.append(distribution[n])
    
print('The distribution of characters in "{0}" is:'.format(string))

for x in range(len(ans)):
    if ans[x][0]>0:
        print(ans[x][1]*ans[x][0])

