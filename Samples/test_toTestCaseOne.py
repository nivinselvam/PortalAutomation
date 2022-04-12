import time

import pytest
from TestCase import setUp
import conftest


tc = 2

def test_Fail():
    pytest.fail()


# @pytest.mark.flaky(reruns=2)
@pytest.mark.usefixtures("my_setup")
def test_pass1():
    global tc
    if tc == 1:
        setUp.createStatusTable("True", "True", "True", "True")
        print("INSIDE TESTCASE NUMBER 12")
        # time.sleep(14)
    else:
        tc = 1
        assert False

#







@pytest.mark.usefixtures("my_setup")
def test_pass2():
    setUp.sampleTrial()

@pytest.mark.usefixtures("my_setup")
def test_pass2234234():
    setUp.sampleTrial()








    # setUp.createStatusTable("True", "True", "True", "True")
    # print("INSIDE TESTCASE NUMBER 13")

#
# @pytest.mark.usefixtures("my_setup")
# def test_pass3():
#     setUp.createStatusTable("True", "True", "True", "True")
#     print("INSIDE TESTCASE NUMBER 16")
#
# @pytest.mark.usefixtures("my_setup")
# def test_pass4():
#     setUp.createStatusTable("True", "True", "True", "True")
#     print("INSIDE TESTCASE NUMBER 14")
#     # time.sleep(14)
#
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_pass5():
#     setUp.createStatusTable("True", "True", "True", "True")
#     print("INSIDE TESTCASE NUMBER 15")
#     # time.sleep(17)
#
# @pytest.mark.usefixtures("my_setup")
# def test_pass6():
#     setUp.createStatusTable("True", "True", "True", "True")
#     print("INSIDE TESTCASE NUMBER 1")
#     # time.sleep(13)
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_pass7():
#     setUp.createStatusTable("True", "True", "True", "True")
#     print("INSIDE TESTCASE NUMBER 3")
#     # time.sleep(20)
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail1():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     print("INSIDE TESTCASE NUMBER 5")
#     assert False
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail2():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     assert False
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail3():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     conftest.api_ValidationCount = +1
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     conftest.api_ValidationCount
#     assert False
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail4():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     assert False
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail5():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     pytest.xfail()
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail6():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     assert False
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail7():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     assert False
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail8():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     assert False
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail9():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     assert False
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_fail10():
#     setUp.createStatusTable("True", "False", "True", "True")
#     # time.sleep(12)
#     assert False
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_skip1():
#     # time.sleep(12)
#     pytest.skip('Skipping test---------------------')
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_skip2():
#     # time.sleep(19)
#     pytest.skip('Skipping test---------------------')
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_skip3():
#     # time.sleep(19)
#     pytest.skip('Skipping test---------------------')
#
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_skip4():
#     pytest.skip('Skipping test---------------------')
#
#
#
# @pytest.mark.usefixtures("my_setup")
# def test_skip5():
#     pytest.skip('Skipping test---------------------')
