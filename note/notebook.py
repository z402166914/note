class Note:
    id_list = list(reversed([x for x in range(100)]))
    '''一个note的单体'''
    def __init__(self, text, tags):
        '''
        初始化属性
        :param text:Note的正文部分
        :param tags: Note的单体部分
        '''
        self.text = text
        self.tags = tags
        try:
            self.note_id = self.id_list.pop()
        except IndexError:
            print('note创建的最大值为100，你已经创建了100个')

    def match(self, text_find):
        '''
        用来查询note中的内容
        :param text_find: 想要查询的文本部分
        :return: 返回一个bool值
        '''
        return True if text_find in self.text else False

class Notebook:
    '''用来存放note'''

    def __init__(self):
        '''
        创建一个容器
        '''
        self.notes = []

    def create_note(self, text, tags):
        '''
        一个实现了上面的Note类的接口，用来创建一个新的Note对象
        :param text: 新的Note的文本
        :param tags: 新的Note的标签
        :return: 返回这个新的note，加入notes中
        '''
        self.notes.append(Note(text, tags))

    def search_note(self, text_find):
        '''
        用来查找符合条件的note
        :param text_find:查找的内容
        :return: 以列表的形式返回符合查找条件的多个note
        '''
        # return list(filter(lambda x:x.match(text_find), self.notes))用高阶函数和匿名函数完成，看起来有点复杂
        return [note for note in self.notes if note.match(text_find)]#用列表表达式写更直观，

    def _find_note(self, note_id):
        '''用来遍历notes，找出给定note_id值的那个note'''
        for note in self.notes:
            if note.note_id == note_id:
                return note

        return None

    def modify_note(self, new_text, note_id):
        '''修改对应id的note的text'''
        a = self._find_note(note_id)
        self._find_note(note_id).text = new_text#调用实例自身的方法
        print('text修改成功')

    def modify_tags(self, new_tags, note_id):
        '''修改对应id的note的tags'''
        self._find_note(note_id).tags = new_tags  # 调用实例自身的方法
        print('tags修改成功')

    def save_as_txt(self, note_id, note_name, encode= 'utf-8'):
        '''用来保存对应的id的note为txt文件'''
        with open('{}.txt'.format(note_name),'w') as f:
            text = self._find_note(note_id).text
            text.encode(encode)
            f.write(text)
        print('保存成功')


