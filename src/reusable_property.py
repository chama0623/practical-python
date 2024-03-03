from weakref import WeakKeyDictionary


class Homework:
    def __init__(self) -> None:
        self._grade = 0

    @property
    def grade(self) -> int:
        return self._grade

    @grade.setter
    def grade(self, value: int):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._grade = value


# 正常に動作しないGradeクラス
# class BadGrade:
#     def __init__(self) -> None:
#         self._value = 0

#     def __get__(self, instance, instance_type):
#         return self._value

#     def __set__(self, instance, value):
#         if not (0 <= value <= 100):
#             raise ValueError("Grade must be between 0 and 100")
#         self._value = value


class Grade:
    def __init__(self) -> None:
        # dictで管理するとインスタンスが保持されるため, メモリリークの可能性がある
        # self._values = {}
        # WeakKeyDictionaryによる改善
        # WeakKeyはキーの参照先がなくなると, 自動でそのキーが削除される
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._values[instance] = value


# 退屈で汎用的ではない実装
# class Exam:
#     def __init__(self) -> None:
#         self._writing_grade = 0
#         self._math_grade = 0

#     @staticmethod
#     def _check_grade(value: int):
#         if not (0 <= value <= 100):
#             raise ValueError("Grade must be between 0 and 100")

#     @property
#     def writing_grade(self) -> int:
#         return self._writing_grade

#     @writing_grade.setter
#     def writing_grade(self, value: int):
#         self._check_grade(value)
#         self._writing_grade = value

#     @property
#     def math_grade(self) -> int:
#         return self._math_grade

#     @math_grade.setter
#     def math_grade(self, value: int):
#         self._check_grade(value)
#         self._math_grade = value


# ディスクプリを用いた再利用可能な@property
class Exam:
    math_grade = Grade()  # BadGrade()
    writing_grade = Grade()  # BadGrade()
    science_grade = Grade()  # BadGrade()


if __name__ == "__main__":
    galileo = Homework()
    galileo.grade = 95
    print("Galileo's score is", galileo.grade)

    first_exam = Exam()
    # Exam.__dict__["writing_grade"].__set__(exam, 40)として解釈
    first_exam.writing_grade = 82
    first_exam.science_grade = 99
    print("Writing", first_exam.writing_grade)  # 82
    print("Science", first_exam.science_grade)  # 99

    second_exam = Exam()
    second_exam.writing_grade = 75
    print("Second Writing", second_exam.writing_grade)  # 75
    print("First Writing", first_exam.writing_grade)  # 75 (expected 82)
    # これはGradeインスタンスがすべてのExamインスタンスの属性に共有されており,
    # __set__()が実行されることにより起こる
