import yaml

from DataReader import DataReader
from Types import DataType


class MyDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            students = yaml.load(file, Loader=yaml.Loader)
            for student in students:
                itemNumber, items = list(student.items())[0]
                self.students[itemNumber] = []
                for item in items.keys():
                    scores = items.get(item)
                    self.students[itemNumber].append((item, scores))

        return self.students
