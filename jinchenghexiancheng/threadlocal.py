# def process_student(name):
#     std=Student(name)
#     do_task_1(std)
#     do_task_1(std)

# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)

# def do_subtask_2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)


# global_dict = {}

# def std_thread(name):
#     std = Student(name)
#     # 把std放到全局变量global_dict中：
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()

# def do_task_1():
#     # 不传入std，而是根据当前线程查找：
#     std = global_dict[threading.current_thread()]
#     ...

# def do_task_2():
#     # 任何函数都可以查找出当前线程的std变量：
#     std = global_dict[threading.current_thread()]
#     # ...

# import threading
# local_school=threading.local()

# def process_student():
#     std=local_school.Student
#     print('hello,%s in %s'%(std,threading.current_thread().name))

# def process_thread(name):
#     local_school.Student=name
#     process_student()

# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()



import threading
# local_school=threading.local()
# def process_student():
#     std=local_school.Student
#     print(std,threading.current_thread().name)
# def process_thread(args):
#     local_school.Student=args
#     process_student()

# t1=threading.Thread(target=process_thread,args=('alice',),name='thread-a')
# t2=threading.Thread(target=process_thread,args=('bob',),name='thread-b')
# t1.start()
# t2.start()
# t1.join()
# t2.join()



thread_local=threading.local() #定义了一个全局变量 但是每个线程都是独立的一份，不影响这个

def hello():
    '''
    实现多个同学同时打招呼
    '''
    name=thread_local.name
    print('大家好，我是%s'% name)
def self_introduction(name):
    '''
    自我介绍的时候，调用hello()
    '''
    thread_local.name=name
    hello()
if __name__=='__main__':
    print('自我介绍开始')
    xm=threading.Thread(target=self_introduction,args=('小明',))
    zs=threading.Thread(target=self_introduction,args=('张三',))
    ls=threading.Thread(target=self_introduction,args=('李四',))
    xm.start()
    zs.start()
    ls.start()
    xm.join()
    zs.join()
    ls.join()
    print('自我介绍结束')
