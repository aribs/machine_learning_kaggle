import pandas as pd
pd.set_option('display.max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")


#Ejercicio 1, crea un DataFrame que se vea como:
#Apples Bananas
# 30    21

fruits = pd.DataFrame({'Apples': [30], "Bananas": [21]})
q1.check()
fruits

#Ejercicio 2, crea un datatrame llamado fruit_sales con el siguiente diagrama
#           Apples  Bananas
#2017Sales  35      21
#2018Sales  41      34

fruit_sales = pd.DataFrame({'Apples': [35, 41], "Bananas": [21, 34]}, index=['2017 Sales', '2018 Sales'])
q2.check()
fruit_sales

#Crea la variable ingredients, con una serie que se vea:
#Flour     4 cups
#Milk       1 cup
#Eggs     2 large
#Spam       1 can
#Name: Dinner, dtype: object
ingredients_data = {'Flour': '4 cups',
                    'Milk': '1 cup',
                    'Eggs': '2 large',
                    'Spam': '1 can'}

ingredients = pd.Series(ingredients_data, name='Dinner')

# Check your answer
q3.check()
ingredients

#Read the following csv dataset of wine reviews into a DataFrame called reviews:
#The filepath to the csv file is ../input/wine-reviews/winemag-data_first150k.csv. The first few lines look like:
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)
reviews.head()

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals

#In the cell below, write code to save this DataFrame to disk as a csv file with the name `cows_and_goats.csv`.
filePath = "cows_and_goats.csv"
animals.to_csv(filePath)

