"""
analyze.py

Svita Kiran
Fall 2023
9/27/23
CS152 Lab 3

python3 analyze.py

"""
import sys
import stats

def main(filename, column_id):

# assign to fp the result of opening the file hurricanes.csv for reading
    fp = open(filename, 'r')
# assign to line the first line of the data file
    line = fp.readline()
# assign to headers the result of splitting the line using commas
    headers = line.split(",")
# print headers
    print(headers)

# assign to a list variable named data an empty list
    data = []

# for all of the remaining lines in the file
    for line in fp:
  # assign to items the result of splitting the line using commas
        items = line.split(",")
  # append the second item to data (which index?) items cast as a float
        data.append(float(items[column_id]))
    # close the data file
    fp.close()
    # print data
    print(data)

    sum = stats.sum(data)
    mean = stats.mean(data)
    var = stats.variance(data)
    min = stats.min(data)
    max = stats.max(data)
    print(f"{sum :.2f}")
    print(f"{mean :.2f}")
    print(f"{var :.2f}")
    print(f"{min :.2f}")
    print(f"{max :.2f}")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))