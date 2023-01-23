import pandas as pd
import openpyxl
from openpyxl.workbook import Workbook


class ExcelToJson:
    def __init__(self, file_path: str) -> None:
        self.__file_path: str = file_path

    def convert_to_json(self) -> dict:
        work_book: Workbook = openpyxl.load_workbook(self.__file_path)
        sheet_name: str = work_book.sheetnames[0]

        data_df: pd.DataFrame = pd.read_excel(self.__file_path, sheet_name, dtype=str)
        index: str = data_df.columns[0]
        data = data_df.set_index(index).T.to_dict(orient="list")

        return data
