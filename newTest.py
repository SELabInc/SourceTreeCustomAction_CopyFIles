import sys
import os

def copyFileMethod(outputList):

    copySource = os.path.join('C:',  os.sep,'CopyFiles')
    os.makedirs(copySource, exist_ok=True)

    for index, mkFile in enumerate(outputList):

        copySource = os.path.join('C:',  os.sep,'CopyFiles')
        chkList = mkFile.split("/")

        for chk in chkList[:-1]:
            copySource = copySource + os.sep + chk
       
        mkFile= mkFile.replace("/", os.sep)
        originPath = mainSource +  os.sep + mkFile

        os.makedirs(copySource, exist_ok=True)
        os.popen('copy {0} {1}'.format(originPath, copySource))
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
    
copySource = os.path.join('C:',  os.sep,'CopyFiles')

os.system('pause')
os.startfile(copySource)