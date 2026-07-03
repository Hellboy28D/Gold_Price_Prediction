from calendar import c
from turtle import color
from utils import *


gold_data = pd.read_csv('gld_price_data.csv')

print(gold_data.head())

print(gold_data.tail())

print(gold_data.shape)

print(gold_data.info())

print(gold_data.isnull().sum())

print(gold_data.describe())


X = gold_data.drop(['Date','GLD'], axis = 1)
Y = gold_data['GLD']