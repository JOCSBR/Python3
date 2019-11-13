#modules 2

import random

# mylist = {'colors': ['blue','yellow','red','green','black'], 'side':
# ['left','right','upper','lower'], 'size': ['small','medium','large','xlarge']}
# # print(mylist)
# crlist = list(mylist)
# print(crlist)
# print('\n')
# subject = random.choice(list(mylist))
# correct = random.choice(mylist[subject])
# print(subject, correct)


listnames = ['paul','peter','mary','john','lois']
selname = random.choice(listnames)
selthree = random.sample(listnames, 3)
print(listnames)
print(selname)
print(selthree)


# jogo = []
# while len(jogo) < 6:
#     num = random.randint(1,60)
#     if num in jogo:
#         continue
#     else:
#         jogo.append(num)
# print(sorted(jogo))
    