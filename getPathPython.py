
# Print dict recursively 
def recPrint(s, pt):
    for k, v in s.items():
        if isinstance(v, dict):
            recPrint(v, pt)
            pt.insert(len(pt) - len(pt) + 2, k)
            if len(v) == 1:
                pt.insert(len(pt) - len(pt) + 2, list(v)[0]) # sort it in order (dir1, dir2, dir3 ...)

    return pt

def biggestPath(**p):
    if len(p) == 1:
        ans = ""
        # finding dublicates
        for i in set(list(p.values())[0]):
            c = 0
            for j in list(p.values())[0]:
                if i == j:
                    c += 1
            if c == 1:
                ans = i
        
        if ans != "":
            return "/" + list(p.keys())[0] + "/" + ans
        else:
            return "/"    

    c = 0
    pat = {}
    pt = ["root"]
    for i in p:
        aim = p.get(i)
        if len(aim) > c:
            pat = aim
            c = len(aim)
            pt[0] = i

    pt.append(list(pat.keys())[0])
    ans = recPrint(pat, pt)

    ans1 = ""

    for i in ans:
        ans1 += "/" + i

    if len(ans1) > 255:
        return "Length 255 error"

    return ans1

d1 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}
d2 = {'dir1': ['file1', 'file1']}
d3 = {'dir1': ['file1', 'file2', 'file2']}

print(biggestPath(**d1))
