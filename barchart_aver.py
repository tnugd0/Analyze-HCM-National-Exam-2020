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

number_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0] # list các môn đc chọn để thi (12 TH: thi 0 môn 1 mon ..... )

average = [0,0,0,0,0,0,0,0,0,0,0,0]    # điểm tb của tất cả các hsinh thi 1 môn 2 môn ..... 
for s in students: 
    count = 0 
    total_score = 0 
    for x in range(5,16):
        if s[x] != "-1":
            count += 1 
            total_score += float(s[x]) 
    number_of_exam_taken[count] += 1 # nếu count = 0 thì vị trí đầu của num + 1 là số ng kh th môn nào, tươnng tự vs các môn vs hsinh còn lại
    average[count] += total_score/count # điểm tb tại vị trí hsinh thi bấy nhiêu môn vs count là vị trị của num ( điểm tb = tổng / số môn )
# average = [0,454,847,17102..... ] tổng điểm tb của tất cả hhsinh thi 1 môn,2 môn,..... 

# tính điểm tb của mỗi thí sinh trong dsach 
for x in range(12):
    if average[x] == 0:
        continue
    else:
        average[x] = round(average[x] / number_of_exam_taken[x],2 ) # điểm tb của mỗi hsinh ở mỗi nhóm thi bnh môn 

#make chart 
import matplotlib.pyplot as plt
import numpy as np # tvien numpy dùng để xử lý các list 

x = np.arange(12) #dsach từ 0 đến 12 
y = np.arange(12)

figure, axis = plt.subplots() # tạo ra 1 plot 


y_pos = np.arange(len(number_of_exam_taken)) # tạo dsach với độ dành 0 - 11 
#create barchart 
# dài của ox vs oy = nhau
plt.bar(y_pos, average) # tạo ra kiểu chart là bar 
plt.xticks(y_pos,y ) # thay thế số thành dsach subject 

axis.set_ylim(0,10) # set cột oy giới hạn từ 0 - 100 
plt.ylabel('điểm trung bình')
plt.title('điêm tbinh của các nhóm thi')

# draw number of students on top of each bar 
rects = axis.patches
for rect, label in zip(rects, average):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom")
plt.show() 