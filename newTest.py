import sys
import os
import shutil


typeValueDic = {}
logList =[]
filteredOutputList =[]

def getKey(selector):
    for key, dicValue in typeValueDic.items():
         if selector == dicValue:
             return key
 
    return "There is no such Key"


def copyEachFile(outputList, mainSource):
    print("=========================================================")
    print("Copy Start")
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

def filteringList(outputList, typeList, typeValueDic):
    selector = 99
    while selector > -1:

        if selector == 8887:
            print("=========================================================")
            print("전체 파일 리스트")
            for index, output in enumerate(outputList):
                print("{0} : {1}".format(index, output))


        print("=========================================================")
        print("복사하지 않을 확장자의 번호를 입력하세요")
        print("파일 리스트를 보고싶으면 8888을 입력해주세요.")
        print("파일 복사를 시작하려면 0번을 선택해주세요.")
        for turples in  typeValueDic.items():
            print("{0} : {1}".format(turples[1] + 1, turples[0]))
        try:
            inputData = sys.stdin.readline()
            selector = int(inputData) - 1
        except Exception as e:
            print(e)
            if inputData == '\n':
                selector = -1

        tempnum = getKey(selector)

        if tempnum != "There is no such Key":
            del typeValueDic[tempnum]
            print("=========================================================")
            print("{0} 확장자 제외 완료 ".format(tempnum))
        

    for filteredTurple in typeValueDic.items():
        for filtering in typeList[filteredTurple[1]]:
            filteredOutputList.append(outputList[filtering])


if __name__ == "__main__" :
    print("=========================================================")
    print("SourceTree Copy Start")
    output = os.popen('git diff --name-only --diff-filter=d {0} {1}'.format(sys.argv[len(sys.argv)-1], sys.argv[2])).read()
    dicIndex = 0
    typeList = []
    outputList = output.splitlines()
    for idx,line in enumerate(outputList):
        
        while line.find(".") > -1:
            line = line[line.find(".") + 1:]

        if line not in typeValueDic:
            typeList.append([])
            typeValueDic[line] = dicIndex
            dicIndex += 1

        typeList[typeValueDic[line]].append(idx)

    filteringList(outputList, typeList, typeValueDic)
    
    mainSource= sys.argv[1].replace("\\" , os.sep)
    os.chdir(mainSource)

    copyFileMethod(filteredOutputList, mainSource)
    
print("=========================================================")
print("Copy Finished!\nPlease check the logFile of the copied directory.")
os.system('pause')

copySource = os.path.join('C:',  os.sep,'CopyFiles')
os.startfile(copySource)