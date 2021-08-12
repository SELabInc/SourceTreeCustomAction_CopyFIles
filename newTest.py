import sys
import os
import shutil

def copyFileMethod(outputList):

    copySource = os.path.join('C:',  os.sep,'CopyFiles')
    os.makedirs(copySource, exist_ok=True)

    for index, mkFile in enumerate(outputList):

        originPath = mainSource +  os.sep + mkFile

        if os.path.isfile(originPath):

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

            results = round((index+1) /len(outputList), 2 ) * 100
            print("{0:>6.2f}% - {1}".format(results, originPath))


if __name__ == "__main__" :

    print("SourceTree Copy Start")

    mainSource = sys.argv[1]
    lastSHA = sys.argv[2]
    startSHA = sys.argv[len(sys.argv)-1]

    mainSource= mainSource.replace("\\" , os.sep)
    os.system('cd {}'.format(mainSource))

    output = os.popen('git diff --name-only {0} {1}'.format(startSHA, lastSHA)).read()

    copyFileMethod(output.splitlines())
    
print("작업이 완료되었습니다!")

copySource = os.path.join('C:',  os.sep,'CopyFiles')
os.system('pause')
os.startfile(copySource)