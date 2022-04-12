import time
import fcntl
from datetime import datetime

import openpyxl
import pandas
import pandas as pd
import pymysql

from TestCase import ExcelProcessor

path = "/home/ezetap/PycharmProjects/PortalAutomation/DataProvider/UserDetails.xlsx"
sheetName = 'Credentials'


def getUserCredentialsFromExcel():
    timer = 1
    while timer < 600:
        try:
            with open(path, 'a') as myFile:
                fcntl.flock(myFile, fcntl.LOCK_EX | fcntl.LOCK_NB)
                df_userDetails = pd.read_excel(path, sheet_name='Credentials')
                df_userDetails.set_index('Username', inplace=True)
                userAvailable = False

                for index in df_userDetails.index:
                    if str(df_userDetails['Status'][index]).lower() == "available":
                        availableUserCredentials = [index, df_userDetails['Password'][index]]
                        updateUserStatusInExcel(index, 'Blocked')
                        fcntl.flock(myFile, fcntl.LOCK_UN)
                        userAvailable = True
                        break

                if userAvailable:
                    return availableUserCredentials
                else:
                    return None
        except IOError as e:
            time.sleep(1)
            timer = timer + 1


def releaseUserInExcel(username):
    try:
        updateUserStatusInExcel(username, 'Available')
        print("Released the credentials of user " + str(username) + " at " + str(datetime.now().time()))
        return True
    except:
        print("Unable to release the credentials of user " + str(username))
        return False


def updateUserStatusInExcel(username, status):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheetName]
    rowNumber = ExcelProcessor.getRowNumberFromValue(workbook, sheet, 'Username', username)
    columnNumber = ExcelProcessor.getColumnNumberFromName(workbook, sheet, 'Status')
    sheet.cell(row=rowNumber, column=columnNumber).value = status
    workbook.save(path)
    workbook.close()


def getUserCredentialsFromDB():
    conn = pymysql.connect(host='localhost', user='root', database='Automation')
    userCredentials = []
    username = ''
    timer = 0
    while timer<30:
        query = "SELECT Username, Password FROM user_credentials WHERE Status = 'Available' limit 1 FOR UPDATE;"
        print("Trying to get user credentials from DB")
        queryResult = pandas.read_sql_query(query, conn)
        try:
            username = queryResult['Username'][0]
            password = queryResult['Password'][0]
            print("Username "+username+"is available")
            userCredentials.append(username)
            userCredentials.append(password)
            cursor = conn.cursor()
            query = "UPDATE user_credentials SET Status='Blocked' WHERE Username = '"+username+"';"
            cursor.execute(query)
            break
        except IndexError:
            print("All the user credentials are already in use.")
            time.sleep(1)
            timer+=1
    conn.commit()
    conn.close()
    if len(userCredentials)==0:
        return None
    else:
        return userCredentials


def releaseUserInDB(username):
    conn = pymysql.connect(host='localhost', user='root', database='Automation')
    query = "UPDATE user_credentials SET status='available' WHERE username = '" + username + "';"
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        print(username+" is released at "+str(datetime.now().time()))
    except:
        print("Unable to release the user "+username)
    conn.commit()
    conn.close()


# print(getUserCredentials())


