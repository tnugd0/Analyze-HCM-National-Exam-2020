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

for s in students: 
    count = 0 
    for x in range(5,16):
        if s[x] != "-1":
            count += 1 
    number_of_exam_taken[count] += 1 # nếu count = 0 thì vị trí đầu của num + 1 là số ng kh th môn nào, tươnng tự vs các môn vs hsinh còn lại
print(number_of_exam_taken)

# create piechart 
import matplotlib.pyplot as plt
number_of_exam_taken_per = [0,0,0,0,0,0,0,0,0,0,0,0]
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
number_of_exam = ["0","1","2","3","4","5","6","7","8 ","9","10 ","11"]
for x in range(1,11):
    number_of_exam_taken_per[x] = number_of_exam_taken[x]*100/len(students)

explode = (0, 0.1,0, 0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
sizes = [0, 80, 122, 2598, 4334, 318, 2730, 64261, 0, 0, 0, 1] # phần trăm các môn đc chọn 
fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=explode,labels=number_of_exam, autopct='%1.1f%%',shadow=True, startangle=90)  

# explode: dùng để cho 1 phần nhô ra ngoài, label là tên các phần trong pie chart
# startangle:  bắt đầu vẽ từ trục dọc góc 90 
#autopct:thêm ký hiệu phần trăm
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()