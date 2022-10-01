# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from MyCalculations import MyCalculations
from MyDataReader import MyDataReader
from TextDataReader import TextDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    # reader = TextDataReader()
    reader = MyDataReader()
    students = reader.read(path)
    print("Students: ", students)

    # rating = CalcRating(students).calc()
    # print("Rating: ", rating)

    rightStudent = MyCalculations(students).GetRightStudent()
    if rightStudent == "":
        print("студентов, имеющих 90 баллов по всем дисциплинам нет")
    else:
        print("студент " + rightStudent + " имеет 90 баллов по всем дисциплинам")


if __name__ == "__main__":
    main()
