import sys 
from collections import Counter

logs = sys.argv[1]

with open(logs) as f:
  lines = f.readlines()

print("Total lines:", len(lines))

dict = Counter(lines)
for i in lines:
  fields = i.split()
  if len(fields) > 6:
    key = fields[6]
    dict[key] += 1

print("Top 3:")
for i, n in dict.most_common(3):
  print(i, n)