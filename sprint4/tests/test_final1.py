import sys

import pytest

from final1 import main


@pytest.mark.parametrize('stdin, expected', (
        ('tests/final1_input1.txt', 'tests/final1_output1.txt'),
        ('tests/final1_input2.txt', 'tests/final1_output2.txt'),
        ('tests/final1/08', 'tests/final1/08.a'),
        ('tests/final1/09', 'tests/final1/09.a'),
        ('tests/final1/10', 'tests/final1/10.a'),
))
def test_main(capsys, stdin, expected):
    with open(stdin) as stdin, open(expected) as expected:
        sys.stdin = stdin
        main()
        out, _ = capsys.readouterr()
        assert out == expected.read()
