import sys

import pytest

from final2 import main


@pytest.mark.parametrize('stdin, expected', (
        ('test_final2_8.txt', 'test_final2_8_expected.txt'),
        ('final2_input.txt', 'final2_output.txt'),
        ('input.txt', 'output.txt')
))
def test_main(capsys, stdin, expected):
    with open(stdin) as stdin, open(expected) as expected:
        sys.stdin = stdin
        main()
        out, _ = capsys.readouterr()
        assert out == expected.read()
