import sys
from notebook import Notebook, Note

class Menu:
    '''菜单栏交互环境'''

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            1:self.show_notes,
            2:self.search_notes,
            3:self.add_note,
            4:self.modify_note,
            5:self.save_note,
            6:self.quit,
        }#这里体现了字典的分支作用，由不同的键值，引向不同的函数，达到交互的效果
        print(
            '''
            已进入XX记事本：
            1，列出现有的备注（note）
            2，查找备注
            3，增加备注
            4，修改备注
            5，保存备注
            6，退出
            '''
        )
        self.run()

    def run(self):
        '''主运行函数'''
        while 1:
            try:
                number = int(input("请输入你的选择(1-5)："))
            except ValueError:
                print("选择无效")
                continue
            if number not in range(1, 6):
                print("选择无效")
                continue
            action = self.choices.get(number)#从字典拿到对应的函数
            action()#执行这个函数

    def show_notes(self, notes=None):
        '''展示备注'''
        if not notes:#默认note为None，用来列出所有的note
            for note in self.notebook.notes:
                print("note_id:{},text:{}".format(note.note_id, note.text[:10] + "......" if len(note.text) > 10 else note.text))
        else:
            for note in notes:
                print("note_id:{},text:{}".format(note.note_id, note.text[:10] + "......" if len(note.text) > 10 else note.text))



    def search_notes(self):
        '''查找符合条件的备注'''
        text_find = input("输入你要查找的备注的内容：")
        results= self.notebook.search_note(text_find)
        print("符合条件的列表如下：")
        self.show_notes(results)

    def add_note(self):
        '''增加备注'''
        new_text = input("输入你要增加的备注的text：")
        new_tags = input("输入你要增加的备注的tags：")
        self.notebook.create_note(new_text,new_tags)
        print("增加成功")

    def modify_note(self):
        '''修改备注'''
        note_id = int(input("输入要修改的备注的id："))
        new_text = input("输入要修改的备注的新text：")
        new_tags = input("输入要修改的备注的新tags：")
        self.notebook.modify_note(note_id=note_id, new_text=new_text)
        self.notebook.modify_tags(note_id=note_id,new_tags=new_tags)

    def save_note(self):
        '''保存为txt'''
        note_id = int(input("输入要保存的备注的note_id："))
        note_name = input("输入保存问txt的文件名字：")
        encode = input("输入要保存的编码格式，默认为UTF-8：")
        if not encode :
            encode = 'utf-8'
        self.notebook.save_as_txt(note_id,note_name,encode)
        print("保存成功")

    def quit(self):
        '''退出应用'''
        print("感谢你的使用，再见")
        sys.exit(0)

if __name__ == '__main__':
    menu = Menu()