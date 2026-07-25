import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    new = {'id':'student_id', 'first':'first_name', 'last':'last_name', 'age':'age_in_years'}
    students.rename(columns = new, inplace = True)
    return students