import sys
import io

import pytest

from a import main

TESTS = (
    ('3', """((()))
(()())
(())()
()(())
()()()
"""),
    ('2', """(())
()()
""")
)


@pytest.mark.parametrize('test_input, expected', TESTS)
def test_main(capsys, test_input, expected):
    sys.stdin = io.StringIO(test_input)
    main()
    out, _ = capsys.readouterr()
    assert out == expected
