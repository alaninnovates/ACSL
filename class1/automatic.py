from prettytable import PrettyTable
from transform import transform

def getFile(fname):
    f = open(fname)
    read = f.read()
    arr = read.split('\n')
    return arr

def main():
    '''
    expectedf = open('./expected.txt')
    expected = expectedf.read()
    expectedArray = expected.split('\n')
    f = open('./one.txt')
    testCases = f.read()
    testCasesArray = testCases.split('\n')
    '''
    expectedArray = getFile('./expected.txt')
    testCasesArray = getFile('./one.txt')

    table = PrettyTable()
    table.field_names = ['Test Case', 'Result', 'Expected', 'Success']
    for i in range(len(testCasesArray)):
        case = testCasesArray[i]
        expect = expectedArray[i]
        npd = case.split(' ')
        result = transform(npd[0], int(npd[1]), int(npd[2]))
        success = False
        if result == expect:
            success = True
        table.add_row([case, result, expect, success])
        # print(case, ' results in: ', result)
    print(table)
'''
for i in range(5):
    # Read the input set
    input_set = input('> ').strip()
    iset = input_set.split()
    n = iset[0]
    p = int(iset[1])
    d = int(iset[2])

    # Hand it over to subroutine
    result = transform(n, p, d)
    print(result)
'''