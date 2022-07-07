
def get_cs():
    """get string input"""
    cs = input("Enter a string")
    return cs


def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    ls = cs.split()
    d=dict()
    i=0
    for word in ls:
        d[i]=word
        i+=1
    return d
def dict_to_cs(d):
    """convert a dictionary to connect string"""
    i=0
    cs=""
    for i in d:
        if i<len(d):
            cs+=d[i]+" "
            i=i+1
    return cs

def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
