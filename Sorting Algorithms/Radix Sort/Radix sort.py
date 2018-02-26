class radixSort:
    def decimalSort( List ):
        maxLength = False
        placement = 1
        while not maxLength:
            # Initilize variables
            maxLength = True
            bins = [[]for i in range(10)]
            # split List between bins
            for i in List:
                tmp = i // placement
                bins[tmp % 10].append(i)
                if maxLength and tmp > 0:
                    maxLength = False
            # empty bins back into List array
            a = 0
            for b in range(10):
                bin = bins[b]
                for i in bin:
                    List[a] = i
                    a += 1
            # move to next digit
            placement *= 10

# Main
# Reading the file into list as ints for Decimal
decimal = open('random_numbers10.txt', 'r')
numbers = decimal.readlines()
numbers = [int(i) for i in numbers]
decimal.close()

# Reading the file into list as ints for Hexdecimal
hexadecimal = open('random_numbers4.txt', 'r')
hexNumbers = hexadecimal.readlines()
hexNumbers = [int(i,16)for i in hexNumbers]
hexadecimal.close()

# Reading the file into list as ints for Octal
octal = open('random_numbers3.txt', 'r')
octalNumbers = octal.readlines()
octalNumbers = [int(i,8)for i in octalNumbers]
octal.close()

# Methods
radixSort.decimalSort(numbers)
radixSort.decimalSort(hexNumbers)
radixSort.decimalSort(octalNumbers)

# Testing
# Decimal
for i in numbers:
    print(i)
# Hex
for i in hexNumbers:
    print(hex(i))
# Octal
for i in octalNumbers:
    print(oct(i))
