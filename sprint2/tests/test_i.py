import io
import sys

from i import main


def test_main(capsys):
    sys.stdin = io.StringIO('''17
8
push -82
push -25
push -57
push -24
size
push 12
push 21
push 62
push 64
push -90
size
pop
peek
push -10
push 60
push 67
size

''')
    main()
    out, _ = capsys.readouterr()
    assert out == '''4
error
8
-82
-25
error
error
8
'''


def test_main2(capsys):
    sys.stdin = io.StringIO('''42
2
push -5
peek
pop
peek
size
push -92
push 91
size
pop
pop
push -8
push 50
pop
peek
size
peek
push 30
peek
peek
pop
size
peek
size
push 96
push -9
push -74
peek
push 22
push -36
peek
pop
peek
push -1
pop
push 55
push -83
push -8
push -57
pop
peek
size
push 80

''')
    main()
    out, _ = capsys.readouterr()
    assert out == '''-5
-5
None
0
2
-92
91
-8
50
1
50
50
50
50
1
30
1
error
error
30
error
error
30
30
96
96
error
error
error
-1
55
1
'''