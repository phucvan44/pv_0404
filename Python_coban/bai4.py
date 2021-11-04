class Date:
    def __init__(self, day, month, year, status):
        self.day = day
        self.month = month
        self.year = year
        self.status = status 
        self.next = None


def get_list_key():
    f = open("kyhieu.txt", "r") # file input
    list_key = {}
    for text_line in f:
        text_line = text_line.split(": ")
        list_key[text_line[0]] = text_line[1].split("\n")[0]
    f.close()
    return list_key


def get_list_date():
    f = open("dubaothoitiet.txt","r")
    list_date = []
    for text_line in f:
        text_line = text_line.split(":")
        text_line[1] = text_line[1].split("\n")[0]
        day,month,year = text_line[0].split("/")
        cur_date = Date(day,month,year,list_key[text_line[1]])
        list_date.append(cur_date)
    f.close()
    return list_date


def find_id_date(cur):
    for i in range(len(list_date)):
        temp = list_date[i]
        if temp.day == cur[0] and temp.month == cur[1] and temp.year == cur[2]:
            return i


if __name__ == "__main__":

    list_key = get_list_key()
    list_date = get_list_date()
    list_check = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

    print("Nhập thứ ngày tháng năm: ",end="")
    line_date = str(input())

    print("Nhập số ngày cần xem: ",end="")
    n_day = int(input())

    line_date = line_date.split(" ")

    today = line_date[0]
    cur_day = line_date[1:]

    id_check = list_check.index(today)+1
    id_day = find_id_date(cur_day)+1

    print("weather forecast for 4 day:")
    for i in range(n_day):
        cur_day = id_day + i 
        cur_check = (id_check+i)%7

        ans = list_check[cur_check] + " - "

        day_ans = list_date[cur_day]

        ans += day_ans.day + "/" + day_ans.month + "/" + day_ans.year + ": " + day_ans.status
        print(ans)
