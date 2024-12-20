import pandas as pd
import numpy as np

# clear outliers by column
def clear_outliers_iqr(df: pd.DataFrame, column:str) -> pd.DataFrame:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df = df[~((df[column] < lower_bound) | (df[column] > upper_bound))]
    return df

if __name__ == "__main__":
    df = pd.read_csv('Diabetes_Final_Data_Cleaned.csv')
    df = clear_outliers_iqr(df, 'bmi')
    df.to_csv('Diabetes_Final_Data_Cleaned.csv', index=False)
    
    
class DataAgent:
    '''
    #### The DataAgent's methods:
    
    - `clear_outliers_iqr`: clear outliers (both by column)
    
    - 
    '''
    def __init__(self, whisker_length = 1.5):
        self.whisker_length = whisker_length
    
    def clear_outliers_iqr(self, df:pd.DataFrame, col:str) -> pd.DataFrame:
        '''
        #### clear data statistically by one column only
        '''
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - self.whisker_length * iqr
        upper_bound = q3 + self.whisker_length * iqr
        df = df[~((df[col] < lower_bound) | (df[col] > upper_bound))]
        return df
    
    # 