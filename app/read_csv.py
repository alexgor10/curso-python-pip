import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    # print(header)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {k: v for k, v in iterable}
      # print(list(iterable))
      data.append(country_dict)
    return data


if __name__ == '__main__':
  data = read_csv('./app/world_population.csv')
  print(data[0])
