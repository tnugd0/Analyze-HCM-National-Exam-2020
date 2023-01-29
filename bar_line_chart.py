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

# dsach nhoms tuổi của hsinh từ 17t đến trên 26t 
number_of_student_per_age = [0,0,0,0,0,0,0,0,0,0,0] 

 # dsach tổng các điểm tb của từng nhóm tuổi
aver_grade_students_per_age = [0,0,0,0,0,0,0,0,0,0,0] 

for x in students: 
    # xác định tuổi của hsinh 
    age = 2020 - int(x[4])
    if age >= 27: # trên 27t quy hết về 27 
        age = 27 
    number_of_student_per_age[age - 17] += 1 
    sum_score = 0 # tổng điểm của tất cả các môn thi 
    count_score = 0 # thi bao nhiêu môn 
    # lọc 11 môn học của hsinh đấy 
    for s in range(5,16): # có 11 môn học môn toán bắt đầu ở vị trí thứ 5  
        if x[s] != "-1":
            count_score += 1 # có thi nên cộng một 
            sum_score += float(x[s])
    average = sum_score/count_score
    aver_grade_students_per_age[age-17] += average 
for x in range(11):
    aver_grade_students_per_age[x] = round(aver_grade_students_per_age[x] / number_of_student_per_age[x] ,2)

# scale gtri của điểm tb để vẽ ghép vào trục 
for y in range(len(aver_grade_students_per_age)):
    aver_grade_students_per_age[y] = aver_grade_students_per_age[y] * 7000 


# create barchart
import matplotlib.pyplot as plt
import numpy as np # tvien numpy dùng để xử lý các list 

x = np.arange(11) #dsach từ 0 đến 11
y = np.arange(11)

figure, axis = plt.subplots() # tạo ra 1 plot 

ages =["17","18","19","20","21","22","23","24","25","26",">27"]
 # tạo dsach với độ dành 0 - 11 
#create barchart 
# dài của ox vs oy = nhau
plt.bar(x, number_of_student_per_age) # tạo ra kiểu chart là bar 

# vẽ line chart 
plt.plot(x, aver_grade_students_per_age, color="red", marker="x") # dùng plot() để vẽ line chart, marker =>>> để đấnh dấu gtri 

plt.xticks(x,ages) # thay thế số thành dsach subject 

axis.set_ylim(0,72000) # set cột oy giới hạn từ 0 - 100 
plt.ylabel('số hsinh dky thi') # tiêu đề cho trục oy bên trái 
plt.xlabel("Tuổi")
plt.title('điểm tb của từng độ tuổi')

# right sight ticks 
axis2 = axis.twinx() # tao them truc oy nx 
axis2.tick_params("y",colors="red")
axis2.set_ylabel("điểm trung bình") # thêm tiêu đề cho cho cột bên phải  
axis2.set_ylim(0,10)

# thêm giá trị vào cho mỗi cột
rects = axis.patches # vẽ các bar theo hình chữ nhật    
for rect, label in zip(rects, number_of_student_per_age):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom")
plt.show() 