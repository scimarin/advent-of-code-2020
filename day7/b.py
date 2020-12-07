#!/usr/bin/python3

class Bag:
  def __init__(self, kind, number):
    self.kind = kind
    self.number = int(number)

  def __repr__(self):
    return ' '.join([self.number, self.kind])

graph = {}

with open('input.txt', 'r') as fin:
  for line in fin.readlines():
    root_bag = line[:line.find('bag')].strip()
    root_bag = Bag(root_bag, 1)

    if root_bag not in graph:
      graph[root_bag.kind] = []

    contents = [i[:i.find('bag')].strip() for i in line[line.find('contain')+len('contain'):].split(',')]
    for content in contents:
      if 'no other' in content:
        continue
      number, kind = content.split(' ', 1)
      bag = Bag(kind, number)

      graph[root_bag.kind].append(bag)

# how many other bags does root_bag contain
def contains(root_bag):
  ans = 0
  for bag in graph[root_bag]:
    if graph[bag.kind] == []:
      ans += bag.number
    else:
      ans += bag.number + bag.number * contains(bag.kind)
  return ans

ans = contains('shiny gold')
print(ans)
