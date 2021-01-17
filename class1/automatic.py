from prettytable import PrettyTable
def transform(nstr, pos, dnum):
    # print(nstr, pos, dnum)
    # array of n
    newN = list(nstr)
    # get the digit at "pos" from last element of newN
    # (counting from last digit backwards)
    posIndex = len(newN) - pos
    posValue = int(newN[posIndex])
    # print(posValue, posIndex)

    if posValue in range(0, 4+1):
        # print('one')
        sum = posValue+dnum
        # make an array of sum
        s = list(str(sum))
        # find the ones place digit (last digit) of sum
        uniDig = s[len(s)-1]
        # set the digit at "pos" to the last digit of "sum"
        newN[posIndex] = uniDig
        # loop from the "pos" position from the right to the end of the array
        for digit in range(posIndex + 1, len(newN)):
            newN[digit] = '0'
        # join the new array of numbers and return it
        newVal = ''.join(newN)
        return newVal

    elif posValue in range(5, 9+1):
        # print('two')
        # get absolute value
        abv = abs(posValue-dnum)
        # make an array of abv
        s = list(str(abv))
        # find the ones place digit (last digit) of sum
        firDig = s[0]
        # set the digit at "pos" to the last digit of "sum"
        newN[posIndex] = firDig
        # loop from the "pos" position from the right to the end of the array
        for digit in range(posIndex + 1, len(newN)):
            newN[digit] = '0'
        # join the new array of numbers and return it
        newVal = ''.join(newN)
        return newVal

#def main():
expectedf = open('./class1/expected.txt')
expected = expectedf.read()
expectedArray = expected.split('\n')
f = open('./class1/one.txt')
testCases = f.read()
testCasesArray = testCases.split('\n')
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