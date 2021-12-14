import sys

from final1 import main

from icecream import ic


def test_main(capsys):
    with open('tests/final1_input1.txt') as test_input:
        sys.stdin = test_input
        main()
        captured = capsys.readouterr()
        ic(captured.err)
        assert captured.out == """gena
timofey
alla
gosha
rita
"""


def test_main2(capsys):
    with open('tests/final1_input2.txt') as test_input:
        sys.stdin = test_input
        main()
        captured = capsys.readouterr()
        ic(captured.err)
        assert captured.out == """alla
gena
gosha
rita
timofey
"""
