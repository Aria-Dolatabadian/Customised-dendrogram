import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
df = pd.read_csv (r'Species.csv')
print (df)
df = df.set_index('Species')
Z = hierarchy.linkage(df, 'ward')
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=8, labels=df.index)
plt.show()
