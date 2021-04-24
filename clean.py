import csv

def main():
    first = 'data/first_names.all.csv'
    last = 'data/last_names.all.csv'
    password = 'data/passwords.txt'

    outfile = 'lists/data.csv'
    
    print("Starting to clean data...")
    data = normalize_lists(100000, clean_first(first), clean_last(last), clean_passwords(password))
    save_to_file(outfile, data)

def clean_passwords(file):
    print("Cleaning passwords...")
    passwords = []
    with open(file) as f:
        for row in f:
            row = row.rstrip()
            if len(row) > 7:
                passwords.append(row)

    return passwords

def clean_first(file):
    print("Cleaning first names...")
    firsts = []
    with open(file) as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if row[0].isalpha() and row[0].isascii():
                firsts.append(row[0])
    
    return firsts

def clean_last(file):
    print("Cleaning last names...")
    lasts = []
    with open(file) as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if row[0].isalpha() and row[0].isascii():
                lasts.append(row[0])
    
    return lasts

def normalize_lists(n, first, last, password):
    maxn = 0
    maxn = len(first)
    if len(last) > maxn:
        maxn = len(last)
    if len(password) > maxn:
        maxn = len(password)

    if maxn < n:
        n = maxn

    first = first[0:n]
    last = last[0:n]
    password = password[0:n]

    return first, last, password

def save_to_file(outfile, outdata):
    final = []

    for i, _ in enumerate(outdata[0]):
        final.append([outdata[0][i], outdata[1][i], outdata[2][i]])

    with open(outfile, 'w') as f:
        csvwriter = csv.writer(f)
        for row in final:
            csvwriter.writerow(row)

if __name__ == '__main__':
    main()