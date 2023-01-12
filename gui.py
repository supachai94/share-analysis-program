import shutil
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox
import os
from tool import doc2docx, create_contents, create_msg_daily
from create_img import img_daily, img_glitter

root = Tk()
root.title('โปรแกรมส่งบทวิเคราะห์')
root.geometry('1225x900')
root.resizable(0,0)
root.config(bg='#ffb969')

part_img99 = r'C:\Users\supachai\Desktop\daily\img\image99_2.jpg'

def select_part(status):

    if status == "daily":
        part_img = r'C:\Users\supachai\Desktop\daily\img\daily_img.png'
        part_price = r'C:\Users\supachai\Desktop\daily\img\daily_price_img.png'

    elif status == "evening":
        part_img = r'C:\Users\supachai\Desktop\daily\img\glitter_img.png'
        part_price = r'C:\Users\supachai\Desktop\daily\img\glitter_price_img.png'

    else:
        print("เกิดข้อผิดพลาดในขั้นตอนการสร้างเนื้อหา")
        print(status)

    return part_img, part_price

def openfn():
    filename = filedialog.askopenfilename(title='เลือกไฟล์บทวิเคราะห์')
    part = os.path.dirname(filename)
    name = os.path.basename(filename)
    splifilename = os.path.splitext(name)
    name = splifilename[0]
    extension = splifilename[1]
    if extension == ".doc":
        doc2docx(filename=filename,part=part, name=name)
        final(part=part, name=name)
        
    elif extension == ".docx":
        final(part=part, name=name)


    else:
        messagebox.showinfo("showinfo", "ไม่พบไฟล์บทวิเคราะห์")

    return

def open_img(part, x, y, plot):    
    img = Image.open(part)
    img = img.resize((435, 435)) 
    img = ImageTk.PhotoImage(img)
    panel = Label(plot, image=img)
    panel.image = img
    panel.pack()
    panel.place(x=x, y=y)

    return

def quit():
   root.destroy()

   return

def get_input():
   value1 = text_box1.get("1.0","end-1c")
   value2 = text_box2.get("1.0","end-1c")
   text_box1.config(state='disabled', bg="#E6E6E6", fg="#363636")
   text_box2.config(state='disabled', bg="#E6E6E6", fg="#363636")
   print(value1, value2)
   print(type(value1+value2))

def edit_text(img_part, status):
    window_2 = Toplevel(root)
    window_2.title('แก้ไขรูปภาพบทวิเคราะห์')
    window_2.geometry('1000x460')
    window_2.resizable(0,0)
    #window_2.config(bg='#ffb166')

    head_size = Label(window_2, text = "ขนาดตัวอักษร").place(x = 520, y = 10)
    head_size = Entry(window_2, width=6).place(x=600, y=11)
    head_x = Label(window_2, text = "ตำแหน่งตัวอักษร X :").place(x = 650, y = 10)
    head_x = Entry(window_2, width=9).place(x=755, y=11)
    head_y = Label(window_2, text = "ตำแหน่งตัวอักษร Y :").place(x = 825, y = 10)
    head_y = Entry(window_2, width=9).place(x=930, y=11)

    Label(window_2, text = "หัวข้อ").place(x = 455, y = 10)
    Label(window_2, text = "เนื้อหา").place(x = 455, y = 90)

    content_size = Label(window_2, text = "ขนาดตัวอักษร").place(x = 520, y = 90)
    content_size = Entry(window_2, width=6).place(x=600, y=91)
    content_x = Label(window_2, text = "ตำแหน่งตัวอักษร X :").place(x = 650, y = 90)
    head_x = Entry(window_2, width=9).place(x=755, y=91)
    content_y = Label(window_2, text = "ตำแหน่งตัวอักษร Y :").place(x = 825, y = 90)
    head_y = Entry(window_2, width=9).place(x=930, y=91)

    text_1 = Text(window_2, height=2, width=59, wrap='word', font= ('Arial', 12))
    text_1.pack(expand=True)
    text_1.place(x=455, y=40)

    text_2 = Text(window_2, height=10, width=59, wrap='word', font= ('Arial', 12))
    text_2.pack(expand=True)
    text_2.place(x=455, y=120)

    open_img(part=img_part, x=10, y=10, plot=window_2)

    def get_text_data():
        header = text_1.get("1.0","end-1c")
        content = text_2.get("1.0","end-1c")
        data2img(header=header, content=content, status=status)
        open_img(part=img_part, x=10, y=10, plot=window_2)
        return

    def exit_btn():
        window_2.destroy()
        window_2.update()

    def update_img():
        open_img(part=img_part, x=10, y=10, plot=root)
        b4 = Button(root, command=lambda:edit_text(img_part=img_part, status=status), text= "แก้ไข").place(x=395, y=15,width=50, relheight=0.03)
        window_2.destroy()
        window_2.update()



    win_2b1 = Button(window_2, command= get_text_data, text= "ปรับค่าใหม่").place(x=455, y=310, width=250, relheight=0.13)

    win_2b2 = Button(window_2, command= update_img, text= "บันทึก").place(x=455, y=380, width=170, relheight=0.15)
    win_2b3 = Button(window_2, command= exit_btn, text= "บันทึกเป็น").place(x=638, y=380, width=170, relheight=0.15)
    win_2b4 = Button(window_2, command= exit_btn, text= "ออก").place(x=820, y=380, width=170, relheight=0.15)


    return

def data2img(status, header, content):

    if status == "daily":
        img_daily(header=header, content=content)

    elif status == "evening":
        img_glitter(header=header, content=content)

    else:
        print("เกิดข้อผิดพลาดในขั้นตอนการสร้างเนื้อหา")
        print(status)
    return

def edit_text_pice(img_part, status):
    window_3 = Toplevel(root)
    window_3.title('แก้ไขรูปภาพบทวิเคราะห์')
    window_3.geometry('1000x460')
    window_3.resizable(0,0)
    #window_2.config(bg='#ffb166')

    head_size = Label(window_3, text = "ขนาดตัวอักษร").place(x = 520, y = 10)
    head_size = Entry(window_3, width=6).place(x=600, y=11)
    head_x = Label(window_3, text = "ตำแหน่งตัวอักษร X :").place(x = 650, y = 10)
    head_x = Entry(window_3, width=9).place(x=755, y=11)
    head_y = Label(window_3, text = "ตำแหน่งตัวอักษร Y :").place(x = 825, y = 10)
    head_y = Entry(window_3, width=9).place(x=930, y=11)

    Label(window_3, text = "หัวข้อ").place(x = 455, y = 10)
    Label(window_3, text = "เนื้อหา").place(x = 455, y = 90)

    content_size = Label(window_3, text = "ขนาดตัวอักษร").place(x = 520, y = 90)
    content_size = Entry(window_3, width=6).place(x=600, y=91)
    content_x = Label(window_3, text = "ตำแหน่งตัวอักษร X :").place(x = 650, y = 90)
    head_x = Entry(window_3, width=9).place(x=755, y=91)
    content_y = Label(window_3, text = "ตำแหน่งตัวอักษร Y :").place(x = 825, y = 90)
    head_y = Entry(window_3, width=9).place(x=930, y=91)

    text_box1 = Text(window_3, height=5, width=59, wrap='word', font= ('Arial', 12))
    text_box1.pack(expand=True)
    text_box1.place(x=455, y=40)

    
    text_box2 = Text(window_3, height=6, width=59, wrap='word', font= ('Arial', 12))
    text_box2.pack(expand=True)
    text_box2.place(x=455, y=120)

    def exit_btn():
        window_3.destroy()
        window_3.update()

    open_img(part=img_part, x=10, y=10, plot=window_3)
    win_2b1 = Button(window_3, command= quit, text= "ปรับค่าใหม่").place(x=455, y=190, width=250, relheight=0.15)
    
    win_2b2 = Button(window_3, command= exit_btn, text= "บันทึก").place(x=455, y=380, width=170, relheight=0.15)
    win_2b3 = Button(window_3, command= exit_btn, text= "บันทึกเป็น").place(x=638, y=380, width=170, relheight=0.15)
    win_2b4 = Button(window_3, command= exit_btn, text= "ออก").place(x=820, y=380, width=170, relheight=0.15)



    window_3.mainloop()
    return

def final(part, name):
    try:
        filename = part+'/'+name+'.docx'
        x = create_contents(filename=filename)
        comment_message = x[0]
        price_message = x[1]
        status = x[2]
        try:
            text_box1.insert('end', comment_message)
            text_box2.insert('end', price_message)
            img = select_part(status=status)
            part_img = img[0]
            part_price = img[1]
            open_img(part=part_img, x=10, y=10, plot=root)
            open_img(part=part_price, x=10, y=455, plot=root)

            b4 = Button(root, command=lambda:edit_text(img_part=part_img, status=status), text= "แก้ไข").place(x=395, y=15,width=50, relheight=0.03)
            b5 = Button(root, command=lambda:edit_text_pice(img_part=part_price, status=status), text= "แก้ไข").place(x=395, y=460,width=50, relheight=0.03)
        except KeyError:
            messagebox.showinfo("showinfo", "เนื้อหามีปัญหา")
        
    except KeyError:
        messagebox.showinfo("showinfo", "การสร้างเนื้อหาไฟล์ไม่สำเร็จ")

    return


b1 = Button(root, command= openfn, text= "เพิ่มไฟล์บทวิเคราะห์").place(x=455, y=758,width=250, relheight=0.15)
b2 = Button(root, command= get_input, text= "ข้อมูลถูกต้องแล้ว").place(x=710, y=758,width=250, relheight=0.15)
b3 = Button(root, command= quit, text= "โพสต์ FB/IG").place(x=965, y=758,width=250, relheight=0.15)

text_box1 = Text(root, height=24, width=84, wrap='word', font= ('Arial', 12))
text_box1.pack(expand=True)
text_box1.place(x=455, y=10)

text_box2 = Text(root, height=16, width=84, wrap='word', font= ('Arial', 12))
text_box2.pack(expand=True)
text_box2.place(x=455, y=455)

open_img(part=part_img99, x=10, y=10, plot=root)
open_img(part=part_img99, x=10, y=455, plot=root)



root.mainloop()