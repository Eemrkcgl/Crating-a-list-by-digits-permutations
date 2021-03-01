from itertools import permutations
def per(x):
    if x<0:
        x=x*(-1)
        result=[]
        list=[]
        y=str(x)
        len_x=len(y)
        for i in y:
            list.append(i)
        perm=permutations(list)
        for i in perm:
            last = ""
            for q in i:
                last+=q
                if len(last)==len_x:
                    if last[0]!="0":
                        result.append(int(last)*(-1))
                    else:
                        continue
        result_last = set(result)
        return result_last
    elif x==0:
        return (0)

    elif x >0:
        result = []
        list = []
        y = str(x)
        len_x = len(y)
        for i in y:
            list.append(i)
        perm = permutations(list)
        for i in perm:
            last = ""
            for q in i:
                last += q
                if len(last) == len_x:
                    if last[0] != "0":
                        result.append(int(last))
                    else:
                        continue
        result_last=set(result)
        return result_last