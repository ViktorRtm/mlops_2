import pandas as pd


def load_dataset(dataset_path: str) -> pd.DataFrame:
    return pd.read_csv(dataset_path)


def upload_dataset(df: pd.DataFrame, dataset_path: str) -> pd.DataFrame:
    return df.to_csv(dataset_path, index=False)


# def load_test_dataset(dataset_path: str) -> pd.DataFrame:
#     return pd.read_csv(dataset_path, index_col='Unnamed: 0')


# def load_pedigree(dataset_path: str) -> pd.DataFrame:
#     return pd.read_csv(dataset_path)