import sys
import io

import pytest

from l import main

TESTS = (
    ("""6
1 2 4 4 6 8
3""", """3 5
"""),
    ("""6
1 2 4 4 4 4
3""", """3 -1
"""),
    ("""6
1 2 4 4 4 4
10""", """-1 -1
""")
)


@pytest.mark.parametrize('test_input, expected', TESTS)
def test_main(capsys, test_input, expected):
    sys.stdin = io.StringIO(test_input)
    main()
    out, _ = capsys.readouterr()
    assert out == expected
