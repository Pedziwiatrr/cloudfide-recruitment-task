import pandas as pd


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    empty_df = pd.DataFrame([])
    print(f"df: {df}")
    print(f"role: {role}")
    print(f"new_column: {new_column}")
    print()

    def is_valid(label):
        if len(label) == 0 or not isinstance(label, str):
            return False
        for char in label:
            if not (char.isalpha() or char == "_"):
                return False
        return True

    if not is_valid(new_column) or not isinstance(role, str):
        return empty_df

    for col in df.columns:
        print(f"col: {col}")
        if not is_valid(col):
            return empty_df

    return empty_df
