import pandas as pd
import numpy as np
from plotnine import *

df = pd.read_csv('https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')

df = df[['Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', 'Country Name']]
df.head()

(ggplot(df, aes(x='Mortality rate, infant (per 1,000 live births)', y='GDP per capita (constant 2010 US$)')) + geom_point())

# made some changes after PR 