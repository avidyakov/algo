import sys
import io

import pytest

from final1 import main

TESTS = (
    ("""4
4
push_front 861
push_front -819
pop_back
pop_back
""", """861
-819
"""),
    ("""7
10
push_front -855
push_front 720
pop_back
pop_back
push_back 844
pop_back
push_back 823
""", """-855
720
844
"""),
    ("""6
6
push_front -201
push_back 959
push_back 102
push_front 20
pop_front
pop_back
""", """20
102
""")
)


@pytest.mark.parametrize('test_input, expected', TESTS)
def test_main(capsys, test_input, expected):
    sys.stdin = io.StringIO(test_input)
    main()
    out, _ = capsys.readouterr()
    assert out == expected
