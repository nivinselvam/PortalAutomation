import pytest

# from test_toTestSetup import testSetup
from TestCase import setUp


# @pytest.mark.usefixtures("my_setup")
# # class testCase2():
# def test_testCaseNumber2():
#     setUp.createStatusTable("True", "True", "True", "True")
#     print("INSIDE TESTCASE NUMBER 2")
#
# @pytest.mark.usefixtures("my_setup")
# def test_testCaseNumber4():
#     setUp.createStatusTable("True", "True", "True", "True")
#     print("INSIDE TESTCASE NUMBER 4")


@pytest.mark.usefixtures("my_setup")
def test_pas2234234():
    a = "Hello"
    b =1,"asd"
    #
    # print("aaaaaaaaaaaaaaaa"+str(b))
    # print(a+True)
    #
    # print("AAAAAAAAAAAAAAAAAAAAAAA")
    # assert "asd"=="axc"