from tkinter import *
from tkinter import messagebox
# Khai báo danh sách toàn cục để lưu trữ tất cả các nhiệm vụ
tasks_list = []

# Biến toàn cục để đếm số nhiệm vụ
counter = 1

# Hàm kiểm tra lỗi nhập liệu khi trường nhiệm vụ trống
def inputError():
	if enterTaskField.get() == "":
		
		# Hiển thị thông báo lỗi
		messagebox.showerror("Lỗi nhập liệu")
		return 0
	return 1

# Hàm để xóa nội dung của trường số nhiệm vụ
def clear_taskNumberField():
	
	# Xóa nội dung của trường số nhiệm vụ
	taskNumberField.delete(0.0, END)

# Hàm để xóa nội dung của trường nhập nhiệm vụ 
def clear_taskField():
	# Xóa nội dung của trường nhập nhiệm vụ
	enterTaskField.delete(0, END)
	
# Hàm để chèn nhiệm vụ từ trường nhập nhiệm vụ vào khu vực văn bản
def insertTask():
	global counter
	# Kiểm tra lỗi
	value = inputError()
	# Nếu có lỗi, thì trả về
	if value == 0:
		return

	# Lấy nhiệm vụ và nối thêm ký tự xuống dòng
	content = enterTaskField.get() + "\n"

	# Lưu trữ nhiệm vụ vào danh sách
	tasks_list.append(content)

	# Chèn nội dung của trường nhập nhiệm vụ vào khu vực văn bản
	# thêm từng nhiệm vụ một
	taskTextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

	# Tăng biến đếm
	counter += 1

	# Gọi hàm để xóa nội dung trường nhiệm vụ
	clear_taskField()

# Hàm để xóa nhiệm vụ cụ thể
def delete():
	global counter
	
	# Xử lý lỗi nhiệm vụ trống
	if len(tasks_list) == 0:
		messagebox.showerror("Không có nhiệm vụ")
		return

	# Lấy số nhiệm vụ cần xóa
	number = taskNumberField.get(1.0, END)

	# Kiểm tra lỗi nhập liệu khi
	# trường số nhiệm vụ trống
	if number == "\n":
		messagebox.showerror("Lỗi nhập liệu")
		return
	
	else:
		task_no = int(number)
    # Hàm để xóa tất cả các nhiệm vụ


	# Gọi hàm để xóa nội dung trường số nhiệm vụ
	clear_taskNumberField()
	
	# Xóa nhiệm vụ cụ thể từ danh sách
	tasks_list.pop(task_no - 1)

	# Giảm biến đếm
	counter -= 1

	# Xóa toàn bộ nội dung khu vực văn bản
	taskTextArea.delete(1.0, END)

	# Ghi lại nhiệm vụ sau khi xóa từng nhiệm vụ một
	for i in range(len(tasks_list)):
		TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

#(BỔ SUNG) Hàm để xóa tất cả các nhiệm vụ
def deleteAllTasks():
    global counter, tasks_list
    # Xóa toàn bộ nội dung trong danh sách và trên giao diện
    tasks_list = []
    counter = 1
    taskTextArea.delete(1.0, END)
#(BỔ SUNG) Hàm để thực hiện tìm kiếm công việc
def searchTasks():
    search_keyword = searchField.get()  # Lấy từ khóa tìm kiếm từ hộp nhập văn bản
    if search_keyword:
        # Xóa nội dung hiện tại trên khu vực văn bản
        taskTextArea.delete(1.0, END)
        
        # Tạo danh sách kết quả tìm kiếm
        search_results = [task for task in tasks_list if search_keyword.lower() in task.lower()]
        
        if search_results:
            # Hiển thị kết quả tìm kiếm trên khu vực văn bản
            for i, result in enumerate(search_results, start=1):
                taskTextArea.insert(END, f"[ {i} ] {result}")
        else:
            taskTextArea.insert(END, "Không tìm thấy kết quả cho từ khóa này.")
    else:
        # Nếu trường tìm kiếm trống, cập nhật lại khu vực văn bản để hiển thị danh sách gốc
        refreshTasks()
#(BỔ SUNG) Hàm để chỉnh sửa công việc đã nhập
def editTask():
    global tasks_list
    task_no = int(taskNumberField.get("1.0", "end-1c"))  # Lấy số nhiệm vụ cần chỉnh sửa
    if 0 < task_no <= len(tasks_list):
        new_content = enterTaskField.get()
        tasks_list[task_no - 1] = new_content + "\n"
        refreshTasks()  # Cập nhật hiển thị công việc sau khi chỉnh sửa
# Hàm để xóa nhiệm vụ cụ thể
def delete():
    global counter

    # Xử lý lỗi nhiệm vụ trống
    if len(tasks_list) == 0:
        messagebox.showerror("Không có nhiệm vụ")
        return

    # Lấy số nhiệm vụ cần xóa
    number = taskNumberField.get(1.0, END)

    # Kiểm tra lỗi nhập liệu khi trường số nhiệm vụ trống
    if number == "\n":
        messagebox.showerror("Lỗi nhập liệu")
        return
    
    else:
        task_no = int(number)
        if 0 < task_no <= len(tasks_list):
            # Xóa nhiệm vụ cụ thể từ danh sách
            tasks_list.pop(task_no - 1)
            
            # Xóa toàn bộ nội dung trong khu vực văn bản
            taskTextArea.delete(1.0, END)

            # Ghi lại nhiệm vụ sau khi xóa từng nhiệm vụ một
            for i in range(len(tasks_list)):
                taskTextArea.insert(END, "[ " + str(i + 1) + " ] " + tasks_list[i])
            
            # Giảm biến đếm
            counter -= 1

        else:
            messagebox.showerror("Lỗi nhập liệu", "Số nhiệm vụ không hợp lệ")
    # Hàm để cập nhật hiển thị công việc
def refreshTasks():
    taskTextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        taskTextArea.insert(END, f"[ {i + 1} ] {tasks_list[i]}") 
# Hàm để lưu danh sách công việc vào tệp văn bản
def saveTasksToFile():
    filename = "tasks.txt"  # Tên tệp để lưu dữ liệu
    
    # Mở tệp để ghi dữ liệu
    with open(filename, 'w') as file:
        for task in tasks_list:
            file.write(task)
    
    messagebox.showinfo("Lưu trữ thành công", "Danh sách công việc đã được lưu vào tệp tasks.txt")

if __name__ == "__main__":
    gui = Tk()
    gui.title("Ứng dụng Quản lý Công việc")
    gui.geometry("400x450")
    gui.configure(background="#F0F0F0")  # Sử dụng màu sáng nhẹ

    enterTaskLabel = Label(gui, text="Nhập Công việc của bạn", fg="black", bg="#B3E5FC")  # Màu sáng cho nhãn
    enterTaskLabel.grid(row=0, column=0, columnspan=2, pady=(10, 5))

    enterTaskField = Entry(gui)
    enterTaskField.grid(row=1, column=0, columnspan=2, padx=10)

    submitButton = Button(gui, text="Gửi", fg="white", bg="#0277BD", width=10, command=insertTask)  # Đổi màu và kích thước nút
    submitButton.grid(row=2, column=0, columnspan=2, pady=(5, 10))

    taskAreaLabel = Label(gui, text="Danh sách công việc", fg="white", bg="#0288D1")
    taskAreaLabel.grid(row=3, column=0, columnspan=2)

    taskTextArea = Text(gui, height=5, width=25, font="lucida 13")
    taskTextArea.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 5))

    deleteTaskLabel = Label(gui, text="Nhập số công việc cần xóa hoặc chỉnh sửa", fg="white", bg="#EC407A")
    deleteTaskLabel.grid(row=5, column=0, columnspan=2, pady=(5, 0))

    taskNumberField = Text(gui, height=1, width=2, font="lucida 13")
    taskNumberField.grid(row=6, column=0, columnspan=2)

    deleteButton = Button(gui, text="Xóa", fg="white", bg="#D32F2F", width=10, command=delete)  # Đổi màu và kích thước nút
    deleteButton.grid(row=7, column=0, pady=(5, 10), sticky="E")

    exitButton = Button(gui, text="Thoát", fg="white", bg="#D32F2F", width=10, command=exit)  # Đổi màu và kích thước nút
    exitButton.grid(row=7, column=1, pady=(5, 10), sticky="W")

    deleteAllButton = Button(gui, text="Xóa Tất Cả", fg="black", bg="#81C784", width=20, command=deleteAllTasks)  # Đổi màu và kích thước nút
    deleteAllButton.grid(row=8, column=0, columnspan=2, pady=(0, 5))

    searchLabel = Label(gui, text="Tìm Kiếm Công Việc", fg="white", bg="#5C6BC0")
    searchLabel.grid(row=9, column=0, columnspan=2)

    searchField = Entry(gui)
    searchField.grid(row=10, column=0, columnspan=2)

    searchButton = Button(gui, text="Tìm Kiếm", fg="white", bg="#7E57C2", width=10, command=searchTasks)  # Đổi màu và kích thước nút
    searchButton.grid(row=11, column=0, columnspan=2, pady=(0, 10))
    # Thêm nút "Chỉnh sửa"
    editButton = Button(gui, text="Chỉnh sửa", fg="White", bg="#FFA500", command=editTask)
    editButton.grid(row=12, column=0)
    #THÊM NÚT LƯU
    saveButton = Button(gui, text="Lưu", fg="white", bg="#4CAF50", width=10, command=saveTasksToFile)
    saveButton.grid(row=12, column=1)  
    gui.mainloop()