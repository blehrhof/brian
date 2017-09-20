def main():
    names=['a','b','c']
    newname=input('what is the new name? ')
    names.append(newname)
    printnames(names)
    return

def printnames(list):
    for name in list:
        print(name)
    return

main()
