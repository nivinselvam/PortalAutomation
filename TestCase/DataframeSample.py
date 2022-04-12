import pandas as pd

# def dataframe_test():
#     # For Dataframe used for testcase execution and result
#     dataForDataFrameHeader = {
#         'Test Case ID': [],
#         'File Name': [],
#         'TC Execution': [],
#         'API Val': [],
#         'DB Val': [],
#         'Portal Val': [],
#         'App Val': [],
#         'UI Val': [],
#         'Execution Time (sec)': [],
#         'Validation Time (sec)': [],
#         'Log Coll Time (sec)': [],
#         'Total Time (sec)': []
#     }
#
#     df_testCasesDetail = pd.DataFrame(dataForDataFrameHeader)
#
#     df_testCasesDetail.at[0, 'Test Case ID'] = "test_success"
#     df_testCasesDetail.at[1, 'Test Case ID'] = "test_Exe_Failure"
#     df_testCasesDetail.at[2, 'Test Case ID'] = "test_api_val_exe_failure"
#     df_testCasesDetail.at[3, 'Test Case ID'] = "test_DB_Val_Exe_Failure"
#     df_testCasesDetail.at[4, 'Test Case ID'] = "test_portal_val_exe_failure"
#     df_testCasesDetail.at[5, 'Test Case ID'] = "test_api_val_failure"
#     df_testCasesDetail.at[5, 'Test Case ID'] = "test_DB_val_failure"
#     df_testCasesDetail.at[5, 'Test Case ID'] = "test_portal_val_failure"
#
#     df_testCasesDetail.set_index('Test Case ID', inplace=True)
#
#     df_testCasesDetail.at['test_success', 'File Name'] = 1234
#
#
#
#     print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#     print(df_testCasesDetail)
#     #
#     print("BBBBBBBBBBBBBBBB")
#     print(str(df_testCasesDetail.iloc[3, 2]).lower())
    # print(df_testCasesDetail['File Name']['test_success'])
    # print(df_testCasesDetail['test_Exe_Failure']['test_success'])
    # print("BBBBBBBBBBBBBBBBBB")

    # sdf = str(df_testCasesDetail['test_Exe_Failure']['test_success']).lower()
    #
    # print(sdf.lower())


    # datatypes = df_testCasesDetail.dtypes

    # print("Printing the default data types")
    # print("")
    # print(datatypes)
    # print("")

    # convert_dict = {'File Name': str,
    #                 'TC Execution': str,
    #                 'API Val': str,
    #                 'DB Val': str,
    #                 'Portal Val': str,
    #                 'App Val': str,
    #                 'UI Val': str
    #            }
    # #
    # df = df_testCasesDetail.astype(convert_dict)
    # print("Printing changed values")
    # print(df.dtypes)



# def tryItOut():
#     a = "abcde!mdamdskm"
#     print(a.split("!")[1])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def convert_excel_to_DF():
    dataframe1 = pd.read_excel('/home/ezetap/PycharmProjects/PortalAutomation/TestCase/Report.xlsx')
    # print(dataframe1)
    # df = pd.DataFrame(np.random.random((10, 3)), columns=("col 1", "col 2", "col 3"))
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=dataframe1.values, colLabels=dataframe1.columns, loc='center')
    pp = PdfPages("table.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
    print("Created PDF")


convert_excel_to_DF()