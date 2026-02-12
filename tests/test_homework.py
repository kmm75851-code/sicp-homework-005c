import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from homework import (
    apply_to_all, filter_by, compose,
    find_large_files, get_python_files, get_file_sizes,
    make_file_filter, get_extension
)

TEST_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "test_files")


class TestApplyToAll:
    def test_double(self):
        assert apply_to_all(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]

    def test_square(self):
        assert apply_to_all(lambda x: x ** 2, [1, 2, 3, 4]) == [1, 4, 9, 16]

    def test_empty(self):
        assert apply_to_all(lambda x: x, []) == []

    def test_strings(self):
        assert apply_to_all(str.upper, ["a", "b"]) == ["A", "B"]

    def test_extensions(self):
        files = ["photo.jpg", "doc.pdf", "main.py"]
        assert apply_to_all(get_extension, files) == ["jpg", "pdf", "py"]


class TestFilterBy:
    def test_positive(self):
        assert filter_by(lambda x: x > 0, [-1, 2, -3, 4]) == [2, 4]

    def test_even(self):
        assert filter_by(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_empty_result(self):
        assert filter_by(lambda x: x > 100, [1, 2, 3]) == []

    def test_all_pass(self):
        assert filter_by(lambda x: x > 0, [1, 2, 3]) == [1, 2, 3]

    def test_strings(self):
        assert filter_by(lambda s: len(s) > 3, ["a", "abc", "abcd"]) == ["abcd"]


class TestCompose:
    def test_double_add1(self):
        add1 = lambda x: x + 1
        double = lambda x: x * 2
        assert compose(double, add1)(5) == 12

    def test_square_add1(self):
        add1 = lambda x: x + 1
        square = lambda x: x * x
        assert compose(square, add1)(3) == 16

    def test_identity(self):
        identity = lambda x: x
        double = lambda x: x * 2
        assert compose(identity, double)(5) == 10

    def test_string_ops(self):
        upper = str.upper
        strip = str.strip
        assert compose(upper, strip)("  hello  ") == "HELLO"


class TestFindLargeFiles:
    def test_large_files(self):
        result = find_large_files(TEST_DIR, 100)
        assert "large.txt" in result
        assert "medium.txt" in result
        assert "small.txt" not in result

    def test_very_large_threshold(self):
        result = find_large_files(TEST_DIR, 500)
        assert result == ["large.txt"]

    def test_zero_threshold(self):
        result = find_large_files(TEST_DIR, 0)
        assert len(result) == 6


class TestGetPythonFiles:
    def test_python_files(self):
        result = get_python_files(TEST_DIR)
        assert "script.py" in result
        assert "utils.py" in result
        assert len(result) == 2

    def test_no_txt_files(self):
        result = get_python_files(TEST_DIR)
        assert "small.txt" not in result
        assert "data.csv" not in result


class TestGetFileSizes:
    def test_returns_tuples(self):
        result = get_file_sizes(TEST_DIR)
        assert isinstance(result, list)
        assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    def test_correct_sizes(self):
        result = dict(get_file_sizes(TEST_DIR))
        assert result["small.txt"] == 5
        assert result["large.txt"] == 762


class TestMakeFileFilter:
    def test_py_filter(self):
        py_filter = make_file_filter("py")
        assert py_filter("main.py") == True
        assert py_filter("data.csv") == False

    def test_txt_filter(self):
        txt_filter = make_file_filter("txt")
        assert txt_filter("notes.txt") == True
        assert txt_filter("script.py") == False

    def test_closure(self):
        csv_filter = make_file_filter("csv")
        json_filter = make_file_filter("json")
        assert csv_filter("data.csv") == True
        assert json_filter("data.csv") == False
