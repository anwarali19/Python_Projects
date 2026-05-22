import pandas as pd
import os


def read_excel(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext in [".xlsx", ".xlsm"]:
        return pd.read_excel(file_path, engine="openpyxl")

    elif ext == ".xls":
        return pd.read_excel(file_path, engine="xlrd")

    elif ext == ".xlsb":
        return pd.read_excel(file_path, engine="pyxlsb")

    elif ext == ".ods":
        return pd.read_excel(file_path, engine="odf")

    else:
        raise Exception("Unsupported file format")


def save_excel(df, original_file, suffix):
    base = os.path.splitext(original_file)[0]

    output_file = f"{base}_{suffix}.xlsx"

    df.to_excel(output_file, index=False)

    return output_file