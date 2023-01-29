
file = open("raw_data.txt", "r")

# read first student 
data =file.readline()

# make data become a list 
data = data .split("\\n") 

# remove \t and \n
for i in range(len(data)): 
    data[i] = data[i].replace("\\r","")
    data[i] = data[i].replace("\\t","")

# remove tags 
for i in range(len(data)):
    tags = []
    for x in range(len(data[i])):
        if data[i][x] == "<":
            begin = x
        elif data[i][x] ==">":
            end = x 
            tags.append(data[i][begin:end +1])

    for tag in tags:
        data[i] = data[i].replace(tag,"")

#remove the blank spaces 
unempty_line = []
for z in range(len(data)):
    data[z] = data[z].strip()
    if data[z] != "":
        unempty_line.append(data[z])
data = unempty_line

name = data[7] #  tên cần tìm 
date_of_birth = data [8] #  ngay sinh 
score = data[9] # lay diem 

# change the unicode to the regular letter 

with open("unicode.txt",encoding="utf8") as file:
    uni_table = file.read().split("\n") # bỏ đi ký tự xuống dòng ->>in từng dòng 1 và chung list

chars = [] # hàng đầu tiên (chữ thông thường )
code = [] # chữ code
for codes in uni_table:
    x = codes.split(" ")
    chars.append(x[0])
    code.append(x[1]) 
# replace the code form to the regular 
for i in range(len(chars)):
    name = name.replace(code[i],chars[i])
    score = score.replace(code[i],chars[i])


# đổi các ký tự còn lại 

for i in range(len(name)):
    if name[i:i+2] == "&#": # để lấy ra cái đuôi số (192 195) sau đó dùng hàm chr để chuyển về dạng chữ bth 
        name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:]

for i in range(len(score)):
    if score[i:i+2] == "&#": # để lấy ra cái đuôi số (192 195) sau đó dùng hàm chr để chuyển về dạng chữ bth 
        score = score[:i] + chr(int(score[i+2:i+5])) + score[i+6:] 

name = name.title()
score = score.lower()


dob_list = date_of_birth.split("/")
dd = int(dob_list[0]) # ngay sinh 
mm = int(dob_list[1]) # thang sinh 
yy = int(dob_list[2]) # nam sinh 

#remove the ":" character 



for x in score:
    if x == ":":
        score = score.replace(x,"")
score = score.replace("khxh ","khxh   ")
score = score.replace("khtn ","khtn   ")
score_list = score.split("   ")
print(score_list)



# lấy ra thông tin cần thiết (tên điểm ngày năm sinh)
data = [name,str(dd),str(mm),str(yy)]     

#add score to data 
list_of_subject = ["toán", "ngữ văn", "tiếng anh", "khxh", "khtn", "lịch sử", "địa lý", "gdcd", "vật lý", "hóa học", "sinh học"]
for subject in list_of_subject:
    if subject in score_list: 
        data.append(str(float(score_list[score_list.index(subject) + 1 ])))
    else:
        data.append("-1")
#write data in txt 
file = open("line1.txt", encoding="utf8", mode="w")
for x in range(len(data)):
    file.write(data[x] +", ")



