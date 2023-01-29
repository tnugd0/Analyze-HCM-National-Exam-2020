# bắt đầu tạo các chart 
with open("final_process.txt",encoding="utf8") as file: 
    data = file.read().split("\n")
header = data[0]
students = data [1:]
total_student =  len(students)

# remove the last student (empty student) file final_process có dòng cuối trống nên kh thực hiện đc for ở dưới
students.pop() # pop() mặc định bỏ thằng cuối dsach 

#split the header 
header = header.split(",")
subjects = header[5:] # liệt kê cacs môn học 


#split student with their score,..... 
for x in range(len(students)):
    students[x] = students[x].split(",")

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0] # dsach cacs môn mà hsinh kh chọn (tổng có 11 môn)

for s in students:  # s là từng điểm ttin của từng hsinh 
    for i in range(5,16): # 5 đến 16 là tâts cả các môn bắt đầu tú toán (0 - 4 là sbd tên năm sinh .... )
        # lieejt ke cacs mon kh đc thi sinh chon 
        if s[i] == "-1":
            not_take_exam[i-5]+= 1 # vd khi i = 5 thì ứng với not_take_exam[0] ( môn đầu tiên) nên phải trừ 5         

# tính từng phần trăm các môn kh đc thi so với tổng só hsinh 
not_take_exam_per  = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,11):
    not_take_exam_per[i] = round(not_take_exam[i] *100/total_student, 2 ) # hàm round để làm tròn (,2 laasy 2 chữ số sau phần thập phân)
print(not_take_exam_per)
print(subjects)
print(not_take_exam)

#make chart 
import matplotlib.pyplot as plt
import numpy as np # tvien numpy dùng để xử lý các list 

figure, axis = plt.subplots() # tạo ra 1 plot 

y_pos = np.arange(len(subjects)) # tạo dsach với độ dành 0 - 11 
#create barchart 
# dài của ox vs oy = nhau
plt.bar(y_pos, not_take_exam_per) # tạo ra kiểu chart là bar 
plt.xticks(y_pos, subjects) # thay thế số thành dsach subject 

axis.set_ylim(0,100) # set cột oy giới hạn từ 0 - 100 
plt.ylabel('percentage')
plt.title('số hsinh bỏ thi hoặc kh đky ')

# draw number of students on top of each bar 
rects = axis.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom")
plt.show()