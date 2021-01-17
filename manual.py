from transform import transform
def main():
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