class Employee:
    def __init__(self, name, birth, position, skill, start, language, project,id):
        self.name = name
        self.birth = birth 
        self.position = position
        self.skill = skill
        self.start = start
        self.language = language
        self.project = project
        self.id = id
class Leader:
    List_Employee = []
    def __init__(self, n):
        self.List_Employee = [0]*n
    
    def Enter_Employee(self, id):
        print("Nhập thông tin nhân viên thứ {0}:".format(str(id)))

        print("Nhập họ và tên nhân viên: ",end="")
        name = str(input())
        
        print("Nhập năm sinh: ",end="")
        birth = int(input())
        
        print("Vị trí công việc hiện tại: ",end="")
        position = str(input())

        print("Năm bắt đầu công việc: ", end="")
        start = int(input())

        print("Số kĩ năng hiện có: ",end="")
        n_skill = int(input())
        list_skill = []
        for i in range(n_skill):
            print("\tNhập kĩ năng {0}: ".format(str(i+1)), end="")
            sub_skill = str(input()).split("\n")[0]
            list_skill.append(sub_skill)
        
        print("Số lượng ngôn ngữ lập trình đã dùng: ",end="")
        n_language = int(input())
        list_language = []
        for i in range(n_language):
            print("\tNhập ngôn ngữ {0}: ".format(str(i+1)), end="")
            sub_language = str(input()).split("\n")[0]
            list_language.append(sub_language)
        
        print("Số lượng project đã hoàn thành: ",end="")
        n_project = int(input())
        list_project = []
        for i in range(n_project):
            print("\tNhập project đã hoàn thành {0}: ".format(str(i+1)), end="")
            sub_project = str(input()).split("\n")[0]
            list_project.append(sub_project)
        
        employee = Employee(name, birth, position, list_skill, start, list_language, list_project, id)
        self.List_Employee[id-1] = employee
    
    def Get_Employee(self, n):
        if n == 0:
            for i in range(len(self.List_Employee)):
                employee = self.List_Employee[i] 
                print("Nhân viên thứ {0}".format(str(i+1)))
                print("\tSố thứ tự: {0}".format(employee.id))
                print("\tHọ và tên: {0}".format(employee.name))
                print("\tNăm sinh: {0}".format(employee.birth))
                print("\tVị trí công việc hiện tại: {0}".format(employee.position))
                print("\tCác kĩ năng: {0}".format(", ".join(employee.skill)))
                print("\tNăm bắt đầu công việc: {0}".format(employee.start))
                print("\tCác ngôn ngữ lập trình đã dùng: {0}".format(", ".join(employee.language)))
                print("\tCác project đã hoàn thành: {0}".format(", ".join(employee.project)))
        else:
            employee = self.List_Employee[n-1] 
            print("Số thứ tự: {0}".format(employee.id))
            print("Họ và tên: {0}".format(employee.name))
            print("Năm sinh: {0}".format(employee.birth))
            print("Vị trí công việc hiện tại: {0}".format(employee.position))
            print("Các kĩ năng: {0}".format(", ".join(employee.skill)))
            print("Năm bắt đầu công việc: {0}".format(employee.start))
            print("Các ngôn ngữ lập trình đã dùng: {0}".format(", ".join(employee.language)))
            print("Các project đã hoàn thành: {0}".format(", ".join(employee.project)))
    def Query_Course(self, Emp_a, Emp_b):
        if len(Emp_a.skill) == len(Emp_b.skill):
            if Emp_a.start == Emp_b.start:
                return Emp_a.name.lower() < Emp_b.name.lower()
            else:
                return Emp_a.start < Emp_b.start
        else:
            return len(Emp_a.skill) < len(Emp_b.skill)

    def Query_Project(self, Emp_a, Emp_b):
        return len(Emp_a.project) < len(Emp_b.project)

    def Sort_Employee_For_Course(self):
        CP_Employee = self.List_Employee.copy()
        for i in range(len(CP_Employee)):
            for j in range(len(CP_Employee)-1,i,-1):
                if self.Query_Course(CP_Employee[i],CP_Employee[j]):
                    CP_Employee[i], CP_Employee[j] = CP_Employee[j], CP_Employee[i]
        list_id = []
        for i in range(3):
            emp = CP_Employee[i]
            list_id.append(emp.id)
        return list_id
    def Sort_Employee_For_Project_1(self):
        CP_Employee = [] 
        for emp in self.List_Employee:
            if "python" in emp.language:
                CP_Employee.append(emp)
        for i in range(len(CP_Employee)):
            for j in range(len(CP_Employee)-1,i,-1):
                if self.Query_Project(CP_Employee[i],CP_Employee[j]):
                    CP_Employee[i], CP_Employee[j] = CP_Employee[j], CP_Employee[i]
        list_id = [i.id for i in CP_Employee]
        return list_id
    def Sort_Employee_For_Project_2(self):
        CP_Employee = [] 
        for emp in self.List_Employee:
            if len(emp.project) > 5 and ( 2021 - emp.birth ) >= 30:
                CP_Employee.append(emp.id)
        return CP_Employee

def control(leader):
    print("[1] Nhập thông tin nhân viên")
    print("[2] Xem thông tin nhân viên")
    print("[3] Danh sách 3 nhân viên tham gia khóa học phát triển toàn diện")
    print("[4] Danh sách nhân viên đã sử dụng Python và có nhiều project hoàn thành nhất")
    print("[5] Danh sách nhân viên từ 30 tuổi trở lên và cố số lượng project lớn hơn 5")
    print("[6] Thoát chương trình")
    n = int(input())
    if n != 6:
        if n == 1:
            for i in range(1,n_nhanvien+1):
                leader.Enter_Employee(i)
            print("Nhập thông tin nhân viên hoàn tất")
            print("=====================================================================")

            control(leader)
        elif n == 2:
            print("Nhập id nhân viên muốn xem. Nhập 0 nếu muốn xem thông tin tất cả nhân viên: ",end="")
            id_nv = int(input())
            leader.Get_Employee(id_nv)
            print("=====================================================================")
            control(leader)
        elif n == 3:
            top_emp = leader.Sort_Employee_For_Course()
            for i in top_emp:
                leader.Get_Employee(i)
            print("=====================================================================")
            control(leader)
        elif n == 4:
            top_emp = leader.Sort_Employee_For_Project_1()
            for i in top_emp:
                leader.Get_Employee(i)
            print("=====================================================================")
            control(leader)
        elif n == 5:
            top_emp = leader.Sort_Employee_For_Project_2()
            for i in top_emp:
                leader.Get_Employee(i)
            print("=====================================================================")
            control(leader)
if __name__ == "__main__":
    print("Vui lòng nhập số lượng nhân viên: ",end="")
    n_nhanvien = int(input())
    leader = Leader(n_nhanvien)
    control(leader)



            

