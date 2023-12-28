import os

from loading_datasets import load_dataset, upload_dataset


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