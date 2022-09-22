import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    f = open(csv_file_path)
    
    csvreader = csv.reader(f)
    res = []
    for row in csvreader:
        for i in range(len(row)):
            if type(int(row[i])) == int:
                row[i] = int(row[i])
            else:
        res.append(row)
                

    return res
