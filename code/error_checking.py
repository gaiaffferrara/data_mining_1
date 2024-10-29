import pandas as pd


def start_endyear (df : pd.DataFrame) -> pd.Series:
    df.loc[df['startYear'].isna()]
    return