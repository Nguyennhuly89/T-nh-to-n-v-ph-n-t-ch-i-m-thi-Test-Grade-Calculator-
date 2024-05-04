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
#### Hướng dẫn cài đặt thư viện pandas, numpy

Install pandas

```bash
  pip install pandas
```
Install numpy
```bash
  pip install numpy
```
Trước khi tiếp tục, hãy đảm bảo bạn có thể đáp ứng các yêu cầu sau:

* Bạn đã cài đặt version mới nhất của Python

* Bạn đã install pandas, numpy

## III. Hướng dẫn cài đặt
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
