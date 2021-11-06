from datetime import datetime


class Basic_Info:
	def __init__(self, id, name, birth, position, skill, start_year):
		self.name = name 
		self.birth = birth
		self.position = position
		self.skill = skill
		self.start_year = start_year 
		self.id = id 
		self.exp = datetime.now().date().year - start_year


class Advance_Info(Basic_Info):
	def __init__(self, id, name, birth, position, skill, start_year, language, project):
		Basic_Info.__init__(self, id, name, birth, position, skill, start_year)
		self.language = language
		self.project = project


class Learn_Employee:
	list_employee = []


	def add_employee(self, info_employee):
		self.list_employee = info_employee


	def get_employee(self, id):
		employee = self.list_employee[id]
		print("-"*50)
		print(f"""
\t Nhân viên thứ: {id + 1}
\t Họ và tên: {employee.name}
\t Năm sinh: {employee.birth}
\t Vị trí công việc: {employee.position}
\t Các kỹ năng hiện có: {", ".join(employee.skill)}
\t Năm bắt đầu công việc: {employee.start_year}
\t Số năm kinh nghiệm: {employee.exp}
		""")
		print("-"*50)
	
	
	def query(self, employee1, employee2):
		if len(employee1.skill) == len(employee2.skill):
			if employee1.exp == employee2.exp:
				return employee1.name.lower() > employee2.name.lower()
			return employee1.exp < employee2.exp 
		return len(employee1.skill) < len(employee2.skill)
	

	def get_employee_for_learn(self):

		employees = self.list_employee.copy()
		
		# Bubble sort
		for i in range(len(employees)):
			for j in range(len(employees)-1, i, -1):
				if self.query(employees[i], employees[j]):
					employees[i], employees[j] = employees[j], employees[i]

		for i in range(min(3, len(employees))):
			self.get_employee(employees[i].id)


class Project_Employee:
	list_employee = []

	
	def add_employee(self, info_employee):
		self.list_employee = info_employee

	
	def get_employee(self, id):
		employee = self.list_employee[id]
		
		print("-"*50)
		print(f"""
\t Nhân sự thứ: {id + 1}
\t Họ và tên: {employee.name}
\t Năm sinh: {employee.birth}
\t Vị trí công việc: {employee.position}
\t Các kỹ năng hiện có: {", ".join(employee.skill)}
\t Năm bắt đầu công việc: {employee.start_year}
\t Số năm kinh nghiệm: {employee.exp}
\t Các ngôn ngữ lập trình đã từng dùng: {", ".join(employee.language)}
\t Các project đã hoàn thành: {", ".join(employee.project)}
		""")
		print("-"*50)
	
	
	def get_employee_python_dev(self):
		employees = []

		for employee in self.list_employee:
			if "Python" in employee.language:
				employees.append(employee)
		
		employees = sorted(employees, key = lambda employee: len(employee.project), reverse = True)

		for employee in employees:
			self.get_employee(employee.id)

	
	def get_employee_exp(self):
		employees = []

		for employee in self.list_employee:
			if employee.exp > 30 and len(employee.project) > 5:
				employees.append(employee)
		
		for employee in employees:
			self.get_employee(employee.id)
	

def control(learn_emp, project_emp):
	
	print(f"""
[*] Thông tin về nhân viên
\t [1] Xem thông tin cơ bản của nhân viên
\t [2] Danh sách nhiều nhất 3 nhân viên tham giá khóa học toàn diện
[*] Thông tin về nhân sự
\t [3] Xem thông tin cơ bản của nhân sự
\t [4] Danh sách nhân sự từng dùng Python và có nhiều project hoàn thành nhất
\t [5] Danh sách nhân sự trên 30 tuổi và có số project hoàn thành lớn hơn 5
[*] Chương trình
\t [6] Thoát khỏi chương trình
	""")
	print("Nhập tùy chọn: ", end="")
	n = int(input())

	if n < 1 or n > 6:
		control(learn_emp, project_emp)
	if n == 1:
		print("Nhập id nhân viên muốn xem (nhập 0 để xem tất cả): ", end="")
		id_employee = int(input())
		
		if id_employee < 0 or id_employee > len(learn_emp.list_employee):
			print("Id nhân viên không có trong danh sách")
			control(learn_emp, project_emp)
		elif id_employee == 0:

			for i in range(len(learn_emp.list_employee)):
				learn_emp.get_employee(i)
		else:
			learn_emp.get_employee(id_employee-1)

		control(learn_emp, project_emp)
	elif n == 2:
		learn_emp.get_employee_for_learn()
		control(learn_emp, project_emp)
	elif n == 3:
		print("Nhập id nhân sự muốn xem (nhập 0 để xem tất cả): ", end="")
		id_employee = int(input())
		
		if id_employee < 0 or id_employee > len(project_emp.list_employee):
			print("Id nhân sự không có trong danh sách")
			control(learn_emp, project_emp)
		elif id_employee == 0:

			for i in range(len(project_emp.list_employee)):
				project_emp.get_employee(i)
		else:
			project_emp.get_employee(id_employee-1)

		control(learn_emp, project_emp)
	elif n == 4:
		project_emp.get_employee_python_dev()
		control(learn_emp, project_emp)
	elif n == 5:
		project_emp.get_employee_exp()
		control(learn_emp, project_emp)
	

if __name__ == "__main__":
	learn_emp = Learn_Employee() # Employee for learn
	project_emp = Project_Employee() # Employee for project

	# Nhập thông tin nhân viên
	emp1 = Basic_Info(0, "Nguyen Van A", 2000, "Dev", ["math", "dev"], 2010)
	emp2 = Basic_Info(1, "Nguyen Van B", 1900, "Dev", ["math", "dev"], 1950)
	emp3 = Basic_Info(2, "Nguyen Van C", 1950, "Dev", ["math", "dev", "programing"], 1970)
	emp4 = Basic_Info(3, "Nguyen Van D", 2009, "Dev", ["math", "dev"], 2019)
	emp5 = Basic_Info(4, "Nguyen Van E", 2015, "Dev", ["math", "dev"], 2020)
	emp6 = Basic_Info(5, "Nguyen Van F", 1969, "Dev", ["math", "dev", "hack", "security"], 1980)

	learn_emp.add_employee([emp1, emp2, emp3, emp4, emp5, emp6])

	# Nhập thông tin nhân sự	
	emp1 = Advance_Info(0, "Nguyen Van A", 2000, "Dev", ["math", "dev"], 2010, ["Python", "C++", "Java"], ["a", "b", "c"])
	emp2 = Advance_Info(1, "Nguyen Van B", 1900, "Dev", ["math", "dev"], 1950, ["Python", "Java"], ["b", "c"])
	emp3 = Advance_Info(2, "Nguyen Van C", 1950, "Dev", ["math", "dev", "programing"], 1970, ["Python", "C++", "Java"], ["a", "b", "c", "d", "e", "f"])
	emp4 = Advance_Info(3, "Nguyen Van D", 2009, "Dev", ["math", "dev"], 2019, ["Java"], ["a"])
	emp5 = Advance_Info(4, "Nguyen Van E", 2015, "Dev", ["math", "dev"], 2020, ["C++", "Java"], ["a", "b"])
	emp6 = Advance_Info(5, "Nguyen Van F", 1969, "Dev", ["math", "dev", "hack", "security"], 1980, ["Python", "C++", "Java"], ["a", "b", "c", "e", "f", "g", "h"])

	project_emp.add_employee([emp1, emp2, emp3, emp4, emp5, emp6])

	control(learn_emp, project_emp)
