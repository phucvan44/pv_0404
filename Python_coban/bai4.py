class date:
    def __init__(seft,day,month,year,status):
        seft.day = day
        seft.month = month
        seft.year = year
        seft.status = status 
        seft.next = None

f = open("kyhieu.txt", "r") # file input
list_key = {}
for text_line in f:
    text_line = text_line.split(": ")
    list_key[text_line[0]] = text_line[1].split("\n")[0]
f.close()

f = open("dubaothoitiet.txt","r")
list_date = []
for text_line in f:
    text_line = text_line.split(":")
    text_line[1] = text_line[1].split("\n")[0]
    day,month,year = text_line[0].split("/")
    cur_date = date(day,month,year,list_key[text_line[1]])
    list_date.append(cur_date)
f.close()

def find_id_date(cur):
    for i in range(len(list_date)):
        temp = list_date[i]
        if temp.day == cur[0] and temp.month == cur[1] and temp.year == cur[2]:
            return i



if __name__ == "__main__":
    list_check = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]


    print("Nhập thứ ngày tháng năm: ",end="")
    s = str(input())

    print("Nhập số ngày cần xem: ",end="")
    n = int(input())

    s = s.split(" ")

    today = s[0]
    cur_day = s[1:]

    id_check = list_check.index(today)+1
    id_day = find_id_date(cur_day)+1

    print("weather forecast for 4 day:")
    for i in range(n):
        cur_day = id_day + i 
        cur_check = (id_check+i)%7
        ans = list_check[cur_check] + " - "
        day_ans = list_date[cur_day]
        ans += day_ans.day + "/" + day_ans.month + "/" + day_ans.year + ": " + day_ans.status
        print(ans)


