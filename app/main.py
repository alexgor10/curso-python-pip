import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('./app/world_population.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))

  charts.generate_pie_chart('bar',countries, percentages)
  
  country = input('Type country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    countryDict = result[0]
    labels, values = utils.get_population(countryDict)
    charts.generate_bar_chart(country,labels, values)
  


if __name__ == '__main__':
  run()
