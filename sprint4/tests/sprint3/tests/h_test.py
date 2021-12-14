from dataclasses import dataclass
import io
import sys

import pytest

from h import get_the_largest_number_from, main


@dataclass
class TestCase:
    test_input: str
    expected: str

#
# TESTS = (
#     TestCase(
#         '82 468 941 181 287 861 291 515 263 424 470 620 954 894 565 69 148 587 823 57 730 389 921 1000 447 1000 748 104 831 943 174 24 340 1000 150 937 324 919 748 271 980 575 392 779 222 316 944 1000 160 501 319 436 26 828 348 211 825 857 486 1000 419 509 409 679 576 700 418 810 674 83 785 251 947 868 964 384 497 192 1000 998 756 649 269 290 197 30 95 796 642 980 474 122 443 707 839 213 1000 530 263 193',
#         '99898098096495954947944943941937921919894868861857839838318288282582381079678577975674874873070770069679674649642620587576575755655305155095014974864744704684474434364244194184093923893843483403243193163029129028727126926326326251242222132111971931921811741601501481221041000100010001000100010001000'
#     ),
#     # TestCase(
#     #     '1000 760 987 422 401 67 321 477 239 128 371 576 819 66 468 992 78 576 648 288 279 1000 182 352 605 80 911 497 569 89 608 220 502 938 988 253 857 496 388 371 932 779 813 437 962 841 584 427 283 133 734 44 921 573 968 779 460 688 871 435 547 821 311 898 402 233 661 206 929 981 72 731 346 258 619 422 884 209 833 1000 518 1000 909 412 462 583 83 988 694 9 436 314 790 978 166 13 938 71 261 177',
#     #     '9992988988987981978968962938938932929921911909898988848718578418383382181981380790787797797607347317271694688676666164861960860558458357657657356954751850249749647746846246044437436435427422422412402401388371371352346321314311288283279261258253239233220209206182177166133131281000100010001000'
#     # ),
# )
#
#
# @pytest.mark.parametrize('test_case', TESTS)
# def test_get_the_largest_number_from(test_case):
#     actual_result = get_the_largest_number_from(test_case.test_input.split())
#     assert actual_result == test_case.expected


TESTS = (
    TestCase(
        test_input="""100
82 468 941 181 287 861 291 515 263 424 470 620 954 894 565 69 148 587 823 57 730 389 921 1000 447 1000 748 104 831 943 174 24 340 1000 150 937 324 919 748 271 980 575 392 779 222 316 944 1000 160 501 319 436 26 828 348 211 825 857 486 1000 419 509 409 679 576 700 418 810 674 83 785 251 947 868 964 384 497 192 1000 998 756 649 269 290 197 30 95 796 642 980 474 122 443 707 839 213 1000 530 263 193
""",
        expected="""99898098096495954947944943941937921919894868861857839838318288282582381079678577975674874873070770069679674649642620587576575755655305155095014974864744704684474434364244194184093923893843483403243193163029129028727126926326326251242222132111971931921811741601501481221041000100010001000100010001000
"""
    ),
    TestCase(
        test_input="""100
530 919 598 564 301 502 512 161 762 594 870 146 775 40 282 500 179 520 512 1000 865 237 167 52 958 437 504 333 421 980 748 358 739 478 740 409 578 629 76 359 677 967 733 91 484 360 945 572 313 73 770 779 131 595 708 624 339 1000 720 732 106 441 569 74 617 560 127 224 88 1000 623 651 871 835 437 14 1000 784 407 277 149 562 14 292 56 20 623 772 20 213 486 976 203 99 806 660 127 60 931 485
""",
        expected="""99980976967958945931919918887187086583580678477977577277076762748747407397373373272070867766065162962462362361760598595594578572569565645625605305252051251250450250048648548447844143743742140940740360359358339333313301292282277237224213203202017916716114914614141311271271061000100010001000
"""
    ),
    TestCase(
        test_input="""100
1000 760 987 422 401 67 321 477 239 128 371 576 819 66 468 992 78 576 648 288 279 1000 182 352 605 80 911 497 569 89 608 220 502 938 988 253 857 496 388 371 932 779 813 437 962 841 584 427 283 133 734 44 921 573 968 779 460 688 871 435 547 821 311 898 402 233 661 206 929 981 72 731 346 258 619 422 884 209 833 1000 518 1000 909 412 462 583 83 988 694 9 436 314 790 978 166 13 938 71 261 177
""",
        expected="""9992988988987981978968962938938932929921911909898988848718578418383382181981380790787797797607347317271694688676666164861960860558458357657657356954751850249749647746846246044437436435427422422412402401388371371352346321314311288283279261258253239233220209206182177166133131281000100010001000
"""
    )
)


@pytest.mark.parametrize('test_case', TESTS)
def test_main(capsys, test_case):
    sys.stdin = io.StringIO(test_case.test_input)
    main()
    out, _ = capsys.readouterr()
    assert out == test_case.expected
