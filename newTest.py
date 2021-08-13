import sys
import os
import shutil

logList =[]

def copyEachFile(outputList, mainSource):
   
    for index, mkFile in enumerate(outputList):
        originPath = os.sep.join([mainSource, mkFile]) 

        if os.path.isfile(originPath):
            logList.append(originPath)
            copySource = os.path.join('C:',  os.sep,'CopyFiles')
            chkList = mkFile.split("/")

            for chk in chkList[:-1]:
                copySource = copySource + os.sep + chk
        
            mkFile= mkFile.replace("/", os.sep)
            os.makedirs(copySource, exist_ok=True)

            try:
                # os.popen('copy {0} {1}'.format(originPath, copySource))
                shutil.copy(originPath, copySource)

            except BaseException as e:
                print(e)

            finally:
                results = round((index+1) /len(outputList), 2 ) * 100
                print("{0:>6.2f}% - {1}".format(results, originPath))


def copyFileMethod(outputList, mainSource):
    copySource = os.path.join('C:',  os.sep,'CopyFiles')
    os.makedirs(copySource, exist_ok=True)
    copyEachFile(outputList, mainSource)
    logFileName = copySource + os.sep + "logFile.txt"
    f = open(logFileName, 'w')

    for logs in logList:
        f.write(logs+"\n")

    f.close()

if __name__ == "__main__" :

    print("SourceTree Copy Start")
    mainSource= sys.argv[1].replace("\\" , os.sep)
    os.chdir(mainSource)
    alloutput = os.popen('git diff --name-only {0} {1}'.format(sys.argv[len(sys.argv)-1], sys.argv[2])).read()
    output = os.popen('git diff --name-only --diff-filter=d {0} {1}'.format(sys.argv[len(sys.argv)-1], sys.argv[2])).read()
    copyFileMethod(output.splitlines(), mainSource)
    

print("Copy Finished!\nPlease check the logFile of the copied directory.")
os.system('pause')

copySource = os.path.join('C:',  os.sep,'CopyFiles')
os.startfile(copySource)