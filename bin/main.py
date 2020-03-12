import requests
import datetime
import os
from bs4 import BeautifulSoup

class GasPriceScraper:
  URL = 'https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm'
  OUTPUT_DIR = 'output/'
  OUTPUT_DAILY = OUTPUT_DIR + 'henry_hub_gas_daily_prices.csv'
  OUTPUT_MONTHLY = OUTPUT_DIR + 'henry_hub_gas_monthly_prices.csv'

  def __init__(self):
    self.dataset = []
    self.html = None
    self.data_node = None
  
  def daily_prices_csv(self):
    self.__run()

    if self.__file_already_exit(self.OUTPUT_DAILY):
      print(self.OUTPUT_DAILY, 'already exit and will be overwritten! \n')
    
    with open(self.OUTPUT_DAILY, 'w') as csv_handle:
      csv_handle.write('date,price\n')
      for day in self.dataset:
        if day[-1] != '' and day[-1] != 'NA':
          csv_handle.write(','.join(day))
          csv_handle.write('\n')
      
    print('Done! ')
    print('Open', os.path.join(os.getcwd(), self.OUTPUT_DAILY))

  def monthly_prices_csv(self):
    self.__run()

    if self.__file_already_exit(self.OUTPUT_MONTHLY):
      print(self.OUTPUT_MONTHLY, 'already exit and will be overwritten! \n')
    
    with open(self.OUTPUT_MONTHLY, 'w') as csv_handle:
      csv_handle.write('date,price\n')
      prev_day = self.dataset[0]

      for day in self.dataset:
        print(day)
        if self.__to_day(day) > self.__to_day(prev_day):
          if prev_day[1] != '' and prev_day[1] != 'NA':
            csv_handle.write(prev_day[0] + ',' + prev_day[1])
            csv_handle.write('\n')
        prev_day = day
      
    print('Done! ')
    print('Open', os.path.join(os.getcwd(), self.OUTPUT_MONTHLY))

  def __to_day(self, day):
    return int(day[0].split('-')[-1])

  def __run(self):
    if len(self.dataset) == 0:
      self.__load_page()
      self.__extract_data_node()
      self.__extract_data()

  def __load_page(self):
    try:
      req = requests.get(self.URL)
      if req.status_code == 200:
        self.html = req.content
        print('HTML document fetched...')
      else:
          print('An error occured with the server...')
    except Exception as e:
      print('Unknown network error...', e)

  def __extract_data_node(self):
    html_node = BeautifulSoup(self.html, 'html5lib')
    self.data_node = html_node.find(summary="Henry Hub Natural Gas Spot Price (Dollars per Million Btu)")
 
  def __extract_data(self):
    dataset = []
    for node in self.data_node.find_all('tr'):
      date_node = node.find('td', {'class': 'B6'})
      if date_node:
        date = date_node.string.replace('\xa0\xa0', '')
        dataset.append([date, *[val.text for val in node.find_all('td', {'class': 'B3'})]])
    self.dataset = self.__format_prices(dataset)
    self.dataset.reverse()

  def __format_prices(self, dataset):
    combined = []
    for week in dataset:
      start_date = self.__normalize_start_date(week[0])
      day_offset = 0
      for daily_price in week[1:]:
        day = start_date + datetime.timedelta(days = day_offset)
        combined.append([day.strftime("%Y-%m-%d"), daily_price])
        day_offset += 1
    return combined

  def __normalize_start_date(self, string):
    start_date = string.replace('- ',' ').replace('-', ' ').split(' ')[0:3]
    return datetime.datetime.strptime('-'.join(start_date), '%Y-%b-%d')

  def __file_already_exit(self, filename):
    return os.path.exists(filename)
  

def main():
  g = GasPriceScraper()
  g.daily_prices_csv()
  g.monthly_prices_csv()
  

if __name__ ==  '__main__':
  main()