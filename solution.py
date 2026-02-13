import pandas as pd


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """
    Adds a new column to the DataFrame based on operator parsed in the 'role' string.
    Possible operators: ['+', '-', '*']
    Returns empty df if validation fails at any point.
    """
    empty_df = pd.DataFrame([])

    def is_valid(label):
        # only letters and underscores allowed
        if not isinstance(label, str) or len(label) == 0:
            return False
        for char in label:
            if not (char.isalpha() or char == "_"):
                return False
        return True

    if not is_valid(new_column) or not isinstance(role, str):
        return empty_df

    for col in df.columns:
        if not is_valid(col):
            return empty_df

    # extract the operator from role string
    operator = None
    for op in ["+", "-", "*"]:
        if op in role:
            operator = op
            break
    if operator is None:
        return empty_df

    # parse role and split it into separate columns
    role_split = role.split(operator)
    if len(role_split) != 2:
        return empty_df

    col1 = role_split[0].strip()
    col2 = role_split[1].strip()

    if not (
        is_valid(col1) and is_valid(col2) and col1 in df.columns and col2 in df.columns
    ):
        return empty_df

    result_df = df.copy()

    # new column creation (based on the previously parsed role)
    if operator == "+":
        result_df[new_column] = result_df[col1] + result_df[col2]
    elif operator == "-":
        result_df[new_column] = result_df[col1] - result_df[col2]
    elif operator == "*":
        result_df[new_column] = result_df[col1] * result_df[col2]

    return result_df


if __name__ == "__main__":
    data = {"name": ["banana", "apple"], "quantity": [10, 3], "price": [10, 1]}
    fruits_sales = pd.DataFrame(data)
    print(f"Original DataFrame:\n{fruits_sales}")

    sales_total = add_virtual_column(fruits_sales, "quantity * price", "total")
    print(f"\nResults:\n{sales_total}")
