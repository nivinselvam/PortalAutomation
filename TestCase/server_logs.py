import paramiko
from DataProvider import GlobalVariables
from Pages import BaseActions

ssh = paramiko.SSHClient()
env = BaseActions.environment("env")

router_ip = '192.168.3.81'    #dev11
router_username = 'divyaandrews' # Replace with your username in config file
router_port = 22
key_filename = '/home/ezetap/.ssh/divya'


# Login to the server
def ssh_connection(ip_address, routerPort, username, key_filename):
    print("Trying To Connect To The Server...")
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip_address, port=routerPort, username=username,
                    pkey=paramiko.RSAKey.from_private_key_file(key_filename))
        return True
    except Exception as error_message:
        print("Unable To Connect To Server")
        print(error_message)
        return False


# To Fetch API logs
def fetchAPILogs():
    data_buffer = ''
    startLineNo = GlobalVariables.startLineNumberAPI
    if env.__contains__('dev'):
        typeOfLog = 'api_' + env[:3]
        logfileName = BaseActions.pathToLogFile(typeOfLog)
        ednLineNo = noOfLine(logfileName)
        command = "awk " + "'NR>=" + startLineNo + " && " + "NR<=" + ednLineNo + " { print }' " + logfileName
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command, get_pty=True)
        for line in iter(lambda: ssh_stdout.readline(), ''):
            data_buffer += line
        return data_buffer
    else:
        typeOfLog = 'api'
        logfileName = BaseActions.pathToLogFile(typeOfLog)
        ednLineNo = noOfLine(logfileName)
        command = "awk " + "'NR>=" + startLineNo + " && " + "NR<=" + ednLineNo + " { print }' " + logfileName
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command, get_pty=True)
        for line in iter(lambda: ssh_stdout.readline(), ''):
            data_buffer += line
        return data_buffer


# To fetch Portal logs
def fetchPortalLogs():
    data_buffer = ''
    startLineNo = GlobalVariables.startLineNumberPortal
    if env.__contains__('dev'):
        typeOfLog = 'portal_' + env[:3]
        logfileName = BaseActions.pathToLogFile(typeOfLog)
        endLineNo = noOfLine(logfileName)
        command = "awk " + "'NR>=" + startLineNo + " && " + "NR<=" + endLineNo + " { print }' " + logfileName
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command, get_pty=True)
        for line in iter(lambda: ssh_stdout.readline(), ''):
            data_buffer += line
        return data_buffer
    else:
        typeOfLog = 'portal'
        logfileName = BaseActions.pathToLogFile(typeOfLog)
        endLineNo = noOfLine(logfileName)
        command = "awk " + "'NR>=" + startLineNo + " && " + "NR<=" + endLineNo + " { print }' " + logfileName
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command, get_pty=True)
        for line in iter(lambda: ssh_stdout.readline(), ''):
            data_buffer += line
        return data_buffer


# To fetch Middleware logs
def fetchMiddlewareLogs():
    data_buffer = ''
    startLineNo = GlobalVariables.startLineNumberMiddlewware
    if env.__contains__('dev'):
        typeOfLog = 'middleware_' + env[:3]
        logfileName = BaseActions.pathToLogFile(typeOfLog)
        endLineNo = noOfLine(logfileName)
        command = "awk " + "'NR>=" + startLineNo + " && " + "NR<=" + endLineNo + " { print }' " + logfileName
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command, get_pty=True)
        for line in iter(lambda: ssh_stdout.readline(), ''):
            data_buffer += line
        return data_buffer
    else:
        typeOfLog = 'middleware'
        logfileName = BaseActions.pathToLogFile(typeOfLog)
        endLineNo = noOfLine(logfileName)
        command = "awk " + "'NR>=" + startLineNo + " && " + "NR<=" + endLineNo + " { print }' " + logfileName
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command, get_pty=True)
        for line in iter(lambda: ssh_stdout.readline(), ''):
            data_buffer += line
        return data_buffer


# To fetch CNP ware logs
def fetchCnpwareLogs():
    data_buffer = ''
    startLineNo = GlobalVariables.startLineNumberCnpware
    if env.__contains__('dev'):
        typeOfLog = 'cnpware_' + env[:3]
        logfileName = BaseActions.pathToLogFile(typeOfLog)
        endLineNo = noOfLine(logfileName)
        command = "awk " + "'NR>=" + startLineNo + " && " + "NR<=" + endLineNo + " { print }' " + logfileName
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command, get_pty=True)
        for line in iter(lambda: ssh_stdout.readline(), ''):
            data_buffer += line
        return data_buffer
    else:
        typeOfLog = 'cnpware'
        logfileName = BaseActions.pathToLogFile(typeOfLog)
        endLineNo = noOfLine(logfileName)
        command = "awk " + "'NR>=" + startLineNo + " && " + "NR<=" + endLineNo + " { print }' " + logfileName
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command, get_pty=True)
        for line in iter(lambda: ssh_stdout.readline(), ''):
            data_buffer += line
        return data_buffer


# To get no of lines from the log file
def noOfLine(logFileName):
    command = 'wc -l ' + logFileName
    # print("FIRST LINE IN NO_OF_LINE")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command, get_pty=True)
    # print("SECOND LINE IN NO_OF_LINE")
    line = ssh_stdout.readline()
    number = line.split(' ')
    return number[0]


# To append the logs in the respective file
def appendLogs(fileName, testName, logs):
    with open(fileName, "a") as file:
        file.write(testName + "\n")
        file.write(logs + "\n")


# ssh_connection(router_ip, router_port, router_username, key_filename)
# print(noOfLine('/var/log/ezetap/api/api.log'))



