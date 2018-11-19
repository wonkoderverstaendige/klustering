# creating empty dictionary

bata = {}   

data = dict()

# dictionary with initial content

gata = { 'x':1, 'y': 2, 'z': 3 }

# add single value 

bata.update({'a':1})
data.update({'b':2})

# print(bata)
# print(data)
# OR
bata['b']=2
data['b']=2

# print(bata)
# print(data)
# OR
bata.update(dict(b=3))
data.update(dict(c=3))
# print(bata)
# print(data)
# OR
bata.update(d=4)
data.update(d=4)
# print(bata)
# print(data)
# print(gata)


# merging dictionaries
dbata = {}
dbata.update(data)
dbata.update(gata)
print(dbata)

# deleting items 

# clear entire zata.clear()


# check if the dictionary is empty or not
my_dict = {}

if not bool(my_dict):
    print("Pustka, Panie Dzieju!")
    
channel_groups = {0: {'channels': [13, 14, 15, 28],
     'description': {13: 'tetrode',
                     14: 'tetrode',
                     15: 'tetrode',
                     28: 'tetrode'},
     'geometry': {13: (1.25, 0.25),
                  14: (1.25, -0.25),
                  15: (0.75, 0.25),
                  28: (0.75, -0.25)},
     'graph': [(13, 14), (13, 15), (13, 28), (14, 15), (14, 28), (15, 28)]},
 1: {'channels': [11, 12, 29, 30],
     'description': {11: 'tetrode', 12: 'dead', 29: 'dead', 30: 'tetrode'},
     'geometry': {11: (1.25, 0.25),
                  12: (1.25, -0.25),
                  29: (0.75, 0.25),
                  30: (0.75, -0.25)},
     'graph': [(11, 12), (11, 29), (11, 30), (12, 29), (12, 30), (29, 30)]},
 2: {'channels': [0, 9, 10, 31],
     'description': {0: 'tetrode', 9: 'tetrode', 10: 'tetrode', 31: 'tetrode'},
     'geometry': {0: (1.25, 0.25),
                  9: (1.25, -0.25),
                  10: (0.75, 0.25),
                  31: (0.75, -0.25)},
     'graph': [(0, 9), (0, 10), (0, 31), (9, 10), (9, 31), (10, 31)]},
 3: {'channels': [1, 2, 3, 8],
     'description': {1: 'tetrode', 2: 'tetrode', 3: 'dead', 8: 'tetrode'},
     'geometry': {1: (1.25, 0.25),
                  2: (1.25, -0.25),
                  3: (0.75, 0.25),
                  8: (0.75, -0.25)},
     'graph': [(1, 2), (1, 3), (1, 8), (2, 3), (2, 8), (3, 8)]},
 4: {'channels': [4, 5, 6, 7],
     'description': {4: 'tetrode', 5: 'tetrode', 6: 'tetrode', 7: 'tetrode'},
     'geometry': {4: (1.25, 0.25),
                  5: (1.25, -0.25),
                  6: (0.75, 0.25),
                  7: (0.75, -0.25)},
     'graph': [(4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7)]},    
    
print("key value count")
for count, key, value in enumerate(channel_groups.items(),1):
    print(key,'    ',value,'    ', count)
    
