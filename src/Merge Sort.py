
def split_and_merge(a):
    slice_index = len(a) // 2
    l = a[:slice_index]
    r = a[slice_index:]
    if len(l) > 1:
        l = split_and_merge(l)
    if len(r) > 1:
        r = split_and_merge(r)
    return merge_lists(l, r)

def merge_lists(a, b):
    m, n = len(a), len(b)

    l, r = 0, 0
    res = []
    while l < m and r < n:
        if a[l] < b[r]:
            res.append(a[l])
            l += 1
        else:
            res.append(b[r])
            r += 1
    res += a[l:] + b[r:]
    return res


a = [5, 7, 12, 3, 1, 2, 7, 15]


a = split_and_merge(a)

print(a)