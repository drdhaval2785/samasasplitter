# Execution
`python split.py <wordInSLP1>`

e.g.

`python split.py DavaleSvarapriya`

# output 

`['Davala+ISvara+priya', 'Dava+lA+ISvara+priya']`

Only first 5 output are shown in decreasing probability by default.

If you want all results, replace `print output[:5]` line with `print output`.

# Dictionary

1. As the speed decreases with too many headwords, currently we are using only 'MD' as our base dictionary. If you want to change the dictionary, it can be changed by altering the dictionaryname in `createhwlist('MD')`

2. Only words having >1 length are taken.

3. The dictionary (hwsorted.txt) is sorted in the following logic. 

3.1. In decreasing order of the occurrence in number of dictionaries in sanhw2.txt.
e.g. headword occurring in 29 dictionaries (and therefore more common) are sorted first, then 28, 27,..... 1.

3.2. In decreasing order of length of the words. Longest words are sorted first. Shortest ones at the end.

3.3. If the above two conditions are satisfied, they are sorted in alphabetic order.
