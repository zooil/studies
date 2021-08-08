import json
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

path = 'datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)
print(frame['a'][1])
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
print(results.value_counts()[:8])

#frame.info()

"""
tz_counts = frame['tz'].value_counts()
cl_tz = frame['tz'].fillna('Missing')
cl_tz[cl_tz == ''] = 'Unknown'
tz_counts = cl_tz.value_counts()
tz_counts[:10].plot(kind='barh', rot=0)
plt.show()
"""

cframe = frame[frame.a.notnull()]
import numpy as np
os = np.where(cframe['a'].str.contains('Windows'),'windows', 'Not windows')
print(os[:5])
by_tz_os = cframe.groupby(['tz', os])
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])

indexer = agg_counts.sum(1).argsort()
indexer[:10]
count_subset = agg_counts.take(indexer)[-10:]
count_subset
count_subset.plot(kind='barh', stacked=True)
!vi usa_gov.py
#plt.show()

normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
#plt.show()

