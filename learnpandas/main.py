from pandas import DataFrame
data = {
    "name": ["John", "Jane", "Jade"],
    "age": [2, 10, 3]
    }

# get number of rows len()
def get_row_count():

    df = DataFrame(data)
    print(f"Number of rows is {len(df)}")
    return df