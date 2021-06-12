### import

import pandas as pd
import os
from os import listdir
from os.path import isfile, join

## firts, you need read one excel with the name the actual files in the first column and the second column with the new name

archivo = '/documents/name_excel.xlsx'

## Verify the name sheet

df = pd.read_excel(archivo, sheet_name='sheet1')


#Path of the files
path_name = 'Documents/files'


## Count total files to change and print
## You need the change the name in the dataframe, depend of name column


n = df['Name_first_column_excel'].count()
print(n)

def change_func():

    for i in range(n):

        ## before name file
        before = "{r}/{name}.{type}".format(r = path_name, name = df['Name_first_column_excel'][i], type = 'pdf' )
        ## new name file
        new = "{r}/{name}.{type}".format(r = path_name, name = df['Name_second_column_excel'][i], type = 'pdf' )
        os.rename(before, new)
        print('name change')

print(change_func())


