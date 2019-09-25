import csv
import os


def check_tikr_high(directory):
    for filename in os.listdir(directory):
        with open(directory + filename + ".csv" , 'w') as highcsv:
            # print("Reading: {}".format(filename))
            if filename.endswith(".txt"):
                with open(directory + filename, newline='\n') as csvfile:
                    fieldnames = ['tikr', 'date', 'time', 'close', 'high', 'low', 'open', 'vol', '?']
                    reader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)
                    highs = []
                    for row in reader:
                        highcsv.write("{},{}\n".format(row['time'], row['high']))
                        highs.append(float(row['high']))
                while len(highs) > 1:
                    top_of_heap = highs.pop(0)
                    highers = [(high - float(top_of_heap)) / float(top_of_heap) for high in highs if (high - float(top_of_heap)) / float(top_of_heap) >= 0.05]
                    if len(highers) > 0:
                        print(filename)
                        print(max(highers))
                        break
            # print("+" * 50)


def main():
    check_tikr_high(r'.\intra-day-data\01APR\\')


if __name__ == '__main__':
    main()
    print('ALL Done!')
