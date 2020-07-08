# 垃圾回收机制
# python采用的是引用计数机制为主，标记-清除和分代收集两种机制为辅的策略。
# 引用计数
class Pyobj:
    def __del__(self):
        print('对象被销毁')

print(1)
obj = Pyobj()
obj = 6   # 让变量obj指向其他对象
print(2)

# 1
# 对象被销毁
# 2