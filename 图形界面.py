# classmates = ['Michael', 'Bob', 'Tracy']
# print(classmates)#打印list
# print(len(classmates))#打印list长度
# print(classmates[0])
# classmates = ('Machael', 'Bob', 'Tracy')
# print(classmates)

# 导入Tkinter包的所有内容
from tkinter import *
import tkinter.messagebox as messagebox

# 从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack() # 把widget添加到父容器
        self.createWidgets()

    # 创建widgets self.quit 关闭窗口
    def createWidgets(self):
        # self.helloLabel = Label(self, text='Hello, world')
        # self.helloLabel.pack()#将helloLabel添加到父容器
        # self.quitButton = Button(self, text='Quit', command=self.quit)
        # self.quitButton.pack()#将quitButton添加到父容器
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app = Application()
# 设置窗口标题
app.master.title('Hello World')
# 消息循环
app.mainloop()