#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue=queue.Queue()
result_queue=queue.Queue()

class QueueManage(BaseManager):
    pass
def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue

# 注册
QueueManage.register('get_task_queue',callable=return_task_queue)
QueueManage.register('get_result_queue',callable=return_result_queue)
# 绑定端口5000，设置验证码
manager=QueueManage(address=('127.0.0.1',5000),authkey='abc')
# 启动
manager.start()
# 通过网络访问
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放任务
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 关闭
manager.shutdown()
print('master exit.')



