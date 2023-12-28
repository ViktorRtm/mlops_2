import sys
import os
import pandas as pd
import numpy as np
import tqdm


from loading_datasets import load_dataset, upload_dataset


X_COLUMNS = ['animal_id','lactation', 'calving_date', 'farm', 'farmgroup', 'birth_date', 'milk_yield_1', 'milk_yield_2', 'mother_id']
Y_COLUMNS = ['milk_yield_3', 'milk_yield_4', 'milk_yield_5', 'milk_yield_6', 'milk_yield_7', 'milk_yield_8', 'milk_yield_9', 'milk_yield_10']


in_train_path = os.path.join('data', 'train.csv')
in_pedigree_path = os.path.join('data', 'pedigree.csv')
out_train_path = os.path.join('data', 'stage1', 'train.csv')
os.makedirs(os.path.join('data', 'stage1'), exist_ok=True)

train_df = load_dataset(in_train_path)
cow_pedigree = load_dataset(in_pedigree_path)

for item in train_df.columns:
    train_df.loc[train_df[item].isna(), item] = 0

train_df = train_df.merge(cow_pedigree[['animal_id', 'mother_id']], 
                                        on='animal_id', 
                                        how='left')

upload_dataset(train_df, out_train_path)