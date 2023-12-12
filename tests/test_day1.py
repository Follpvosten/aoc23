from app.day1 import calc_total_sum

def test_oneplus():
    assert 1 + 1 == 2

example_string = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

def test_example_input():
    assert calc_total_sum(example_string) == 142
