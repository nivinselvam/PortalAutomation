#To iterate through each line from the textfile hellowWorld which splits each word in line by a /
# sample data in file:
#     success/false/user updated successfully/update user
import allure
import pymysql
import sshtunnel
import pandas as pd



#Convert time to seconds
def sample():
    time = "01:34:11"
    print(sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":"))))



def readFileLineByLine():
    file1 = open("/home/ezetap/PycharmProjects/PortalAutomation/TestData/hellowWorld","r")
    lines = file1.readlines()
    count = 0

    for line in lines:
        count += 1
        words = line.strip().split("/")
        password = words[0]
        success = words[1]
        expectedMessage = words[2]
        testcase = words[3]

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        print("password: ",password)
        print("success:",success)
        print("message:",expectedMessage)
        print("testcase:",testcase)


def dbConnection():
    tunnel = sshtunnel.SSHTunnelForwarder(ssh_address_or_host='dev11', remote_bind_address=('localhost', 3306))
    tunnel.start()
    org_code = "SANDESHIYER_2397"
    conn = pymysql.connect(host='localhost', user='ezedemo', passwd='abc123', database='', port=tunnel.local_bind_port)
    query1 = ("SELECT * from ezetap_demo.setting where org_code ='%s' and setting_value='true';"%org_code)
    data = pd.read_sql_query(query1, conn)
    amount = str(data['amount'].values[0])    #To get only the amount without name and datatype
    conn.close()
    tunnel.close()
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    print(data)


#TO ADD CUSTOM TITLE FOR TEST CASE IN ALLURE REPORT
@allure.title("This test has a custom title")
def test_sampleTest():
    pass



################################################################################################# TO ADD EXTRA DESCRIPTION
# @allure.description_html("""
# <h1>Test with some complicated html description</h1>
# <table style="width:100%">
#   <tr>
#     <th>Firstname</th>
#     <th>Lastname</th>
#     <th>Age</th>
#   </tr>
#   <tr align="center">
#     <td>William</td>
#     <td>Smith</td>
#     <td>50</td>
#   </tr>
#   <tr align="center">
#     <td>Vasya</td>
#     <td>Jackson</td>
#     <td>94</td>
#   </tr>
# </table>
# """)
#
# def test_html_description():
#     assert True
#
#
# @allure.description("""
# Multiline test description.
# That comes from the allure.description decorator.
# Nothing special about it.
# """)
# def test_description_from_decorator():
#     assert 42 == int(6 * 7)
# def test_unicode_in_docstring_description():
#     """Unicode in description.
#     Этот тест проверяет юникод.
#     你好伙计.
#     """
#     assert 42 == int(6 * 7)


##################################################### ADD DIFF TYPES OF LINKS ###############################################
TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
def with_link():
    pass
@allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='Click me')
def with_named_link():
    pass
@allure.issue('140', 'Pytest-flaky test retries shows like test steps')
def with_issue_link():
    pass
@allure.testcase(TEST_CASE_LINK, 'Test case title')
def with_testcase_link():
    pass


