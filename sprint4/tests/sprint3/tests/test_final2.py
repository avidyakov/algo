import sys
import io
from dataclasses import dataclass

import pytest

from final2 import main


@dataclass
class MainCase:
    input_stdin: str
    expected_stdout: str


MAIN_CASES = (
    MainCase('''5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80
''', '''gena
timofey
alla
gosha
rita
'''),
    MainCase('''5
alla 0 0
gena 0 0
gosha 0 0
rita 0 0
timofey 0 0
''', '''alla
gena
gosha
rita
timofey
''')
)


@pytest.mark.parametrize('case', MAIN_CASES)
def test_main(capsys, case):
    sys.stdin = io.StringIO(case.input_stdin)
    main()
    out, _ = capsys.readouterr()
    assert out == case.expected_stdout
