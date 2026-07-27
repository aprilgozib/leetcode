import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered_df = animals[animals['weight'] >= 100].sort_values(by = 'weight', ascending = False)[['name']]
    return filtered_df