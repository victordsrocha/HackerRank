from itertools import groupby

s = input()
data = list(str(s))
res = ''
groups = []
for k, g in groupby(data, lambda x: x):
    new_group = list(g)
    res += '({}, {}) '.format(len(new_group), new_group[0])
res = res[:-1]
print(res)
