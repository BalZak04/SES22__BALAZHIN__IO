import re


def main():

    line=input(str())
    print(line)
    print(re.sub(r'[.,!?\'\";:]'," ", line))


if __name__ == '__main__':
    main()
