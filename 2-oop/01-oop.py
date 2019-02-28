'''
定义一个学生类，用来形容学生
'''
#定义一个空的类
class Student():
    pass
#定义一个对象
mingyue = Student()

#再定义一个类，用来描述在听python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #需要注意
    #1.def doHomework的缩进层级
    #2.系统默认有一个self参数
    def doHomework(self):
        print("我在写作业")
#实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传递进入参数
yueyue.doHomework()


