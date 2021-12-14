import sys
import io

import pytest

from j import main

TESTS = (
    ('''10
put -34
put -23
get
size
get
size
get
get
put 80
size
''', '''-34
1
-23
0
error
error
1
'''), ('''9
get
size
put 74
get
size
put 90
size
size
size
''', '''error
0
74
0
1
1
1
'''), ('''6
put -66
put 98
size
size
get
get
''', '''2
2
-66
98
''')
)


@pytest.mark.parametrize('test_input, expected', TESTS)
def test_main(capsys, test_input, expected):
    sys.stdin = io.StringIO(test_input)
    main()
    out, _ = capsys.readouterr()
    assert out == expected
