from math import sqrt
from table import Table


def welcome():
    print("Welcome to double transposition cipher solver!")


def process_cipher():
    print("Please enter an encrypted text without any punctuation or white spaces:")
    cipher = input()
    return cipher, get_divisors(len(str(cipher)))


def get_divisors(n):
    divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(int(n / i))
    divisors.sort()
    return divisors


def create_tables(cipher, divisors):
    tables = []
    for i in range(len(divisors)):
        tables.append(Table(cipher, divisors[i], divisors[-(i + 1)]))
    return tables


def transpose(transcripts, divisors):
    transpositions = []
    for transcript in transcripts:
        tables = create_tables(transcript, divisors)
        for table in tables:
            transpositions.append(table.get_columnar_transcript())
    return transpositions


def main():
    welcome()
    cipher, divisors = process_cipher()
    tables = create_tables(cipher, divisors)
    transcripts = []
    for table in tables:
        transcripts.append(table.get_columnar_transcript())
    double_transpositions = transpose(transcripts, divisors)
    for transposition in double_transpositions:
        print(transposition)


if __name__ == "__main__":
    main()
