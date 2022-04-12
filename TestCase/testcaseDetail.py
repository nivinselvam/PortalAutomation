import pandas as pd

# workbook = pd.read_excel("/home/ezetap/PycharmProjects/PortalAutomation/DataProvider/TestCasesDetail.xlsx", None)
# ls_sheets = workbook.keys()
# print("list of sheets : ", ls_sheets)
# print("")
# df_consolidatedTCList = pd.DataFrame()
# print("")
# print("Empty dataframe : ", df_consolidatedTCList)
#
# for sheet in ls_sheets:
#     print("")
#     print("sheet : ", sheet)
#
#     df_testCasesDetail = pd.DataFrame(workbook.get(sheet))
#     print("Separate dataframe : ")
#     print(df_testCasesDetail)
#
#     df_consolidatedTCList.append(df_testCasesDetail)
#     print("")
#     print("")
#     print("")
#     print("AT LAST")
#     print(df_consolidatedTCList)

workbook = pd.read_excel("/home/ezetap/PycharmProjects/PortalAutomation/DataProvider/TestCasesDetail.xlsx", None)
ls_sheets = workbook.keys()
print("list of sheets : ", ls_sheets)
print("")
df_consolidatedTCList = pd.DataFrame()
print("")
print("Empty dataframe : ", df_consolidatedTCList)
df_all_rows = pd.DataFrame()

for sheet in ls_sheets:
    df_testCasesDetail = pd.DataFrame(workbook.get(sheet))
    df_all_rows = pd.concat([df_all_rows, df_testCasesDetail])

    # df_consolidatedTCList.append(df_testCasesDetail)
print("########")
print(df_all_rows)
df_all_rows.to_excel("/home/ezetap/PycharmProjects/PortalAutomation/TestCase/Report.xlsx")

