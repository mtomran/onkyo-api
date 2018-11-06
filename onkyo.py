import subprocess
def runCommand(command):
    result= subprocess.check_output(['onkyo', command])
    print result
    return result

