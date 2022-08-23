import pandas as pd
from pyspark.sql.types import IntegerType, FloatType, StringType, DateType


def spark_rename_column(df, col_name, col_type):
    '''This function changes the type of a given column using the withColumn method in Spark'''
    if col_type == 'str':
        return df.withColumn(col_name, df[col_name].cast(StringType()))                
    elif col_type == 'int':
        return df.withColumn(col_name, df[col_name].cast(IntegerType()))
    elif col_type == 'float':
        return df.withColumn(col_name, df[col_name].cast(FloatType()))
    elif col_type == 'date':
        return df.withColumn(col_name, df[col_name].cast(DateType()))
    else:
        print("Unable to cast {} column to {} type.".format(col_name, col_type))
        
        
def pandas_rename_column(df, col_name, col_type):
    '''This function changes the type of a given column using the withColumn method in Spark'''
    if col_type in ['str', 'int', 'float']:
        try:
            return df[col_name].astype(col_type)
        except pd.errors.IntCastingNaNError:
            return df[col_name].fillna(0).astype('int')
    elif col_type == 'date':
        return pd.to_datetime(df[col_name])
    else:
        print("Unable to cast {} column to {} type.".format(col_name, col_type))