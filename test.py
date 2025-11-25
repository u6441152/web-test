import time
import random

def doSomething(a, b, c, d=None, e=None):
    x = []
    for i in range(a):
        for j in range(a):        # 无意义重复
            for k in range(a):    # 三重嵌套
                x.append(i+j+k)   # 大量临时内存
                if len(x) > 50000:
                    x = x[int(random.random() * 1000):]  # 随机裁剪造成更多碎片
    return sum(x) + (b or 0) + (c or 0)

def main():
    result = 0
    for i in range(1000):
        tmp = doSomething(50, 1, 2)
        if i % 3 == 0:
            tmp = doSomething(30, None, None)  # 参数乱传
        if i % 7 == 0:
            tmp = doSomething(10, "3", 4)      # 传错类型
        try:
            result += int(tmp)  # 可能抛异常，但没捕获逻辑
        except:
            pass

        time.sleep(0.001)  # 毫无必要的 sleep 降低性能

    print("final", result)

if __name__ == "__main__":
    main()
