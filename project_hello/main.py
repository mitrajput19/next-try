def p1():
  print('''
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 
# Create a dataframe
df = pd.DataFrame({'x': [10, 38, 5, 7, 300, 11, 113, 165, 17, 19],
          'y': [28, 4, 6, 8, 10, 122, 14, 16, 158, 200]})
#Create a joint plot with a kernel density estimate (KDE) and a scatter plot
sns.jointplot(x='x', y='y', data=df, kind='kde').plot_joint(sns.scatterplot)
plt.show()
''')
