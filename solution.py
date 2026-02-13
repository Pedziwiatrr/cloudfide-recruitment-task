import pandas as pd


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    empty_df = pd.DataFrame([])
    print(f"df: {df}")
    print(f"role: {role}")
    print(f"new_column: {new_column}")
    print()

    def is_valid(label):
        if not isinstance(label, str) or len(label) == 0:
            return False
        for char in label:
            if not (char.isalpha() or char == "_"):
                return False
        return True

    if not is_valid(new_column) or not isinstance(role, str):
        return empty_df

    for col in df.columns:
        # print(f"col: {col}")
        if not is_valid(col):
            return empty_df

    operator = None
    for op in ["+", "-", "*"]:
        if op in role:
            operator = op
            break
    if operator is None:
        return empty_df

    role_split = role.split(operator)
    print(f"splitted role: {role_split}")
    if len(role_split) != 2:
        return empty_df

    col1 = role_split[0].strip()
    col2 = role_split[1].strip()
    print(f"col1: {col1}, col2: {col2}")

    if not (
        is_valid(col1) and is_valid(col2) and col1 in df.columns and col2 in df.columns
    ):
        return empty_df

    result_df = df.copy()

    if operator == "+":
        result_df[new_column] = result_df[col1] + result_df[col2]
    elif operator == "-":
        result_df[new_column] = result_df[col1] - result_df[col2]
    elif operator == "*":
        result_df[new_column] = result_df[col1] * result_df[col2]

    return result_df
