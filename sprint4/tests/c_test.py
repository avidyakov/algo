import io
import sys
from dataclasses import dataclass

import pytest

from с import main


@dataclass
class MainCase:
    test_input: str
    expected: str


TESTS = (
    MainCase("""100
10
a
1
1 1
""", """7
"""),
)


@pytest.mark.parametrize('test_case', TESTS)
def test_main(capsys, test_case):
    sys.stdin = io.StringIO(test_case.test_input)
    main()
    out, _ = capsys.readouterr()
    assert out == test_case.expected
