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

Mỗi tệp dữ liệu chứa một loạt câu trả lời của học sinh. Giá trị đầu tiên là số ID của học sinh, 25 chữ cái sau là câu trả lời của học sinh.


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
