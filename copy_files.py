import sys
import os
import shutil


class ResultData: 
    """
    문장과 문장 삭제여부를 저장합니다.
    """
    def __init__(self):
        '''
        초기화
        '''
        self.is_use = 0
        self.output = ""

    def setdata(self, set_output_data):
        '''
        문장을 업데이트합니다.
        '''
        self.output = set_output_data



def get_key(selector):
    '''
    확장자가 들어가있는 번호를 리턴해줍니다.
    '''
    for key, dic_value in type_value_dic.items():
        if selector == dic_value:
            return key

    return "There is no such Key"


def copy_each_file(copy_each_class_list, main_source):
    '''
    파일을 하나씩 검사하고 복사합니다.
    '''
    print("=========================================================")
    print("Copy Start")

    list_len = 0
    count = 1

    for class_list_counting in copy_each_class_list:
        list_len += class_list_counting.is_use

    list_len = len(class_list) - list_len

    for class_list_result in copy_each_class_list:
        results = round((count) / list_len, 2) * 100

        if class_list_result.is_use > 0:
            continue

        origin_path = os.sep.join([main_source, class_list_result.output])
        count += 1

        if os.path.isfile(origin_path):
            copy_source = os.path.join("C:", os.sep, "CopyFiles")
            chk_list = class_list_result.output.split("/")

            for chk in chk_list[:-1]:
                copy_source = copy_source + os.sep + chk

            class_list_result.output = class_list_result.output.replace("/", os.sep)
            os.makedirs(copy_source, exist_ok=True)

            try:
                shutil.copy(origin_path, copy_source)

            except BaseException as base_exception:
                print(base_exception)

            finally:
                print("{0:>6.2f}% - {1}".format(results, origin_path))
                log_list.append(origin_path)

        else:
            print("{0:>6.2f}% - {1} 파일이 존재하지 않습니다.".format(results, origin_path))


def copy_file_method(copy_file_class_list, main_source):
    '''
    파일을 하나씩 검사하고 복사합니다.
    '''
    copy_source = os.path.join("C:", os.sep, "CopyFiles")
    os.makedirs(copy_source, exist_ok=True)
    copy_each_file(copy_file_class_list, main_source)
    log_file_name = copy_source + os.sep + "logFile.txt"

    log_file = open(log_file_name, "w")
    for logs in log_list:
        log_file.write(logs + "\n")

    log_file.close()


def filtered_list(not_filtered_list, not_filterd_type_list, not_filtered_type_value_dic):
    '''
    전체 파일에서 사용할껏만 찾게 필터링.
    '''
    selector = 99

    while selector > -1:

        if selector == 8887:
            print("=========================================================")
            print("Full list of files")
            for filter_index, class_list_filter in enumerate(not_filtered_list):
                if class_list_filter.is_use < 1:
                    print("{0} : {1}".format(filter_index, class_list_filter.output))

        print("=========================================================")
        print("Enter the file extension number, if you do not want to copy")
        print("If you want to see Full file list, Enter the 8888")
        print("Enter the 0 button OR JUST PRESS ENTER to start COPY")

        for turples in not_filtered_type_value_dic.items():
            print("{0} : {1}".format(turples[1] + 1, turples[0]))
        try:
            input_data = sys.stdin.readline()
            selector = int(input_data) - 1
        except BaseException as exception:
            print(exception)
            if input_data == "\n":
                selector = -1

        tempnum = get_key(selector)

        if tempnum != "There is no such Key":
            for idx in not_filterd_type_list[not_filtered_type_value_dic[tempnum]]:
                not_filtered_list[idx].is_use = 1

            del not_filtered_type_value_dic[tempnum]
            print("=========================================================")
            print("{0} is excluded.".format(tempnum))

    return not_filtered_list


if __name__ == "__main__":
    type_value_dic = {}
    log_list = []
    print("=========================================================")
    print("SourceTree Copy Start")
    output = os.popen(
        "git diff --name-only --diff-filter=d {0} {1}".format(
            sys.argv[len(sys.argv) - 1], sys.argv[2]
        )
    ).read()
    IDX = 0
    type_list = []
    class_list = []
    outputList = output.splitlines()

    for output_list_index, line in enumerate(outputList):
        class_list_data = ResultData()
        class_list_data.setdata(line)

        while line.find(".") > -1:
            line = line[line.find(".") + 1 :]

        if line not in type_value_dic:
            type_list.append([])
            type_value_dic[line] = IDX
            IDX += 1

        type_list[type_value_dic[line]].append(output_list_index)
        class_list.append(class_list_data)

    class_list = filtered_list(class_list, type_list, type_value_dic)
    basic_main_source = sys.argv[1].replace("\\", os.sep)
    os.chdir(basic_main_source)
    copy_file_method(class_list, basic_main_source)


print("=========================================================")
print("Copy Finished!\nPlease check the logFile of the copied directory.")
os.system("pause")

final_copy_source = os.path.join("C:", os.sep, "CopyFiles")
os.startfile(final_copy_source)
