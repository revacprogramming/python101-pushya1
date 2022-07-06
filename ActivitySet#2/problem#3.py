

def get_cs():
    """get string input"""
    cs=input("Enter a string:")
    return cs


def cs_to_lot(cs):
    """convert connected string to list of strings"""
    ls=cs.split()
    return ls


def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
