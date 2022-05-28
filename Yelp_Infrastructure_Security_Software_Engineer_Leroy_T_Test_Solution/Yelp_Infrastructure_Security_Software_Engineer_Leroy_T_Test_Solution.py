#Yelp software engineer interview 1
import fileinput
from collections import defaultdict

class Business(object):

    def __init__(self, name, location, id):
        self.name = name
        self.location = location
        self.id = id

class Chain(object):

    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

def detect_and_order_chain_businesses(businesses, location):
  idCheck, chain, count = [], [], []
  for i in businesses:
    if i.location == location and i.id not in idCheck:
      #print(i.name, i.location, i.id)
      idCheck.append(i.id)
      if i.name not in count:
        chain.append(Chain(i.name, 0))
      count.append(i.name)
  for j in chain:
    j.frequency = str(count.count(j.name))
  return sorted(chain, key=lambda x: x.frequency,reverse=True)
  
def parse_stdin_and_get_input():
  with open('input.txt') as f:
    lines = [line.strip() for line in list(f)]
  businesses = []
  target_location = lines[-1]

  for line in lines[:-1]:
      name, location, id = line.split(' - ')
      businesses.append(Business(name, location, id))

  return businesses, target_location

if __name__ == '__main__':
    businesses, location = parse_stdin_and_get_input()

    chains = \
        detect_and_order_chain_businesses(businesses, location)

    for chain in chains:
        print('{} - {}'.format(chain.name, chain.frequency))