from collections import defaultdict
from collections import namedtuple


class SimpleGradebook:
    """Record student's grade."""

    def __init__(self) -> None:
        self._grades = {}

    def add_student(self, name: str) -> None:
        """Register student's name

        Args:
            name (str): student's name
        """
        self._grades[name] = []

    def report_grade(self, name: str, score: int) -> None:
        """Register studen't score

        Args:
            name (str): student's name
            score (int): score of report or test
        """
        self._grades[name].append(score)

    def average_grade(self, name: str) -> float:
        """Get average grade of args student

        Args:
            name (str): student's name

        Returns:
            float: average grade of args student
        """
        grades = self._grades[name]
        return sum(grades) / len(grades)


class BySubjectGradebook:
    """Record student's grade by subject."""

    def __init__(self) -> None:
        self._grades = {}

    def add_student(self, name: str) -> None:
        """Register student's name

        Args:
            name (str): student's name
        """
        # When key is missing, create new list
        self._grades[name] = defaultdict(list)

    def report_grade(self, name: str, subject: str, score: int) -> None:
        """Register studen't score

        Args:
            name (str): student's name
            subject (str): subject's name
            score (int): score of report or test
        """
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(score)

    def average_grade(self, name: str) -> float:
        """Get average grade of args student

        Args:
            name (str): student's name

        Returns:
            float: average grade of args student
        """
        by_subject = self._grades[name]
        total, count = 0, 0
        for grade in by_subject.values():
            total += sum(grade)
            count += len(grade)
        return total / count


# リファクタリング
# score, weightのnamedtuple
Grade = namedtuple("Grade", ("score", "weight"))


class Subject:
    """Subject class"""

    def __init__(self) -> None:
        self._grades = []

    def report_grade(self, score: int, weight: float) -> None:
        """Register score and weight

        Args:
            score (int): score of report or test
            weight (float): weight to stat
        """
        self._grades.append(Grade(score, weight))

    def average_grade(self) -> float:
        """Get average of grade

        Returns:
            float: average grade
        """
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    """Student class"""

    def __init__(self) -> None:
        self._subjects = defaultdict(Subject)

    def get_subject(self, name: str) -> Subject:
        """Get student's subject

        Args:
            name (str): student's name

        Returns:
            Subject: instance of subject
        """
        return self._subjects[name]

    def average_grade(self) -> float:
        """Get average grade of all subject

        Returns:
            _float: _description_
        """
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    """Grade book class"""

    def __init__(self) -> None:
        self._students = defaultdict(Student)

    def get_student(self, name: str) -> Student:
        """Get args student

        Args:
            name (str): student's name

        Returns:
           Student: Instance of student
        """
        return self._students[name]


if __name__ == "__main__":
    # 学生ごとの点数を記録する
    book = SimpleGradebook()
    book.add_student("Isaac Newton")
    book.report_grade("Isaac Newton", 90)
    book.report_grade("Isaac Newton", 95)
    book.report_grade("Isaac Newton", 85)
    avg = book.average_grade("Isaac Newton")
    print(f"Average Score : {avg}")

    # 学生の教科ごとの点数を記録する
    # クラス構造が複雑で分かりにくい, 点数の重み付け機能を加えるのも大変
    book = BySubjectGradebook()
    book.add_student("Isaac Newton")
    book.add_student("Albert Einstein")
    book.report_grade("Isaac Newton", "Math", 90)
    book.report_grade("Isaac Newton", "Gym", 70)
    book.report_grade("Albert Einstein", "Math", 95)
    book.report_grade("Albert Einstein", "Gym", 65)
    avg_newton = book.average_grade("Isaac Newton")
    avg_einstein = book.average_grade("Albert Einstein")
    print(f"Newton's Average Score : {avg_newton}")
    print(f"Einstein's Average Score : {avg_einstein}")

    # クラスを用いたリファクタリング例
    book = Gradebook()
    albert = book.get_student("Albert Einstein")
    math = albert.get_subject("Math")
    math.report_grade(75, 0.05)
    math.report_grade(65, 0.15)
    math.report_grade(70, 0.80)
    gym = albert.get_subject("Math")
    gym.report_grade(100, 0.40)
    gym.report_grade(85, 0.60)
    print(albert.average_grade())
