#copyright BrilliantLadder Privatized. 

import random
from time import sleep#time.sleep的作用是控制游戏节奏.
import tkinter


def init(end=100,setlife=100,roblife=100):
    global life,robolife,rend,datadic,bloodimg
    rend=end
    life=setlife
    robolife=roblife
    bloodimg='█'
    datadic={'life':life,'robolife':robolife}
    #测试用
    #print('init is conducted.')
    
if __name__=='__main__':
    init()

def acheck(n,wholife,way):#应该实现分别扣除life
    #干脆直接写逻辑函数
    global life,answer,robolife,datadic,k
    if way==1:#判断写入路径
        name='life'
    elif way==2:
        name='robolife'
    if n<answer:#检查
        print('Bigger.\n')
        print('Life-5\n')
        wholife=wholife-5
        datadic[name]=wholife#数据存

    elif n>answer:
        print('Smaller.\n')
        print('Life-5\n')
        wholife=wholife-5
        datadic[name]=wholife
        
    elif n==answer:
        print('Obviously!Congradulations!\n')
        print('Life+10\n')
        answer=random.randint(0,rend)
        print('The answer has been updated...')#生成新答案，进入下一轮
        wholife=wholife+10
        datadic[name]=wholife
    
    if name=='life':
        life=wholife
    elif name=='robolife':
        robolife=wholife


#Main    
print('Battle against Robot!')#title

#生成答案
answer=random.randint(0,rend)
#仅在开局时显示满血.
'''blood=datadic['life']//10
roboblood=datadic['robolife']//10'''
    
while True:
#测试用,进行5轮
#for i in [1,2,3,4,5]:
    
    #将血量值转换为血条.
    #仅在开局时显示满血.
    blood=datadic['life']//10
    roboblood=datadic['robolife']//10
    
    print('Current Life:'+bloodimg*blood)
    print('Robot Life:'+bloodimg*roboblood)
    
    #猜数部分
    try:#防止无输入引发ValueError，为其赋值0
        quest=int(input('What The Correct Number is anyway?'))#Player
    except ValueError:
        quest=0

    print('And Waits for the Robot give the answer.......')
    sleep(3)
    
    robo=random.randint(0,rend)#Robot为了方便，与答案使用同样范围.
    #机器人的逻辑模块
    print('And the Robot says:%s'%answer)
    sleep(1)
    print('Robot:',end=' ')
    sleep(1)
    acheck(robo,robolife,2)
    sleep(1)
    
    #判断大小及血量扣除:玩家的逻辑模块\
    print('Player:',end=' ')
    sleep(1)
    acheck(quest,life,1)
    sleep(1)
    #当判断一方血量归零时：结束游戏
    if datadic['life']==0:
        print('GameEnd.Robots Win!')
        
        break
    elif datadic['robolife']==0:
        print('GameEnd.Player Win!')
        
        break
    #测试用 检测答案是否会改变
    
    #print(answer)
            
            
    #测试用
    #input('Enter to End_______')


"""
Futures:
1、Robot的显示优化(tk pygame)
    
2、游戏节奏的控制优化
"""
    
    

    

