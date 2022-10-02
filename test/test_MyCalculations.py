import pytest

from MyCalculations import MyCalculations, GetStudentScores, RightScores
from Types import DataType

RightStudentType = str
ScoresType = list
RightScoresType = bool


class TestMyCalculations:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RightStudentType,
                                  ScoresType, RightScoresType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 90),
                    ("русский язык", 90),
                    ("программирование", 90),
                    ("литература", 90)
                ]
        }

        rightStudent: RightStudentType = "Петров Игорь Владимирович"
        scores: ScoresType = [80, 76, 100]
        rightScores: RightScoresType = False

        return data, rightStudent, scores, rightScores

    def test_init_MyCalculations(self, input_data: tuple[DataType,
                                                         RightStudentType,
                                                         ScoresType,
                                                         RightScoresType]) \
            -> None:
        myCalculations = MyCalculations(input_data[0])
        assert input_data[0] == myCalculations.data

    def test_GetRightStudent(self, input_data: tuple[DataType,
                                                     RightStudentType,
                                                     ScoresType,
                                                     RightScoresType]) \
            -> None:
        rightStudent = MyCalculations(input_data[0]).GetRightStudent()
        assert input_data[1] == rightStudent

    def test_GetStudentScores(self, input_data: tuple[DataType,
                                                      RightStudentType,
                                                      ScoresType,
                                                      RightScoresType]) \
            -> None:
        students = list(input_data[0].items())
        student = students[0]
        scores = GetStudentScores(student)
        assert input_data[2] == scores

    def test_RightScores(self, input_data: tuple[DataType,
                                                 RightStudentType,
                                                 ScoresType,
                                                 RightScoresType]) \
            -> None:
        students = list(input_data[0].items())
        student = students[0]
        scores = GetStudentScores(student)
        rightScores = RightScores(scores)
        assert input_data[3] == rightScores
