def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]

def every_other(seq):
    return seq[::2]

def first_last_every_other(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def mid_last_first(seq):
    third = len(seq)//3
    first = seq[:(third)]
    mid = seq[third:(third*2)]
    last = seq[(third*2):]
    return mid+last+first


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
longer_tuple = (1,2,3,"cutoff", 0,1,2,3,4,5,"cutoff",3,2,1)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
assert every_other(a_string) == 'ti sasrn'
assert every_other(a_tuple) == (2, 13, 5)
assert first_last_every_other(a_string) == ' sas'
assert first_last_every_other(longer_tuple) == (0, 2, 4)
assert reverse(a_string) == 'gnirts a si siht'
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)