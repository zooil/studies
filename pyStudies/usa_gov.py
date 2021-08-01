import json
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

path = 'datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
cl_tz = frame['tz'].fillna('Missing')
cl_tz[cl_tz == ''] = 'Unknown'
tz_counts = cl_tz.value_counts()
tz_counts[:10].plot(kind='barh', rot=0)
plt.show()
