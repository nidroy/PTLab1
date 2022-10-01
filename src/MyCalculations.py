from Types import DataType


class MyCalculations:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def GetStudentScores(self, studentNumber):
        student = list(self.data[studentNumber].values())
        scores = list(student[0].values())
        return scores

    def RightScores(self, studentNumber):
        scores = MyCalculations.GetStudentScores(self, studentNumber)
        isRightScores = True
        for itemScores in scores:
            if itemScores != 90:
                isRightScores = False
        return isRightScores

    def GetRightStudent(self):
        rightStudent = ""
        for studentNumber in range(len(self.data)):
            if MyCalculations.RightScores(self, studentNumber):
                student = list(self.data[studentNumber].keys())
                rightStudent = str(student[0])
        return rightStudent
