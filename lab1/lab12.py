import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
df1 = pd.DataFrame({'Spending':[18079, 18594, 19753, 20734, 20831, 23029, 23597, 23584, 25525, 27731, 29449], 'Year':[1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]})
df2 = pd.DataFrame({'Suicide':[5427, 5688, 6198, 6462, 6635, 7336, 7248, 7491, 8161, 8578, 9000],'Year':[1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009] })

plt.plot(df1['Year'], df1['Spending'] )
plt.legend(['Spending'])

plt.plot(df2['Year'], df2['Suicide']) 
plt.legend(['Suicide'])
plt.show()

x = 1999
y = -0.6442*np.power(x, 5) + 6457.3 * np.power(x, 4) - 3 * np.power(10, 7) * np.power(x, 3) + 5 * np.power(10, 10) * np.power(x, 2) - 5 * np.power(10, 13) * x + 2 * np.power(10, 16)
print(y)