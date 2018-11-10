import pathlib
import random

with open('sherlock.txt', 'r') as infile:
    book = infile.read()
    book = book.replace('\n', ' ')
    book = book.replace('--', ' ')
    words = book.split(' ')
    # for x in range(len(words)):
    #     words[x] = words[x].lower()
d={}
for i in range(len(words)-2):
    if (words[i]+ ' ' + words[i+1]) in d:
        d[words[i]+ ' ' + words[i+1]].append(words[i+2])
    else:
        d[words[i]+ ' ' + words[i+1]] = [words[i+2]]

def start_sen():
    starter = ' '
    while starter[0].isupper() == False:
        starter = random.choice(list(d.keys()))
    return starter

sentences = 0
para = 0
story = start_sen()
#next_sen=random.choice(list(d.keys()))

while para < 4:
    while sentences < 5:
        if story[-1] == '.':
            sentences += 1
            if sentences == 5:
                para +=1
                sentences = 0
                if para == 4:
                    break
                else:
                    story = story +"\n\n " + start_sen()
            else:
                story = story + ' ' + start_sen()
        else:
            part = story.split(' ')
            story = story +' ' + random.choice(d[part[-2] + ' ' + part[-1]])

print(story)
