import sys
import os
import datetime

if __name__ == "__main__" :
    print("START")

    mainSource = sys.argv[1]
    firstSha = sys.argv[2]
    secondSha = sys.argv[len(sys.argv)-1]

    for index, arg in enumerate(sys.argv): 
        print('index = {0}, arg value = {1}' .format(index, arg))

    print("결과값")
    print(mainSource)
    print(firstSha)
    print(secondSha)

    os.system('cd {}'.format(mainSource))
    output = os.popen('git diff --name-only {0} {1}'.format(firstSha, secondSha)).read()
    print(output)


os.system('pause')
