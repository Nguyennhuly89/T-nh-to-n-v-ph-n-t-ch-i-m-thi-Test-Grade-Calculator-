import numpy as np
import pandas as pd


filename = ['class1', 'class2','class3','class4','class5','class6','class7','class8']
file = input('Enter a class file to grade (i.e. class1 for class1.txt):')
path = 'D:\DSP301\ASM\Data Files'
answer_key = ['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B',
              'D','A','C','A','A','B','D','D']

#Task 1: Nguoi dung nhap ten cua mot tep va truy cap doc
# Code thông báo xác nhận file tồn tại hay không
def input_file(file):
    try:
        if file in filename:
            with open(path + '\\' + file + '.txt', 'r') as f:
                print('Sucessfully opened '+ file +'.txt')
                content = f.read()
        else:
            print('Files can not be found. Please check filename again')
    except:
        print('Errors have been occurred.')

# Task 2:
# Code check data và in báo cáo số dòng hợp lệ và không hợp lệ trong tệp
def check_data(file):
    sum = 0
    count_row = 0
    if file in filename:
        with open (path+ '\\' +file + '.txt' ,'r') as f:
            content = f.readlines()
            for line in content:
                count_row +=1
            for line in content:
                list_check =list(line.strip().split(','))
                if len(list_check) != 26:
                    print('Invalid line of data: does not contain exactly 26 values: \n', line)
                elif len(list_check[0]) != 9 or 'N' not in list_check[0] or list_check[0][1:].isnumeric()== False:
                    print('Invalid line of data: N# is invalid \n',line)
                else:
                    sum +=1
            if sum == count_row:
                print('No errors found!')
        print('\n**** REPORT ****\n')
        if sum == count_row:
            print('Total valid lines of data:',count_row)
            print('Total invalid lines of data:', count_row - sum)
        else:
            print('Total valid lines of data:',sum)
            print('Total invalid lines of data:', count_row - sum)
    else:
        print('Errors')

# Hàm tính trung vị
def median(x):
    n = len(x)
    sorted_x = sorted(x)
    midpoint = n//2
    if n%2 == 1:
        return sorted_x[midpoint]
    else:
        low = midpoint - 1
        high = midpoint
        return (sorted_x[low] + sorted_x[high])/2

# Code check dữ liệu loại bỏ dữ liệu không hợp lệ
def check_data2(file):
    invalid_line = []
    valid_line = []
    if file in filename:
        with open (path+ '\\' +file + '.txt' ,'r') as f:
            content = f.readlines()
            # Check dữ liệu để loại dữ liệu không hợp lệ
            for line in content:
                list_check =list(line.strip().split(','))
                if len(list_check) != 26:
                    invalid_line.append(line)
                elif len(list_check[0]) != 9 or 'N' not in list_check[0] or list_check[0][1:].isnumeric()== False:
                    invalid_line.append(line)
                else:
                    valid_line.append(line)
            return valid_line
    else:
        print('Errors')

# Task 3
# Code chấm điểm thi và thống kê
def score_check(file):
    score_list = {}
    highscore_list = []
    valid_line = check_data2(file)
    if file in filename:
        for line in valid_line:
            valid_list = list(line.strip().split(','))
            # Tính điểm cho từng học sinh
            for line in valid_list:
                i = 0
                score = []
                for a in valid_list[1:]:
                    if a == '':
                        score.append(0)
                        i += 1
                    elif a == answer_key[i]:
                        score.append(4)
                        i += 1
                    elif a != answer_key[i]:
                        score.append(-1)
                        i +=1
                score_list.setdefault(valid_list[0],sum(score))  #Tạo dict tập hợp điểm số
        #Code thống kê số lượng học sinh đạt điểm cao (>80)
        for values in score_list.values():
            if values > 80:
                highscore_list.append(values)
            else: continue
        # Số lượng học sinh đạt điểm cao
        print('\nTotal student of high score:', len(highscore_list))
        # Điểm trung bình
        print('Mean score:', round(sum(score_list.values())/len(score_list.values()),3))
        # Điểm thấp nhất
        print('Lowest score:', min(score_list.values()))
        # Điểm cao nhất
        print('Highest score:',max(score_list.values()))
        # Miền giá trị của điểm
        print('Range of score:', max(score_list.values()) - min(score_list.values()))
        # Giá trị trung vị của điểm
        print('Median score:', round(median(score_list.values()),3))
    else:
        print('Errors')

# Tính điểm cho mỗi học sinh
def scores(file):
    i = 0
    score = []
    for a in file[1:]:
        if a == '':
            score.append(0)
            i += 1
        elif a == answer_key[i]:
            score.append(4)
            i += 1
        elif a != answer_key[i]:
            score.append(-1)
            i += 1
    return score

#Tập hợp list các câu hỏi bị học sinh bỏ qua
def no_ans(file):
    try:
        no_ans = []
        valid_line = check_data2(file)
        for line in valid_line:
            valid_list = list(line.strip().split(','))
            i = 1
            for ans in valid_list[1:]:
                if ans == '':
                    no_ans.append(i)
                    i += 1
                else:
                    i += 1
        return no_ans
    except:
        print('Errors')

#Code tính thứ tự các câu hỏi bị bỏ qua nhiều nhất
def no_ans_sort(file):
    try:
        no_ans_list = no_ans(file)
        no_ans_set = set(no_ans_list)
        question_list = []
        no_answer_times = []
        for i in no_ans_set:
            question_list.append(i)
            no_answer_times.append(no_ans_list.count(i))
        no_ans_dict = dict(zip(question_list, no_answer_times))
        print('Questions that most people skip:')
        for key in no_ans_dict.keys():
            if no_ans_dict[key] == max(no_answer_times):
                print('\n- Question:', key ,'\n- Student quantity skip question:', no_ans_dict[key], '\n- Rate:',
                    round(no_ans_dict[key]/len(check_data2(file)),3))
            else: continue
    except:
        print('Errors')

# Tập hợp list các câu hỏi bị sai
def wrong_ans(file):
    try:
        wrong_ans = []
        scores_list = check_data2(file)
        for line in scores_list:
            i = 1
            wrong_list = list(line.strip().split(','))
            for a in scores(wrong_list):
                if a == -1:
                    wrong_ans.append(i)
                    i += 1
                else:
                    i += 1
        return wrong_ans
    except:
        print('Errors')

#Tính thứ tự các câu hỏi bị sai nhiều nhất:
def wrong_ans_sort(file):
    try:
        wrong_ans_list = wrong_ans(file)
        wrong_ans_set = set(wrong_ans_list)
        wrong_list = []
        wrong_times = []
        for i in wrong_ans_set:
            wrong_list.append(i)
            wrong_times.append(wrong_ans_list.count(i))
        wrong_dict = dict(zip(wrong_list, wrong_times))
        print('Questions that most people answer incorrectly:')
        for key in wrong_dict.keys():
            if wrong_dict[key] == max(wrong_times):
                print('\n- Question:', key, '\n- Student quantity has incorrect answer:', wrong_dict[key],
                      '\n- Rate:', round(wrong_dict[key]/len(check_data2(file)),3))
            else: continue
    except:
        print('Errors')
# Tính tổng điểm của mỗi học sinh
def sum_score(file):
    score_list = {}
    valid_line = check_data2(file)
    if file in filename:
        for line in valid_line:
            valid_list = list(line.strip().split(','))
            for line in valid_list:
                scores(valid_list)
            score_list.setdefault(valid_list[0],sum(scores(valid_list)))
        return score_list
    else:
        print('Errors')

# Task 4
# Tạo ra tệp kết quả chứa các kết quả chi tiết của từng học sinh trong lớp
def result(file):
    path = 'D:\DSP301\ASM\Result'
    result = sum_score(file)
    if file in filename:
        with open (path + '\\' + file + '_grades.txt', 'w') as wf:
            for key in result:
                wf.write(key + ','+ str(result[key]) + '\n')
    else:
        print('Errors')

if __name__ == '__main__':
    input_file(file)
    print('\n**** ANALYZING ****\n')
    check_data(file)
    score_check(file)
    no_ans_sort(file)
    wrong_ans_sort(file)
    result(file)

#Task 5 chỉ dùng Pandas và numpy khi triển khai task 1 đến task 4
    #Task 1: người dùng nhập tên của tệp và truy cập đọc
    # Xác nhận file có tồn tại hay không
try:
    if file in filename:
        df = pd.read_csv(path + '\\' + file + '.txt', sep='\t', header=None, on_bad_lines='skip')
        print('Sucessfully opened ' + file + '.txt')
    else:
        print('Files can not be found. Please check filename again')
    # Đọc file với sep = '' để tránh lỗi không lấy hết dữ liệu của file
    #(với những dòng có nhiều cột hơn chuẩn)
    df = pd.read_csv(path + '\\' + file + '.txt', sep='\t',header=None, on_bad_lines='skip')
    # Tách dữ liệu theo cột
    df = df[0].str.split(',',expand = True)
    # Tạo cột check số ký tự ID number
    df['Check ID Character'] = df[0].apply(lambda x: len(x))
    # Tạo cột check ID có hợp lệ hay không, ID hợp lệ là phải chứa ký tự "N" theo sau là 8 ký tự số
    # Tạo hàm kiểm tra các ký tự có phải là số hay không
    def check_ID(x):
        try:
            int(x)
            return 'OK'
        except:
            return 'NG'
    df['Check regular ID '] = df[0].apply(lambda x:x[1:])
    df['Check regular ID '] = df['Check regular ID '].apply(lambda x: check_ID(x))
    # Tính thêm 2 cột vừa tạo, 1 dòng hợp lệ sẽ có 28 giá trị, khác 28 thì sẽ không hợp lệ
    df[df.count(axis=1)>28]
    df[df.count(axis=1)<28]
    #Task 2: thống kê dữ liệu
    # Tạo dataframe tập hợp dữ liệu không hợp lệ và in dữ liệu không hợp lệ
    invalid_value1 = df[df.count(axis=1)>28]
    invalid_value2 = df[df.count(axis=1)<28]
    invalid_value = pd.concat([invalid_value1, invalid_value2],axis=0)
    invalid_id1 = df[(df['Check ID Character']!=9) | ~(df[0].str.startswith('N'))]
    invalid_id2 = df[df['Check regular ID ']=='NG']
    invalid_id = pd.concat([invalid_id1, invalid_id2],axis = 0)
    print('\n**** ANALYZING ****\n')
    if invalid_id.shape[0] == 0 and invalid_value.shape[0] == 0:
        print('No errors found!')
    else:
        for i in range(invalid_value.shape[0]):
            arr = np.array(invalid_value.iloc[i,:invalid_value.shape[1]-2])
            b = np.sum(arr == None)
            arr = np.array(invalid_value.iloc[i, :invalid_value.shape[1] - 2 - b])
            print('Invalid line of data: does not contain exactly 26 values: \n',arr.tolist())
        for a in range(invalid_id.shape[0]):
            arr_id = np.array(invalid_id.iloc[a,: invalid_id.shape[1]-2])
            c = np.sum(arr_id == None)
            arr_id = np.array(invalid_id.iloc[a, : invalid_id.shape[1] - 2 - c])
            print('Invalid line of data: N# is invalid \n',arr_id.tolist())
    print('\n**** REPORT ****\n')
    print('Total valid lines of data:', df.shape[0] - invalid_id.shape[0] - invalid_value.shape[0])
    print('Total invalid lines of data:', invalid_value.shape[0] + invalid_id.shape[0])
    # Task 3: thống kê điểm cho từng lớp
    # Lấy các dữ liệu hợp lệ từ tệp
    valid_line = df[(df['Check regular ID ']=='OK') & (df['Check ID Character']==9)
                    & (df.count(axis=1)==28) & df[0].str.startswith('N')]
    #Tạo từ điển lưu trữ điểm cho các câu hỏi của mỗi học sinh
    ID_list = list(valid_line[0])
    score_list = []
    for i in range(valid_line.shape[0]):
        arr = np.array(valid_line.iloc[i,:26])
        i = 0
        scores = []
        for a in arr[1:]:
            if a == answer_key[i]:
                scores.append(4)
                i += 1
            elif a == '':
                scores.append(0)
                i += 1
            else:
                scores.append(-1)
                i += 1
        score_list.append(scores)
    scores_dict = dict(zip(ID_list,score_list))
    # Tạo dataframe từ dict lưu trữ điểm
    score_df = pd.DataFrame.from_dict(scores_dict, orient='index')
    #Tạo thêm cột tính tổng điểm của mỗi học sinh
    score_df['Total scores'] = (score_df.sum(axis=1))
    #Lấy số lượng các học sinh đạt điểm cao (Total scores >80)
    high_score = score_df[score_df['Total scores']>80]
    print('\nTotal student of high score:', high_score.shape[0])
    #Tính điểm trung bình của lớp
    mean_score = score_df['Total scores'].mean()
    print('Mean score:', round(mean_score,3))
    #Tính điểm thấp nhất
    lowest_score = score_df['Total scores'].min()
    print('Lowest score:', lowest_score)
    #Tính điểm cao nhất
    highest_score = score_df['Total scores'].max()
    print('Highest score:',highest_score)
    #Tính miền giá trị của điểm
    print('Range of score:', highest_score - lowest_score)
    #Tính giá trị trung vị của điểm
    median_score = score_df['Total scores'].median()
    print('Median score:', round(median_score,3))
    #Tạo dataframe lưu trữ số lượng các câu hỏi bị bỏ qua
    skip_questions = list((score_df == 0).sum())
    skip_dict = dict(zip(range(1,26),skip_questions))
    skip_df = pd.DataFrame.from_dict(skip_dict, orient='index')
    # In các câu hỏi bị bỏ qua nhiều nhất
    print('Questions that most people skip:')
    for i in range(skip_df.shape[0]):
        if skip_df.iloc[i,0] == skip_df[0].max():
            print('\n- Question:', i + 1,
                  '\n- Student quantity skip question:', skip_df.iloc[i,0],
                  '\n- Rate:', round(skip_df.iloc[i,0]/valid_line.shape[0],3))
        else:
            continue
    # Tạo dataframe lưu trữ số lượng các câu hỏi trả lời sai
    incorrect_ans = list((score_df == -1).sum())
    incorrect_dict = dict(zip(range(1,26), incorrect_ans))
    incorrect_df = pd.DataFrame.from_dict(incorrect_dict,orient='index')
    #In các câu hỏi bị trả lời sai nhiều nhất
    print('Questions that most people answer incorrectly:')
    for i in range(incorrect_df.shape[0]):
        if incorrect_df.iloc[i,0] == incorrect_df[0].max():
            print('\n- Question:', i + 1,
                  '\n- Student quantity has incorrect answer:', incorrect_df.iloc[i,0],
                  '\n- Rate:', round(incorrect_df.iloc[i,0]/valid_line.shape[0],3))
        else:
            continue
    #Task 4: Lưu trữ kết quả vào tệp
    path = 'D:\DSP301\ASM\Result'
    result_df = score_df.iloc[:,-1]
    result_df.to_csv(path + '\\' + file + '_grades.txt', sep = ',',header = False)
except:
    print('Errors')













































