class Info:
	def __init__(self, name, birth, possition, skill, start, language, project,id):
		self.name = name
		self.birth = birth 
		self.possition = possition
		self.skill = skill
		self.start = start
		self.language = language
		self.project = project
		self.id = id

class NhanVien:
	list_nv = []
	def __init__(self, n):
		self.n = n 
		self.list_nv = []

	def enter_nv(self, id):
		print("Nhân viên thứ: ", id+1)

		print("\t Họ và tên: ", end="")
		name = str(input())

		print("\t Năm sinh: ", end="")
		birth = int(input())

		print("\t Vị trí công việc hiện tại: ", end="")
		possition = str(input())

		print("\t Năm bắt đầu làm việc: ", end="")
		start = int(input())

		print("\t Số kĩ năng hiện có: ", end="")
		n_skill = int(input())
		list_skill = []
		for i in range(n_skill):
			print("\t\t Kĩ năng {0}: ".format(i+1), end="")
			sub = str(input())
			list_skill.append(sub)

		print("\t Số lượng ngôn ngữ lập trình đã dùng: ", end="")
		n_lang = int(input())
		list_lang = [] 
		for i in range(n_lang):
			print("\t\t Ngôn ngữ {0}: ".format(i+1), end="")
			sub = str(input())
			list_lang.append(sub)

		print("\t Số lượng project đã hoàn thành: ", end="")
		n_pro = int(input())
		list_pro = [] 
		for i in range(n_pro):
			print("\t\t Project {0}: ".format(i+1), end="")
			sub = str(input())
			list_pro.append(sub)

		info_nv = Info(name, birth, possition, list_skill, start, list_lang, list_pro, id)
		self.list_nv.append(info_nv)
		print("-"*50)

	def show_info(self, id):
		nvi = self.list_nv[id]
		print("-"*50)
		print("\t Nhân viên thứ: ", id+1)
		print("\t Họ và tên: ", nvi.name)
		print("\t Năm sinh: ", nvi.birth)
		print("\t Vị trí công việc hiện tại: ", nvi.possition)
		print("\t Năm bắt đầu công việc: ", nvi.start)
		print("\t Các kỹ năng hiện có: ", ", ".join(nvi.skill))
		print("\t Các ngôn ngữ lập trình đã từng dùng: ", ", ".join(nvi.language))
		print("\t Các project đã hoàn thành: ", ", ".join(nvi.project))
		print("-"*50)

	def query_nv(self, nv1, nv2):
		if len(nv1.skill) == len(nv2.skill):
			if nv1.exp == nv2.exp:
				return nv1.name.lower() < nv2.name.lower()
			return nv1.exp > nv2.exp
		return len(nv1.skill) > len(nv2.skill)
	
	def sort_nv(self):
		list_ans = []

		for i in self.list_nv:
			if len(i.skill) > 3:
				list_ans.append(i)

		if len(list_ans) == 0:
			return list_ans

		for i in range(len(list_ans)):
			for j in range(len(list_ans)-1, i, -1):
				if self.query_nv(list_ans[i], list_ans[j]):
					list_ans[i], list_ans[j] = list_ans[j], list_ans[i]

		return list_ans

	def sort_ns(self):
		list_ans1 = []
		list_ans2 = []

		for i in self.list_nv:
			i.language = [x.lower() for x in i.language]
			if "python" in i.language:
				list_ans1.append(i)
			if 2021-i.birth > 30 and len(i.project) > 5:
				list_ans2.append(i)

		list_ans1 = sorted(list_ans1, key = lambda x: len(x.project), reverse = True)
		
		return [list_ans1, list_ans2]		

	def get_ans_nv(self):
		ans = self.sort_nv()

		if len(ans) == 0:
			print("Không có nhân viên nào thỏa mãn yêu cầu")
			print("-"*50)
			return;

		for i in range(min(3, len(ans))):
			self.show_info(ans[i].id)

	def get_ans_ns(self):
		ans = self.sort_ns()

		return ans

def control(leader):
    print("[1] Nhập thông tin nhân viên")
    print("[2] Xem thông tin nhân viên")
    print("[3] Danh sách 3 nhân viên tham gia khóa học phát triển toàn diện")
    print("[4] Danh sách nhân viên đã sử dụng Python và có nhiều project hoàn thành nhất")
    print("[5] Danh sách nhân viên từ 30 tuổi trở lên và cố số lượng project lớn hơn 5")
    print("[6] Thoát chương trình")
    n = int(input())
    if n > 6 or n < 1:
    	print("Yêu cầu không hợp lệ. Vui lòng thử lại!")
    	control(leader)
    else:
    	if n == 6:
    		return;
    	if n == 1:
            for i in range(leader.n):
                leader.enter_nv(i)
            control(leader)
    	elif n == 2:
	        print("Nhập id nhân viên muốn xem. Nhập 0 nếu muốn xem thông tin tất cả nhân viên: ",end="")
	        id_nv = int(input())
	        if id_nv < 0 or id_nv > leader.n:
	        	print("Id nhân viên không có trong danh sách")
	        	control(leader)
	        if id_nv == 0:
	        	for i in range(leader.n):
	        		leader.show_info(i)
	        else:
	        	leader.show_info(id_nv-1)
	        print("=====================================================================")
	        control(leader)
    	elif n == 3:
	        leader.get_ans_nv()
	        print("=====================================================================")
	        control(leader)
    	elif n == 4:
	        ans = leader.get_ans_ns()

	        if len(ans[0]) == 0:
	        	print("Không có nhân viên nào thỏa mãn yêu cầu")
	        	control(leader)

	        for i in ans[0]:
	        	leader.show_info(i.id)
	        print("=====================================================================")
	        control(leader)
    	elif n == 5:
	        ans = leader.get_ans_ns()

	        if len(ans[1]) == 0:
	        	print("Không có nhân viên nào thỏa mãn yêu cầu")
	        	control(leader)

	        for i in ans[1]:
	        	leader.show_info(i.id)
	        print("=====================================================================")
	        control(leader)

if __name__ == "__main__":
	print("Vui lòng nhập số lượng nhân viên: ", end="")

	n_nhanvien = int(input())
	leader = NhanVien(n_nhanvien)

	control(leader)