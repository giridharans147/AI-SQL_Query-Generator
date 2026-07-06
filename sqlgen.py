import re

def extract_column(question):
    question = question.lower()

    columns = [
        "salary",
        "price",
        "age",
        "amount",
        "stock",
        "city",
        "category"
    ]

    for col in columns:
        if col in question:
            return col

    return "column_name"

 

def generate_sql(question, prediction,column):

    question = question.lower()

    # Detect table
    if "employee" in question:
        table = "employees"

    elif "customer" in question:
        table = "customers"

    elif "product" in question:
        table = "products"

    elif "Orders" in question:
        table="products"

    else:
        table = "table_name"

    # SELECT *
    if prediction == "SELECT_ALL":
        return f"SELECT * FROM {table};"

    # SELECT WHERE city
    elif prediction == "SELECT_WHERE":

        match = re.search(r"city\s+([a-zA-Z]+)", question)

        if match:
            city = match.group(1).title()
            return f"SELECT * FROM {table} WHERE city = '{city}';"

        return f"SELECT * FROM {table} WHERE condition;"

    # ORDER BY
    elif prediction == "ORDER_BY":

        if "ascending" in question or "asc" in question:
            return f"SELECT * FROM {table} ORDER BY {column} ASC;"

        elif "descending" in question or "desc" in question:
            return f"SELECT * FROM {table} ORDER BY {column} DESC;"

        return f"SELECT * FROM {table} ORDER BY {column};"

    # COUNT
    elif prediction == "COUNT":
        return f"SELECT COUNT(*) FROM {table};"

    # MAX
    elif prediction == "MAX":
        return f"SELECT MAX({column}) FROM {table};"

    # MIN
    elif prediction == "MIN":
        return f"SELECT MIN({column}) FROM {table};"

    # AVG
    elif prediction == "AVG":
        return f"SELECT AVG({column}) FROM {table};"

    # SUM
    elif prediction == "SUM":
        return f"SELECT SUM({column}) FROM {table};"

    else:
        return "Unable to generate SQL."