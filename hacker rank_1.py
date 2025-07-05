def print_rangoli(size):
    # Create a list of lowercase letters a-z
    l1 = list(map(chr, range(97, 123)))
    # Create the widest row (e.g., for n=3: c-b-a-b-c)
    x = l1[size-1::-1] + l1[1:size]
    # Calculate the width of the rangoli
    m = len('-'.join(x))
    # Upper half of the rangoli
    for i in range(1, size):
        print('-'.join(l1[size-1:size-i:-1] + l1[size-i:size]).center(m, '-'))
    # Full rangoli including the middle row and lower half
    for i in range(size, 0, -1):
        print('-'.join(l1[size-1:size-i:-1] + l1[size-i:size]).center(m, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)