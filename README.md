# Tính toán và phân tích điểm thi (Test Grade Calculator)

Chào mừng bạn đến với hướng dẫn dự án Tính toán và phân tích điểm thi. Sau đây là một số chia sẻ, hướng dẫn của mình về dự án.

## Mục lục
I. Tổng quan về dự án

II. Một vài lưu ý

III. Hướng dẫn cài đặt

IV. Nội dung hướng dẫn

## I. Tổng quan về dự án

Dự án cần viết một chương trình để tính toán điểm thi cho nhiều lớp với sĩ số hàng nghìn học sinh. Mục đích của chương trình giúp giảm thời gian chấm điểm. Dự án sẽ áp dụng các functions khác nhau trong Python để viết chương trình.
## II. Một vài lưu ý
Trước khi tiếp tục, hãy đảm bảo bạn có thể đáp ứng các yêu cầu sau:

* Bạn đã cài đặt version mới nhất của Python

* Bạn đã install pandas, numpy

## III. Hướng dẫn cài đặt
#### Hướng dẫn cài đặt thư viện pandas, numpy

Install pandas

```bash
  pip install pandas
```
Install numpy
```bash
  pip install numpy
```

## IV. Nội dung hướng dẫn

Chương trình sẽ thực hiện với các tác vụ sau:

1. Mở các tập tin văn bản bên ngoài

2. Quét từng dòng của câu trả lời bài thi để tìm dữ liệu hợp lệ và cung cấp báo cáo tương ứng

3. Chấm điểm từng bài thi dựa trên tiêu chí đánh giá (rubic) được cung cấp và báo cáo

4. Tạo tập tin kết quả được đặt tên thích hợp

Dự án yêu cầu thực hiện các tác vụ trên với các hàm functions trong Python và thực hiện chỉ với pandas và numpy

Đầu tiên, mình sẽ hướng dẫn thực hiện dự án với các hàm functions trong Python.

### Task 1 : Mở các tập tin văn bản bên ngoài
Ta viết một chương trình cho phép người dùng nhập tên một tệp và truy cập đọc. Thông báo xác nhận cho người dùng biết tệp có tồn tại hay không. Nếu tệp không tồn tại cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ. Dùng try/except để thực hiện việc này.

Trước tiên, tạo list filename chứa tên các tệp đang cần tính điểm

```bash
filename = ['class1', 'class2','class3','class4','class5','class6','class7','class8']
```

List tên đường dẫn đang lưu các tệp để lấy dữ liệu

```bash
path = 'E:\Lap DSP301\ASM\data-files\Data Files'
```
Tạo hàm thông báo xác nhận tệp có tồn tại hay không

```bash
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
```

### Task 2 : Quét từng dòng của câu trả lời bài thi để tìm dữ liệu hợp lệ và cung cấp báo cáo tương ứng

Mỗi tệp dữ liệu chứa một loạt câu trả lời của học sinh. Giá trị đầu tiên là số ID của học sinh, 25 chữ cái sau là câu trả lời của học sinh. Tất cả các giá trị được phân tách bằng dấu phẩy. Nếu không có chữ cái nào sau dấu phẩy, điều này có nghĩa là học sinh đã bỏ qua việc trả lời câu hỏi.


Một dòng hợp lệ chứa danh sách 26 giá trị được phân tách bằng dấu phẩy. N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự "N" và theo sau là 8 ký tự số.

Trước tiên, ta cần tạo hàm check dữ liệu và loại bỏ các dữ liệu không hợp lệ. Kết quả của hàm trả về list các dòng dữ liệu hợp lệ.

```bash
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
```

Tiếp theo, ta tạo hàm in ra các báo cáo thống kê theo yêu cầu dự án.

* Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp.

* Báo cáo tống số dòng không hợp lệ trong tệp.

* In ra thông báo lỗi nếu dòng dữ liệu không hợp lệ.

```bash
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
```
Dưới đây là mẫu chạy chương trình cho tệp dữ liệu đầu tiên

```bash
Enter a class file to grade (i.e. class1 for class1.txt):class1
Sucessfully opened class1.txt

**** ANALYZING ****

No errors found!

**** REPORT ****

Total valid lines of data: 20
Total invalid lines of data: 0
```
Và mẫu chạy chương trình cho tệp dữ liệu thứ 2

```bash
Enter a class file to grade (i.e. class1 for class1.txt):class2
Sucessfully opened class2.txt

**** ANALYZING ****

Invalid line of data: does not contain exactly 26 values: 
 N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A

Invalid line of data: N# is invalid 
 N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D

Invalid line of data: N# is invalid 
 NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D

Invalid line of data: does not contain exactly 26 values: 
 N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A


**** REPORT ****

Total valid lines of data: 21
Total invalid lines of data: 4
```
### Task 3: Chấm điểm từng bài thi dựa trên tiêu chí đánh giá (rubic) được cung cấp và báo cáo

Trước tiên, ta tạo list các đáp án cho các câu hỏi

```bash
answer_key = ['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B',
              'D','A','C','A','A','B','D','D']
```

Tạo hàm tính điểm cho mỗi học sinh trong tệp dữ liệu. Hàm trả về list điểm cho mỗi câu trả lời của học sinh. Điểm được tính như sau:

* +4 điểm cho mỗi câu trả lời đúng

* 0 điểm cho mỗi câu trả lời bị bỏ qua. 

* -1 cho mỗi câu trả lời sai

```bash
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
```
Ta cần thống kê các thông tin bên dưới theo yêu cầu của dự án:

3.1 Đếm số lượng học sinh đạt điểm cao (>80)

3.2 Điểm trung bình

3.3 Điểm cao nhất

3.4 Điểm thấp nhất

3.5 Miền giá trị của Điểm

3.6 Giá trị trung vị của điểm

Để tính trung vị của điểm, ta cần xây dựng hàm tính trung vị. Trước tiên ta sắp xếp điểm theo thứ tự tăng dần, nếu số học sinh là số lẻ, trung vị là giá trị nằm giữa của tất cả các điểm. Nếu số học sinh là số chẵn, giá trị trung vị là trung bình của 2 giá trị ở giữa.

```bash
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
```
Tiếp theo, sẽ xây dựng hàm để chấm điểm tự động và thống kê các thông tin theo yêu cầu dự án.

```bash
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
```

Kết quả của hàm sẽ trả về các giá trị thống kê như bên dưới khi ta tính điểm tự động cho tệp dữ liệu đầu tiên:

```bash
Total student of high score: 6
Mean score: 75.6
Lowest score: 59
Highest score: 91
Range of score: 32
Median score: 73.0
```

Với các yêu cầu thống kê ở mục 3.7 và 3.8 của dự án, ta xây dựng hàm tính toán và thống kê các dữ liệu

3.7 Trả về các câu hỏi bị học sinh bỏ qua nhiều nhất

Trước tiên, ta tạo hàm tập hợp các câu hỏi bị học sinh bỏ qua. 

```bash
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
```
Sau đó ta tìm các câu hỏi bị bỏ qua nhiều nhất và thống kê. Dùng set để tạo list không lặp lại các câu hỏi bị bỏ qua. Tạo dict để tìm được câu hỏi có số lần bỏ qua nhiều nhất.

```bash
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
```

3.8 Trả về các câu hỏi bị học sinh sai qua nhiều nhất.

Tương tự mục 3.7, ta cũng sẽ tạo hàm để tính toán và thống kê. Trước tiên, tập hợp các câu hỏi bị trả lời sai, sau đó sort dữ liệu để tìm câu hỏi bị sai nhiều nhất

Hàm trả về các câu hỏi bị trả lời sai:

```bash
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
```

Hàm tìm câu trả lời sai nhiều nhất và thống kê:

```bash
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
```

Dưới đây là mẫu khi chương trình chạy các hàm để thống kê dữ liệu cho mục 3.7 và 3.8 của tệp dữ liệu đầu tiên
```bash
Questions that most people skip:

- Question: 3 
- Student quantity skip question: 4 
- Rate: 0.2

- Question: 5 
- Student quantity skip question: 4 
- Rate: 0.2

- Question: 23 
- Student quantity skip question: 4 
- Rate: 0.2
Questions that most people answer incorrectly:

- Question: 10 
- Student quantity has incorrect answer: 4 
- Rate: 0.2

- Question: 14 
- Student quantity has incorrect answer: 4 
- Rate: 0.2

- Question: 16 
- Student quantity has incorrect answer: 4 
- Rate: 0.2

- Question: 19 
- Student quantity has incorrect answer: 4 
- Rate: 0.2

- Question: 22 
- Student quantity has incorrect answer: 4 
- Rate: 0.2
```
### Task 4: Tạo tập tin kết quả được đặt tên thích hợp
Ở task này, dự án yêu cầu tạo ta một tệp kết quả chứa các kết quả chi tiết của từng học sinh trong lớp. Mỗi dòng của tệp chứa ID của học sinh, dấu phẩy và sau đó là điểm của họ.

Để thực hiện yêu cầu, trước tiên ta sẽ tạo hàm để tính tổng điểm cho mỗi học sinh. Tạo dict lưu trữ thông tin ID và tổng điểm của mỗi học sinh.

```bash
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
```
Sau đó xây dựng hàm để lưu kết quả và tệp dữ liệu.
```bash
def result(file):
    path = 'E:\Lap DSP301\ASM\data-files\Result' # Đường dẫn lưu dữ liệu file kết quả
    result = sum_score(file)
    if file in filename:
        with open (path + '\\' + file + '_grades.txt', 'w') as wf:
            for key in result:
                wf.write(key + ','+ str(result[key]) + '\n')
    else:
        print('Errors')
```

Cuối cùng, thực hiện lệnh thực thi các hàm đã xây dựng ở trên để hoàn thành dự án.
```bash
if __name__ == '__main__':
    input_file(file)
    print('\n**** ANALYZING ****\n')
    check_data(file)
    score_check(file)
    no_ans_sort(file)
    wrong_ans_sort(file)
    result(file)
```
Đây là kết quả của chương trình thi thực thi với tệp dữ liệu thứ 2:
```bash
Enter a class file to grade (i.e. class1 for class1.txt):class2
Sucessfully opened class2.txt

**** ANALYZING ****

Invalid line of data: does not contain exactly 26 values: 
 N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A

Invalid line of data: N# is invalid 
 N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D

Invalid line of data: N# is invalid 
 NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D

Invalid line of data: does not contain exactly 26 values: 
 N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A


**** REPORT ****

Total valid lines of data: 21
Total invalid lines of data: 4

Total student of high score: 7
Mean score: 78.0
Lowest score: 66
Highest score: 100
Range of score: 34
Median score: 76
Questions that most people skip:

- Question: 22 
- Student quantity skip question: 6 
- Rate: 0.286
Questions that most people answer incorrectly:

- Question: 18 
- Student quantity has incorrect answer: 5 
- Rate: 0.238
```
File kết quả của tệp 2
```bash
N00000021,68
N00000022,76
N00000024,73
N00000026,72
N00000028,73
N00000029,87
N00000030,82
N00000031,76
N00000032,87
N00000033,77
N00000034,69
N00000036,77
N00000037,75
N00000038,73
N00000039,66
N00000040,73
N00000041,91
N00000042,100
N00000043,86
N00000044,90
N00000045,67
```
Như vậy mình đã hướng dẫn các bạn hoàn thành dự án bằng cách sử dụng các hàm functions trong Python.
