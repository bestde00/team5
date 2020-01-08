a=0
loadname=""
loadin =False
def menu():
    import pygame
    pygame.init()
    main_surface = pygame.display.set_mode((1530,800))
    main_surface.fill((0,0,0))
    main_surface.fill((150,150,0),(600,500,330,65))
    main_surface.fill((150,150,0),(600,650,330,65))
    pic = pygame.image.load("槌子魔法師.png")
    font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 50)
    option1 = font.render("新遊戲(Y)",True,(255,255,255))
    option2 = font.render("載入進度(N)",True,(255,255,255))
    main_surface.blit(option1,(645,507))
    main_surface.blit(option2,(615,657))
    main_surface.blit(pic, (200, 0))
    def load():
        global loadname
        main_surface.fill((0,0,0))
        font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 20)
        new_font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 60)
        some_color = (255,255,200)
        somerect = (500,400,450,50)
        main_surface.fill(some_color,somerect)
        the_text = font.render('請輸入檔案名字(不須加".txt")，輸入完後按Enter:',True,(255,255,255))
        new_text = new_font.render(loadname,True,(0,0,0))
        main_surface.blit(the_text,(500,375))
        main_surface.blit(new_text,(520,405))
    global loadin
    global loadname
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        else:
            if ev.type==pygame.KEYDOWN:
                key = ev.dict["key"]
                if key == ord("y"):
                    break
                if key == ord("n"):
                    loadin=True
                    break
            if ev.type == pygame.MOUSEBUTTONDOWN:
                posn_of_click = ev.dict["pos"]
                if 600 <= posn_of_click[0] <= 930 and 500 <= posn_of_click[1] <= 565:
                    #Equivalent to "y"
                    break
                elif 600 <= posn_of_click[0] <= 930 and 650 <= posn_of_click[1] <= 715:
                    #Equivalent to "n"
                    loadin=True
                    break
        pygame.display.flip()
    while loadin==True:
        load()
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            loadin=False
            break
        if ev.type==pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 13:
                loadname+=".txt"
                break
            elif key == 8:
                loadname=loadname[:(-1)]
            if key==ord("q"):
                loadname+="q"
            elif key==ord("w"):
                loadname+= 'w'
            elif key==ord("e"):
                loadname+= 'e'
            elif key==ord("r"):
                loadname+= 'r'
            elif key==ord("t"):
                loadname+= 't'
            elif key==ord("y"):
                loadname+= 'y'
            elif key==ord("u"):
                loadname+= 'u'
            elif key==ord("i"):
                loadname+= 'i'
            elif key==ord("o"):
                loadname+= 'o'
            elif key==ord("p"):
                loadname+= 'p'
            elif key==ord("a"):
                loadname+= 'a'
            elif key==ord("s"):
                loadname+= 's'
            elif key==ord("d"):
                loadname+= 'd'
            elif key==ord("f"):
                loadname+= 'f'
            elif key==ord("g"):
                loadname+= 'g'
            elif key==ord("h"):
                loadname+= 'h'
            elif key==ord("j"):
                loadname+= 'j'
            elif key==ord("k"):
                loadname+= 'k'
            elif key==ord("l"):
                loadname+= 'l'
            elif key==ord("z"):
                loadname+= 'z'
            elif key==ord("x"):
                loadname+= 'x'
            elif key==ord("c"):
                loadname+= 'c'
            elif key==ord("v"):
                loadname+= 'v'
            elif key==ord("b"):
                loadname+= 'b'
            elif key==ord("n"):
                loadname+= 'n'
            elif key==ord("m"):
                loadname+= 'm'
            elif key==49 or key==257:
                loadname+="1"
            elif key==50 or key==258:
                loadname+="2"
            elif key==51 or key==259:
                loadname+="3"
            elif key==52 or key==260:
                loadname+="4"
            elif key==53 or key==261:
                loadname+="5"
            elif key==54 or key==262:
                loadname+="6"
            elif key==55 or key==263:
                loadname+="7"
            elif key==56 or key==264:
                loadname+="8"
            elif key==57 or key==265:
                loadname+="9"
            elif key==48 or key==256:
                loadname+="0"
        pygame.display.flip()
def save(save_name):#要加".txt"
    global hero1
    global weapon1
    global money
    global timing
    global mons1
    global mons2
    global mons3
    global mons4
    global mons5
    global mons6
    global mons7
    global mons8
    global mons9
    global package1
    listing=[hero1.N,weapon1.N,money,int(timing),mons1.N,mons2.N,mons3.N,mons4.N,mons5.N,mons6.N,mons7.N,mons8.N,mons9.N,package1.p1,package1.p2,package1.p3,package1.p4,package1.p5,hero1.exp_all,int(hero1.hp),weapon1.alv,weapon1.slv,weapon1.dur,int(mons1.hp),int(mons2.hp),int(mons3.hp),int(mons4.hp),int(mons5.hp),int(mons6.hp),int(mons7.hp),int(mons8.hp),int(mons9.hp),int(mons1.atk),int(mons2.atk),int(mons3.atk),int(mons4.atk),int(mons5.atk),int(mons6.atk),int(mons7.atk),int(mons8.atk),int(mons9.atk)]
    with open (save_name,"w") as file:
        file.write(str(listing))
class weapon:
    def __init__(self,l=1):
        self.alv=0
        self.slv=0
        if l==2:
            self.N=2
            self.dur_max=600
            self.dur=600
            self.shd=198
            self.atk=360
        elif l==5:
            self.N=5
            self.dur_max=606
            self.dur=606
            self.shd=200
            self.atk=365
        else:
            self.N=1
            self.dur_max=606
            self.shd=200
            self.dur=606
            self.atk=360
        self.cd=0
    def alv_up(self):
        self.alv+=1
        if self.N==5:
            self.atk+=31
        else:
            self.atk+=30
    def slv_up(self):
        self.slv+=1
        self.shd+=13
    def dur_heal(self):
        if self.N==2 or self.N==5:
            self.dur+=255
        else:
            self.dur+=250
        if self.dur>self.dur_max:
            self.dur=self.dur_max
    def use(self):
        self.dur-=1
    def __str__(self):
        return f"""weapon number：{self.N}
weapon attack：{self.atk}（level：{self.alv}）
weapon shield：{self.shd}（level：{self.slv}）
weapon endurance：{self.dur}／{self.dur_max}（level：{self.elv}）"""
    def skill(self):
        global timing
        if timing-self.cd>=0:
            if self.N==2:
                global money
                import random
                money+=random.randint(1500,2000)
                self.cd=timing+25
            elif self.N==1:
                global hero1
                hero1.heal(int((hero1.hp_max-hero1.hp)*0.16))
                self.cd=timing+25
            elif self.N==5:
                pass
    def intro(self):
        if self.N==1:    
            return "特性：堅固耐用\n技能：回復16%已損生命(CD:25s)"
        elif self.N==2:
            return "特性：消耗金錢DOWN\n技能：隨機獲得金錢(1500-2000)(CD:25s)"
        elif self.N==5:
            return "特性：小範圍攻擊(鄰近12%)\n技能：基礎能力UP(Passive)"
class hero:
    def __init__(self,l=1):
        self.N=l
        self.exp_all=0
        self.lv=0
        self.exp=0
        self.hp=2100
        self.hp_max=2100
    def intro(self):
        return "特性：血量UP"
    def __str__(self):
        return f"""hero number：{self.N}
hero level：{self.lv}
hero hp：{self.hp}／{self.hp_max}
hero exp：{self.exp}／500"""
    def getexp(self,N):
        self.exp_all+=N
        self.exp=self.exp_all%500
        if self.exp_all//500>self.lv:
            self.hp+=160*(self.exp_all//500-self.lv)
            self.hp_max+=160*(self.exp_all//500-self.lv)
            self.lv=self.exp_all//500
    def heal(self,a):
        if self.hp+a>self.hp_max:
            self.hp=self.hp_max
        else:
            self.hp+=a
class monster:
    def __init__(self,l):
        global turn
        if l==1:#(small)
            self.atk=360+58*turn
            self.hp=1666+355*turn
        elif l==2:#(medium)
            self.atk=390+61*turn
            self.hp=2321+395*turn
        elif l==3:#(large)
            self.atk=415+64*turn
            self.hp=2666+429*turn
        elif l==4:#(bomb)
            global hero1
            self.atk=min(int(hero1.hp*0.18*1.01**turn),hero1.hp)
            self.hp=2150+415*turn
        elif l==5:#(treasure)
            self.atk=0
            self.hp=1
        else:
            self.atk=0
            self.hp=0
        self.N=l
        import time
        self.time=time.time()
    def __str__(self):
        if self.N==1:
            name="small 郁翔"
        elif self.N==2:
            name="medium 郁翔"
        elif self.N==3:
            name="large 郁翔"
        elif self.N==4:
            name="bomb 郁翔"
        elif self.N==5:
            name="treasure"
        else:
            name="None"
        return f"""monster name：{name}
monster attack：{self.atk}
monster hp：{self.hp}
monster time：{self.time}"""

def startdata(numberstr):
    if len(numberstr)==8 and numberstr.isdigit():
        A1=numberstr[0:5]
        A2=numberstr[5:]
        A1=int(A1)
        A2=int(A2)
    else:
        import random
        A1=random.randint(0,9999)
        A2=random.randint(0,9999)
    ans=[]
    if A1%3==0:
        ans.append(2)
    elif A1%3==2:
        ans.append(5)
    else:
        ans.append(1)
    if A2==0:
        ans.append(10)
    elif A2==1110:
        ans.append(1)
    elif A2==3141:
        ans.append(4)
    elif A2==1017:
        ans.append(8)
    elif A2%6==0:
        ans.append(2)
    elif A2%6==1:
        ans.append(3)
    elif A2%6==2:
        ans.append(5)
    elif 21%6==3:
        ans.append(6)
    elif A2%6==4:
        ans.append(7)
    elif A2%6==5:
        ans.append(9)
    return ans

def monsappear():
    global timing
    turn=timing//20
    Small=3000000+30001*turn
    Medium=740000+7401*turn
    Large=27000+2701*turn
    Bomb=280000+2801*turn
    Treasure=41000+411*turn
    import random
    k=random.randint(1,Small+Medium+Large+Bomb+Treasure)
    if k<=Small:
        return 1
    elif k<=Small+Medium:
        return 2
    elif k<=Small+Medium+Large:
        return 3
    elif k<=Small+Medium+Large+Bomb:
        return 4
    else:
        return 5

class package:
    def __init__(s):
        s.p1=0
        s.p2=0
        s.p3=0
        s.p4=0
        s.p5=0
        s.p4_cd=0
    def p4_skill(s):
        global timing
        global weapon1
        if 0<=timing-s.p4_cd<=0.008 and timing>0.008:
            weapon1.shd-=100000
    def use_p1(s):
        if s.p1>=1:
            s.p1-=1
            global hero1
            hero1.heal(hero1.hp_max*0.15)
    def use_p2(s):
        if s.p2>=1:
            s.p2-=1
            global hero1
            hero1.heal(hero1.hp_max*0.19)
    def use_p3(s):
        if s.p3>=1:
            s.p3-=1
            global hero1
            hero1.heal(hero1.hp_max*0.23)
    def use_p4(s):
        if s.p4>=1:
            s.p4-=1
            global timing
            s.p4_cd=timing+10
    def use_p5(s):
        if s.p5>=1:
            s.p5-=1
    def get_p1(s):
        s.p1+=1
        if s.p1>=6:
            s.p1=6
    def get_p2(s):
        s.p2+=1
        if s.p2>=6:
            s.p2=6
    def get_p3(s):
        s.p3+=1
        if s.p3>=6:
            s.p3=6
    def get_p4(s):
        s.p4+=1
        if s.p4>=6:
            s.p4=6
    def get_p5(s):
        s.p5+=1
        if s.p5>=6:
            s.p5=6

def get_treasure():
    global package1
    global money
    global hero1
    def treaappear():
        global turn
        N1=1000000+20001*turn
        N2=500000+10001*turn
        N3=250000+5001*turn
        M=600000+12001*turn
        S=100000+2001*turn
        R=10000+201*turn
        EXP=600000+12001*turn
        import random
        k=random.randint(1,N1+N2+N3+M+S+R+EXP)
        if k<=N1:
            return 1
        elif k<=N1+N2:
            return 2
        elif k<=N1+N2+N3:
            return 3
        elif k<=N1+N2+N3+M:
            return 4
        elif k<=N1+N2+N3+M+S:
            return 5
        elif k<=N1+N2+N3+M+S+R:
            return 6
        else:
            return 7
    val = treaappear()
    if val==1:
        package1.get_p1()
    elif val==2:
        package1.get_p2()
    elif val==3:
        package1.get_p3()
    elif val==4:
        import random
        money+=random.randint(2345,2999)
    elif val==5:
        package1.get_p4()
    elif val==6:
        package1.get_p5()
    elif val==7:
        import random
        hero1.getexp(random.randint(75,95))
def 新遊戲螢幕(新遊戲_end):
    import pygame
    pygame.init()
    main_surface = pygame.display.set_mode((1530,800))
    main_surface.fill((0,0,0))
    welcome_count = 0
    parameter = ''
    password = ''
    def 輸入號碼(parameter,password):
        main_surface.fill((0,0,0))
        font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 20)
        new_font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 60)
        some_color = (255,255,200)
        somerect = (500,400,450,50)
        main_surface.fill(some_color,somerect)
        the_text = font.render('請輸入一組八位數，輸入完後按Enter:',True,(255,255,255))
        new_text = new_font.render(password,True,(0,0,0))
        main_surface.blit(the_text,(500,375))
        main_surface.blit(new_text,(520,405))
    def welcome(welcome_count):
        my_font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 30)
        text_color = (255,255,255)
        sentence0 = '西元2019年，這個世界遭受到了外星人的入侵'
        sentence1 = '生物學家分析了這類生物，並將它命名為"YU-SIANG"'
        sentence2 = '然而，為了防止世界被破壞，為了守護世界的和平'
        sentence3 = '一位勇者誕生於世上，這個人就是您，偉大的冒險者' 
        sentence4 = '您將踏上一個不平凡的旅途，世界的和平就靠您守護了'
        sentence5 = '來吧!決定你的人生吧!'
        if welcome_count == 0:
            text0 = my_font.render(sentence0,True,text_color)
            main_surface.blit(text0,(450,400))
        elif welcome_count == 1:
            text1 = my_font.render(sentence1,True,text_color)
            text0 = my_font.render(sentence0,True,(0,0,0))
            main_surface.blit(text0,(450,400))
            main_surface.blit(text1,(450,400))
        elif welcome_count == 2:
            text2 = my_font.render(sentence2,True,text_color)
            text1 = my_font.render(sentence1,True,(0,0,0))
            main_surface.blit(text1,(450,400))
            main_surface.blit(text2,(450,400))
        elif welcome_count == 3:
            text3 = my_font.render(sentence3,True,text_color)
            text2 = my_font.render(sentence2,True,(0,0,0))
            main_surface.blit(text2,(450,400))
            main_surface.blit(text3,(450,400))
        elif welcome_count == 4:
            text4 = my_font.render(sentence4,True,text_color)
            text3 = my_font.render(sentence3,True,(0,0,0))
            main_surface.blit(text3,(450,400))
            main_surface.blit(text4,(450,400))
        elif welcome_count == 5:
            text5 = my_font.render(sentence5,True,text_color)
            text4 = my_font.render(sentence4,True,(0,0,0))
            main_surface.blit(text4,(450,400))
            main_surface.blit(text5,(450,400))
        else: 
            輸入號碼(parameter,password)
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT or 新遊戲_end == True:       
            break
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            welcome_count += 1
            if event.type == pygame.KEYDOWN:
                key = event.dict["key"]
                if key == 13 and welcome_count > 6:
                     新遊戲_end = True
                if key == 8 and 1<=len(parameter)<=8 and welcome_count > 6:
                    parameter = parameter[:-1]
                    password = password[:-1]
                if key==ord("a") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'a'
                    password += '*'
                if key==ord("b") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'b'
                    password += '*'
                if key==ord("c") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'c'
                    password += '*'
                if key==ord("d") and len(parameter) <8  and welcome_count > 6:
                    parameter += 'd'
                    password += '*'
                if key==ord("e") and len(parameter) <8  and welcome_count > 6:
                    parameter += 'e'
                    password += '*'
                if key==ord("f") and len(parameter) <8  and welcome_count > 6:
                    parameter += 'f'
                    password += '*'
                if key==ord("g") and len(parameter) <8  and welcome_count > 6:
                    parameter += 'g'
                    password += '*'
                if key==ord("h") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'h'
                    password += '*'
                if key==ord("i") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'i'
                    password += '*'
                if key==ord("j") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'j'
                    password += '*'
                if key==ord("k") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'k'
                    password += '*'
                if key==ord("l") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'l'
                    password += '*'
                if key==ord("m") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'm'
                    password += '*'
                if key==ord("n") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'n'
                    password += '*'
                if key==ord("o") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'o'
                    password += '*'
                if key==ord("p") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'p'
                    password += '*'
                if key==ord("q") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'q'
                    password += '*'
                if key==ord("r") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'r'
                    password += '*'
                if key==ord("s") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 's'
                    password += '*'
                if key==ord("t") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 't'
                    password += '*'
                if key==ord("u") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'u'
                    password += '*'
                if key==ord("v") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'v'
                    password += '*'
                if key==ord("w") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'w'
                    password += '*'
                if key==ord("x") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'x'
                    password += '*'
                if key==ord("y") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'y'
                    password += '*'
                if key==ord("z") and len(parameter) < 8 and welcome_count > 6:
                    parameter += 'z'
                    password += '*'
                if key == 257 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '1'
                    password += '*'
                if key == 258 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '2'
                    password += '*'
                if key == 259 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '3'
                    password += '*'
                if key == 260 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '4'
                    password += '*'
                if key == 261 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '5'
                    password += '*'
                if key == 262 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '6'
                    password += '*'
                if key == 263 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '7'
                    password += '*'
                if key == 264 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '8'
                    password += '*'
                if key == 265 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '9'
                    password += '*'
                if key == 256 and len(parameter) < 8 and welcome_count > 6:
                    parameter += '0'
                    password += '*'
        welcome(welcome_count)
        pygame.display.flip()
    return parameter
hero1=hero()
weapon1=weapon()
package1=package()
def 新遊戲螢幕2():
    global hero1
    global weapon1
    global st
    ddd=startdata(st)
    weapon1=weapon(ddd[0])
    hero1=hero(ddd[1])
    新遊戲_end =False
    import pygame
    pygame.init()
    main_surface = pygame.display.set_mode((1530,800))
    main_surface.fill((0,0,0))
    welcome_count = 0
    def welcome(welcome_count):
        global hero1
        global weapon1
        my_font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 30)
        text_color = (255,255,255)
        sentence0 = '英雄誕生了'
        man = pygame.image.load("英雄.png")
        sentence00=f"英雄介紹：{hero1.intro()}"
        s01=f"武器介紹：{weapon1.intro()}"
        monster1 = pygame.image.load("青蛙1.png")
        monster2 = pygame.image.load("怪物1.png")
        monster3 = pygame.image.load("大怪.png")
        monster4 = pygame.image.load("炸彈怪.png")
        monster5 = pygame.image.load("未開寶箱.png")
        sentence1 = '您將面對兇惡的"YU-SIANG"'
        sentence2 = 'Small YU-SIANG'
        sentence3 = 'Medium YU-SIANG' 
        sentence4 = 'Large YU-SIANG'
        sentence5 = 'Bomb YU-SIANG'
        sentence6 = 'Treasure'
        s0="玩法介紹"
        s1="增加攻擊力(atk):按K鍵(消耗6000金錢)"
        s2="增加防禦力(shd):按S鍵(消耗2800金錢)"
        sentence7 = '前方危險，請小心應對'
        if welcome_count == 0:
            main_surface.fill((0,0,0))
            text0 = my_font.render(sentence0,True,text_color)
            main_surface.blit(text0,(450,400))
        elif welcome_count == 1:
            main_surface.fill((0,0,0))
            main_surface.blit(man, (500,100))
            text0 = my_font.render(sentence00,True,text_color)
            main_surface.blit(text0,(450,400))
            text0 = my_font.render(s01,True,text_color)
            main_surface.blit(text0,(450,500))
        elif welcome_count == 2:
            main_surface.fill((0,0,0))
            text1 = my_font.render(sentence1,True,text_color)
            main_surface.blit(text1,(450,400))
        elif welcome_count == 3:
            main_surface.fill((0,0,0))
            main_surface.blit(monster1, (500,100))
            text2 = my_font.render(sentence2,True,text_color)
            main_surface.blit(text2,(450,400))
        elif welcome_count == 4:
            main_surface.fill((0,0,0))
            main_surface.blit(monster2, (500,100))
            text3 = my_font.render(sentence3,True,text_color)
            main_surface.blit(text3,(450,400))
        elif welcome_count == 5:
            main_surface.fill((0,0,0))
            main_surface.blit(monster3, (500,100))
            text4 = my_font.render(sentence4,True,text_color)
            main_surface.blit(text4,(450,400))
        elif welcome_count == 6:
            main_surface.fill((0,0,0))
            main_surface.blit(monster4, (500,100))
            text5 = my_font.render(sentence5,True,text_color)
            main_surface.blit(text5,(450,400))
        elif welcome_count == 7:
            main_surface.fill((0,0,0))
            main_surface.blit(monster5, (500,100))
            text6 = my_font.render(sentence6,True,text_color)
            main_surface.blit(text6,(450,400))
        elif welcome_count==8:
            main_surface.fill((0,0,0))
            text7 = my_font.render(sentence7,True,text_color)
            main_surface.blit(text7,(450,400))
        else:
            main_surface.fill((0,0,0))
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            welcome_count += 1
        welcome(welcome_count)
        if welcome_count > 8:
            break
        pygame.display.flip()
import pygame
import time
def 遊戲螢幕():
    pygame.init()
    global loadin
    global weapon1
    global hero1
    global package1
    global mons1
    global mons2
    global mons3
    global mons4
    global mons5
    global mons6
    global mons7
    global mons8
    global mons9
    global timing
    global money
    global turn
    mons1 = monster(6)
    mons2 = monster(6)
    mons3 = monster(6)
    mons4 = monster(6)
    mons5 = monster(6)
    mons6 = monster(6)
    mons7 = monster(6)
    mons8 = monster(6)
    mons9 = monster(6)
    hammer1 = pygame.image.load("槌子1.png")
    hammer2 = pygame.image.load("槌子2.png")
    hammer3 = pygame.image.load("槌子3.png")
    monster1 = pygame.image.load("青蛙1.png")
    monster2 = pygame.image.load("怪物1.png")
    monster3 = pygame.image.load("大怪.png")
    monster4 = pygame.image.load("炸彈怪.png")
    monster5 = pygame.image.load("未開寶箱.png")
    man = pygame.image.load("英雄.png")
    pygame.mixer.init()
    pygame.mixer.music.load("hit.mp3")
    main_surface = pygame.display.set_mode((1530,800))
    my_font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 30)
    人物與怪獸字體 = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 15)
    def draw_grid(x,y):
        pygame.draw.polygon(main_surface,(100,100,0), ((480+x, 20+y), (588+x, 100+y), (547+x, 227+y), (412+x, 227+y), (370+x, 100+y)))
    def 選單格(文字,j):
        text = my_font.render(文字, True, (100,0,0))
        some_color = (200,100,0)
        some_rect = (1250,95+80*j,200,40)
        main_surface.fill(some_color, some_rect)
        main_surface.blit(text,(1265,100+80*j))
    def 槌子攻擊(N,鎚子count):
        global weapon1
        global hero1
        global mons1
        global mons2
        global mons3
        global mons4
        global mons5
        global mons6
        global mons7
        global mons8
        global mons9
        global package1
        global money
        global timing
        a = (N-1)//3
        b = (N-1)%3
        if 15>=槌子count>=11:
            main_surface.blit(hammer1, (250+250*b, -75+250*(2-a)))
        if 10>=槌子count>=6:
            main_surface.blit(hammer2, (365+i+250*b, 30+i+250*(2-a)))
        if 5>=槌子count>=1:    
            main_surface.blit(hammer3, (420+250*b, 65+250*(2-a)))
        if N == 1 and 槌子count == 14:
            atk_mons1()
        if N == 2 and 槌子count == 14:
            atk_mons2()
        if N == 3 and 槌子count == 14:
            atk_mons3()
        if N == 4 and 槌子count == 14:
            atk_mons4()
        if N == 5 and 槌子count == 14:
            atk_mons5()
        if N == 6 and 槌子count == 14:
            atk_mons6()
        if N == 7 and 槌子count == 14:
            atk_mons7()
        if N == 8 and 槌子count == 14:
            atk_mons8()
        if N == 9 and 槌子count == 14:
            atk_mons9()
    def 畫背包():
        global package1
        big_rect = [(200,100,0),(1200,650,310,70)]
        main_surface.fill(big_rect[0],big_rect[1])
        for i in range(5):
            main_surface.fill((250,150,150),(1210+60*i,660,50,50))
        index1 = 人物與怪獸字體.render("補血1號",True,(0,0,0))
        index2 = 人物與怪獸字體.render("補血2號",True,(0,0,0))
        index3 = 人物與怪獸字體.render("補血3號",True,(0,0,0))
        index4 = 人物與怪獸字體.render("無敵星星",True,(0,0,0))
        index5 = 人物與怪獸字體.render("復活卡",True,(0,0,0))
        blood1 = 人物與怪獸字體.render('X'+str(package1.p1),True,(0,0,0))
        blood2 = 人物與怪獸字體.render('X'+str(package1.p2),True,(0,0,0))
        blood3 = 人物與怪獸字體.render('X'+str(package1.p3),True,(0,0,0))
        無敵星星 = 人物與怪獸字體.render('X'+str(package1.p4),True,(0,0,0))
        復活 = 人物與怪獸字體.render('X'+str(package1.p5),True,(0,0,0))
        main_surface.blit(index1,(1220,670))
        main_surface.blit(index2,(1280,670))
        main_surface.blit(index3,(1340,670))
        main_surface.blit(index4,(1400,670))
        main_surface.blit(index5,(1460,670))
        main_surface.blit(blood1,(1220,690))
        main_surface.blit(blood2,(1280,690))
        main_surface.blit(blood3,(1340,690))
        main_surface.blit(無敵星星,(1400,690))
        main_surface.blit(復活,(1460,690))
    def atk_mons1():
        global weapon1
        global mons1
        if weapon1.dur>=1:
            weapon1.use()
            pygame.mixer.music.play()
            mons1.hp-=weapon1.atk
            if weapon1.N==5:
                global mons2,mons4
                mons2.hp-=int(weapon1.atk*0.1)
                mons4.hp-=int(weapon1.atk*0.1)
    def atk_mons2():
        global weapon1
        global mons2
        if weapon1.dur>=1:
            weapon1.use()
            pygame.mixer.music.play()
            mons2.hp-=weapon1.atk
            if weapon1.N==5:
                global mons1,mons3,mons5
                mons1.hp-=int(weapon1.atk*0.1)
                mons3.hp-=int(weapon1.atk*0.1)
                mons5.hp-=int(weapon1.atk*0.1)
    def atk_mons3():
        global weapon1
        global mons3
        if weapon1.dur>=1:
            weapon1.use()
            pygame.mixer.music.play()
            mons3.hp-=weapon1.atk
            if weapon1.N==5:
                global mons2,mons6
                mons2.hp-=int(weapon1.atk*0.1)
                mons6.hp-=int(weapon1.atk*0.1)
    def atk_mons4():
        global weapon1
        global mons4
        if weapon1.dur>=1:
            weapon1.use()
            pygame.mixer.music.play()
            mons4.hp-=weapon1.atk
            if weapon1.N==5:
                global mons1,mons5,mons7
                mons1.hp-=int(weapon1.atk*0.1)
                mons7.hp-=int(weapon1.atk*0.1)
                mons5.hp-=int(weapon1.atk*0.1)
    def atk_mons5():
        global weapon1
        global mons5
        if weapon1.dur>=1:
            weapon1.use()
            pygame.mixer.music.play()
            mons5.hp-=weapon1.atk
            if weapon1.N==5:
                global mons2,mons4,mons6,mons8
                mons2.hp-=int(weapon1.atk*0.1)
                mons4.hp-=int(weapon1.atk*0.1)
                mons6.hp-=int(weapon1.atk*0.1)
                mons8.hp-=int(weapon1.atk*0.1)
    def atk_mons6():
        global weapon1
        global mons6
        if weapon1.dur>=1:
            weapon1.use()
            pygame.mixer.music.play()
            mons6.hp-=weapon1.atk
            if weapon1.N==5:
                global mons9,mons5,mons3
                mons3.hp-=int(weapon1.atk*0.1)
                mons5.hp-=int(weapon1.atk*0.1)
                mons9.hp-=int(weapon1.atk*0.1)
    def atk_mons7():
        global weapon1
        global mons7
        if weapon1.dur>=1:
            weapon1.use()
            pygame.mixer.music.play()
            mons7.hp-=weapon1.atk
            if weapon1.N==5:
                global mons4,mons8
                mons4.hp-=int(weapon1.atk*0.1)
                mons8.hp-=int(weapon1.atk*0.1)
    def atk_mons8():
        global weapon1
        global mons8
        if weapon1.dur>=1:
            weapon1.use()
            pygame.mixer.music.play()
            mons8.hp-=weapon1.atk
            if weapon1.N==5:
                global mons7,mons5,mons9
                mons7.hp-=int(weapon1.atk*0.1)
                mons5.hp-=int(weapon1.atk*0.1)
                mons9.hp-=int(weapon1.atk*0.1)
    def atk_mons9():
        global weapon1
        global mons9
        if weapon1.dur>=1:
            weapon1.use()
            pygame.mixer.music.play()
            mons9.hp-=weapon1.atk
            if weapon1.N==5:
                global mons8,mons6
                mons6.hp-=int(weapon1.atk*0.1)
                mons8.hp-=int(weapon1.atk*0.1)
    def 怪獸出現(種類,N):
        if 種類 == 1:
            a = (N-1)//3
            b = (N-1)%3
            main_surface.blit(monster1, (380+250*b, 50+250*(2-a)))
        elif 種類 == 2:
            a = (N-1)//3
            b = (N-1)%3
            main_surface.blit(monster2, (255+250*b, 10+250*(2-a)))
        elif 種類 == 4:
            a = (N-1)//3
            b = (N-1)%3
            main_surface.blit(monster4, (225+250*b, -10+250*(2-a)))   
        elif 種類 == 3:
            a = (N-1)//3
            b = (N-1)%3
            main_surface.blit(monster3, (265+250*b, -10+250*(2-a)))
        elif 種類 == 5:
            a = (N-1)//3
            b = (N-1)%3
            main_surface.blit(monster5, (330+250*b, -10+250*(2-a))) 
    def weapon_alv_up():
        global weapon1
        global money
        if weapon1.N==2:
            if money>=4900:
                money-=4900
                weapon1.alv_up()
        else:
            if money>=5000:
                money-=5000
                weapon1.alv_up()
    def weapon_slv_up():
        global weapon1
        global money
        if weapon1.N==2:
            if money>=2750:
                money-=2750
                weapon1.slv_up()
        else:
            if money>=2800:
                money-=2800
                weapon1.slv_up()
    def weapon_dur_heal():
        global weapon1
        global money
        if weapon1.N==2:
            if money>=5400:
                money-=5400
                weapon1.dur_heal()
        else:
            if money>=5500:
                money-=5500
                weapon1.dur_heal()
    def generate_mons1():
        global mons1
        global timing
        def mons1_atk():
            global weapon1
            global hero1
            global mons1
            a=mons1.atk-weapon1.shd
            if a<=10:
                a=10
            hero1.hp-=a
        if mons1.N == 6:
            import random
            number = random.randint(1,800)
            if number == 1:
                mons1 = monster(monsappear())
        elif mons1.N == 1 or mons1.N == 2 or mons1.N == 3 or mons1.N == 4 or mons1.N == 5:
            if mons1.N == 1:
                怪獸出現(1,1)
            if mons1.N == 2:
                怪獸出現(2,1)
            if mons1.N == 3:
                怪獸出現(3,1)
            if mons1.N == 4:
                怪獸出現(4,1)
            if mons1.N == 5 and mons1.hp > 0:
                怪獸出現(5,1)
            if (time.time()-mons1.time)%(1*0.99**(timing//20)+1.5) <= 0.008 and time.time()-mons1.time>(1*0.99**turn+1.5) and mons1.hp>0:
                if mons1.N!=5:
                    mons1_atk()
                else:
                    mons1_dead()
    def generate_mons2():
        global mons2
        global turn
        def mons2_atk():
            global weapon1
            global hero1
            global mons2
            a=mons1.atk-weapon1.shd
            if a<=10:
                a=10
            hero1.hp-=a
        if mons2.N == 6:
            import random
            number = random.randint(1,800)
            if number == 1:
                mons2 = monster(monsappear())
        elif mons2.N == 1 or mons2.N == 2 or mons2.N == 3 or mons2.N == 4 or mons2.N == 5:
            if mons2.N == 1:
                怪獸出現(1,2)
            if mons2.N == 2:
                怪獸出現(2,2)
            if mons2.N == 3:
                怪獸出現(3,2)
            if mons2.N == 4:
                怪獸出現(4,2)
            if mons2.N == 5 and mons2.hp > 0:
                怪獸出現(5,2)
            if abs((time.time()-mons2.time)%(1*0.99**(timing//20)+1.5) )<= 0.008 and time.time()-mons2.time>(1*0.99**turn+1.5) and mons2.hp>0:
                if mons2.N!=5:
                    mons2_atk()
                else:
                    mons2_dead()
    def generate_mons3():
        global mons3
        global turn
        def mons3_atk():
            global weapon1
            global hero1
            global mons3
            a=mons3.atk-weapon1.shd
            if a<=10:
                a=10
            hero1.hp-=a
        if mons3.N == 6:
            import random
            number = random.randint(1,800)
            if number == 1:
                mons3 = monster(monsappear())
        else:
            怪獸出現(mons3.N,3)
            if abs((time.time()-mons3.time)%(1*0.99**(timing//20)+1.5) )<= 0.008 and time.time()-mons3.time>(1*0.99**turn+1.5) and mons3.hp>0:
                if mons3.N!=5:
                    mons3_atk()
                else:
                    mons3_dead()
    def generate_mons4():
        global mons4
        global turn
        def mons4_atk():
            global mons4
            global weapon1
            global hero1
            a=mons4.atk-weapon1.shd
            if a<=10:
                a=10
            hero1.hp-=a
        if mons4.N == 6:
            import random
            number = random.randint(1,800)
            if number == 1:
                mons4 = monster(monsappear())
        elif mons4.N == 1 or mons4.N == 2 or mons4.N == 3 or mons4.N == 4 or mons4.N == 5:
            if mons4.N == 1:
                怪獸出現(1,4)
            if mons4.N == 2:
                怪獸出現(2,4)
            if mons4.N == 3:
                怪獸出現(3,4)
            if mons4.N == 4:
                怪獸出現(4,4)
            if mons4.N == 5 and mons4.hp > 0:
                怪獸出現(5,4)
            if abs((time.time()-mons4.time)%(1*0.99**(timing//20)+1.5) )<= 0.008 and time.time()-mons4.time>(1*0.99**turn+1.5) and mons4.hp>0:
                if mons4.N!=5:
                    mons4_atk()
                else:
                    mons4_dead()
    def generate_mons5():
        global mons5
        global turn
        def mons5_atk():
            global mons5
            global weapon1
            global hero1
            a=mons5.atk-weapon1.shd
            if a<=10:
                a=10
            hero1.hp-=a
        if mons5.N == 6:
            import random
            number = random.randint(1,800)
            if number == 1:
                mons5 = monster(monsappear())
        elif mons5.N == 1 or mons5.N == 2 or mons5.N == 3 or mons5.N == 4 or mons5.N == 5:
            if mons5.N == 1:
                怪獸出現(1,5)
            if mons5.N == 2:
                怪獸出現(2,5)
            if mons5.N == 3:
                怪獸出現(3,5)
            if mons5.N == 4:
                怪獸出現(4,5)
            if mons5.N == 5 and mons5.hp > 0:
                怪獸出現(5,5)
            if abs((time.time()-mons5.time)%(1*0.99**(timing//20)+1.5) )<= 0.008 and time.time()-mons5.time>(1*0.99**turn+1.5) and mons5.hp>0:
                if mons5.N!=5:
                    mons5_atk()
                else:
                    mons5_dead()
    def generate_mons6():
        global mons6
        global turn
        def mons6_atk():
            global mons6
            global weapon1
            global hero1
            a=mons6.atk-weapon1.shd
            if a<=10:
                a=10
            hero1.hp-=a
        if mons6.N == 6:
            import random
            number = random.randint(1,800)
            if number == 1:
                mons6 = monster(monsappear())
        elif mons6.N == 1 or mons6.N == 2 or mons6.N == 3 or mons6.N == 4 or mons6.N == 5:
            if mons6.N == 1:
                怪獸出現(1,6)
            if mons6.N == 2:
                怪獸出現(2,6)
            if mons6.N == 3:
                怪獸出現(3,6)
            if mons6.N == 4:
                怪獸出現(4,6)
            if mons6.N == 5 and mons6.hp > 0:
                怪獸出現(5,6)
            if abs((time.time()-mons6.time)%(1*0.99**(timing//20)+1.5) )<= 0.008 and time.time()-mons6.time>(1*0.99**turn+1.5) and mons6.hp>0:
                if mons6.N!=5:
                    mons6_atk()
                else:
                    mons6_dead()
    def generate_mons7():
        global mons7
        global turn
        def mons7_atk():
            global mons7
            global weapon1
            global hero1
            a=mons7.atk-weapon1.shd
            if a<=10:
                a=10
            hero1.hp-=a
        if mons7.N == 6:
            import random
            number = random.randint(1,800)
            if number == 1:
                mons7 = monster(monsappear())
        elif mons7.N == 1 or mons7.N == 2 or mons7.N == 3 or mons7.N == 4 or mons7.N == 5:
            if mons7.N == 1:
                怪獸出現(1,7)
            if mons7.N == 2:
                怪獸出現(2,7)
            if mons7.N == 3:
                怪獸出現(3,7)
            if mons7.N == 4:
                怪獸出現(4,7)
            if mons7.N == 5 and mons7.hp > 0:
                怪獸出現(5,7)
            if abs((time.time()-mons7.time)%(1*0.99**(timing//20)+1.5) )<= 0.008 and time.time()-mons7.time>(1*0.99**turn+1.5)and mons7.hp>0:
                if mons7.N!=5:
                    mons7_atk()
                else:
                    mons7_dead()
    def generate_mons8():
        global mons8
        global turn
        def mons8_atk():
            global mons8
            global weapon1
            global hero1
            a=mons8.atk-weapon1.shd
            if a<=10:
                a=10
            hero1.hp-=a
        if mons8.N == 6:
            import random
            number = random.randint(1,800)
            if number == 1:
                mons8 = monster(monsappear())
        elif mons8.N == 1 or mons8.N == 2 or mons8.N == 3 or mons8.N == 4 or mons8.N == 5:
            if mons8.N == 1:
                怪獸出現(1,8)
            if mons8.N == 2:
                怪獸出現(2,8)
            if mons8.N == 3:
                怪獸出現(3,8)
            if mons8.N == 4:
                怪獸出現(4,8)
            if mons8.N == 5 and mons8.hp > 0:
                怪獸出現(5,8)
            if abs((time.time()-mons8.time)%(1*0.99**(timing//20)+1.5) )<= 0.008 and time.time()-mons8.time>(1*0.99**turn+1.5) and mons8.hp>0:
                if mons8.N!=5:
                    mons8_atk()
                else:
                    mons8_dead()
    def generate_mons9():
        global mons9
        global turn
        def mons9_atk():
            global weapon1
            global hero1
            global mons9
            a=mons9.atk-weapon1.shd
            if a<=10:
                a=10
            hero1.hp-=a
        if mons9.N == 6:
            import random
            number = random.randint(1,800)
            if number == 1:
                mons9 = monster(monsappear())
        elif mons9.N == 1 or mons9.N == 2 or mons9.N == 3 or mons9.N == 4 or mons9.N == 5:
            if mons9.N == 1:
                怪獸出現(1,9)
            if mons9.N == 2:
                怪獸出現(2,9)
            if mons9.N == 3:
                怪獸出現(3,9)
            if mons9.N == 4:
                怪獸出現(4,9)
            if mons9.N == 5 and mons9.hp > 0:
                怪獸出現(5,9)
            if abs((time.time()-mons9.time)%(1*0.99**(timing//20)+1.5) )<= 0.008 and time.time()-mons9.time>(1*0.99**turn+1.5)  and mons9.hp>0:
                if mons9.N!=5:
                    mons9_atk()
                else:
                    mons9_dead()
    def mons1_dead():
        global hero1
        global mons1
        global money
        import random
        if mons1.hp<=0:
            if mons1.N==1:
                mons1=monster(6)
                hero1.getexp(30)
                money+=random.randint(600,1100)
            elif mons1.N==2:
                mons1=monster(6)
                hero1.getexp(50)
                money+=random.randint(1300,1800)
            elif mons1.N==3:
                mons1=monster(6)
                hero1.getexp(70)
                money+=random.randint(2200,2700)
            elif mons1.N==4:
                mons1=monster(6)
                hero1.getexp(55)
                money+=1700
            elif mons1.N==5:
                mons1=monster(6)
                money+=1
                hero1.getexp(1)
                get_treasure()
        elif time.time()-mons1.time>10 and mons1.N!=6:
            hero1.hp-=int(mons1.atk*0.7)
            mons1=monster(6)
    def mons2_dead(): 
        global hero1
        global mons2
        global money
        import random
        if mons2.hp<=0:
            if mons2.N==1:
                mons2=monster(6)
                hero1.getexp(30)
                money+=random.randint(600,1100)
            elif mons2.N==2:
                mons2=monster(6)
                hero1.getexp(50)
                money+=random.randint(1300,1800)
            elif mons2.N==3:
                mons2=monster(6)
                hero1.getexp(70)
                money+=random.randint(2200,2700)
            elif mons2.N==4:
                mons2=monster(6)
                hero1.getexp(55)
                money+=1700
            elif mons2.N==5:
                mons2=monster(6)
                money+=1
                hero1.getexp(1)
                get_treasure()
        elif time.time()-mons2.time>10 and mons2.N!=6:
            hero1.hp-=int(mons2.atk*0.7)
            mons2=monster(6)
    def mons3_dead():
        global hero1
        global mons3
        global money
        import random
        if mons3.hp<=0:
            if mons3.N==1:
                mons3=monster(6)
                hero1.getexp(30)
                money+=random.randint(600,1100)
            elif mons3.N==2:
                mons3=monster(6)
                hero1.getexp(50)
                money+=random.randint(1300,1800)
            elif mons3.N==3:
                mons3=monster(6)
                hero1.getexp(70)
                money+=random.randint(2200,2700)
            elif mons3.N==4:
                mons3=monster(6)
                hero1.getexp(55)
                money+=1700
            elif mons3.N==5:
                mons3=monster(6)
                money+=1
                hero1.getexp(1)
                get_treasure()
        elif time.time()-mons3.time>10 and mons3.N!=6:
            hero1.hp-=int(mons3.atk*0.7)
            mons3=monster(6)
    def mons4_dead():
        import random
        global hero1
        global mons4
        global money
        if mons4.hp<=0:
            if mons4.N==1:
                mons4=monster(6)
                hero1.getexp(30)
                money+=random.randint(600,1100)
            elif mons4.N==2:
                mons4=monster(6)
                hero1.getexp(50)
                money+=random.randint(1300,1800)
            elif mons4.N==3:
                mons4=monster(6)
                hero1.getexp(70)
                money+=random.randint(2200,2700)
            elif mons4.N==4:
                mons4=monster(6)
                hero1.getexp(55)
                money+=1700
            elif mons4.N==5:
                mons4=monster(6)
                money+=1
                hero1.getexp(1)
                get_treasure()
        elif time.time()-mons4.time>10 and mons4.N!=6:
            hero1.hp-=int(mons4.atk*0.7)
            mons4=monster(6)
    def mons5_dead():
        global hero1
        global mons5
        global money
        import random
        if mons5.hp<=0:
            if mons5.N==1:
                mons5=monster(6)
                hero1.getexp(30)
                money+=random.randint(600,1100)
            elif mons5.N==2:
                mons5=monster(6)
                hero1.getexp(50)
                money+=random.randint(1300,1800)
            elif mons5.N==3:
                mons5=monster(6)
                hero1.getexp(70)
                money+=random.randint(2200,2700)
            elif mons5.N==4:
                mons5=monster(6)
                hero1.getexp(55)
                money+=1700
            elif mons5.N==5:
                mons5=monster(6)
                money+=1
                hero1.getexp(1)
                get_treasure()
        elif time.time()-mons5.time>10 and mons5.N!=6:
            hero1.hp-=int(mons5.atk*0.7)
            mons5=monster(6)
    def mons6_dead():
        global hero1
        global mons6
        global money
        import random
        if mons6.hp<=0:
            if mons6.N==1:
                mons6=monster(6)
                hero1.getexp(30)
                money+=random.randint(600,1100)
            elif mons6.N==2:
                mons6=monster(6)
                hero1.getexp(50)
                money+=random.randint(1300,1800)
            elif mons6.N==3:
                mons6=monster(6)
                hero1.getexp(70)
                money+=random.randint(2200,2700)
            elif mons6.N==4:
                mons6=monster(6)
                hero1.getexp(55)
                money+=1700
            elif mons6.N==5:
                mons6=monster(6)
                money+=1
                hero1.getexp(1)
                get_treasure()
        elif time.time()-mons6.time>10 and mons6.N!=6:
            hero1.hp-=int(mons6.atk*0.7)
            mons6=monster(6)
    def mons7_dead():
        global mons7
        global money
        global hero1
        import random
        if mons7.hp<=0:
            if mons7.N==1:
                mons7=monster(6)
                hero1.getexp(30)
                money+=random.randint(600,1100)
            elif mons7.N==2:
                mons7=monster(6)
                hero1.getexp(50)
                money+=random.randint(1300,1800)
            elif mons7.N==3:
                mons7=monster(6)
                hero1.getexp(70)
                money+=random.randint(2200,2700)
            elif mons7.N==4:
                mons7=monster(6)
                hero1.getexp(55)
                money+=1700
            elif mons7.N==5:
                mons7=monster(6)
                money+=1
                hero1.getexp(1)
                get_treasure()
        elif time.time()-mons7.time>10 and mons6.N!=6:
            hero1.hp-=int(mons7.atk*0.7)
            mons7=monster(6)
    def mons8_dead():
        global hero1
        global mons8
        global money
        import random
        if mons8.hp<=0:
            if mons8.N==1:
                mons8=monster(6)
                hero1.getexp(30)
                money+=random.randint(600,1100)
            elif mons8.N==2:
                mons8=monster(6)
                hero1.getexp(50)
                money+=random.randint(1300,1800)
            elif mons8.N==3:
                mons8=monster(6)
                hero1.getexp(70)
                money+=random.randint(2200,2700)
            elif mons8.N==4:
                mons8=monster(6)
                hero1.getexp(55)
                money+=1700
            elif mons8.N==5:
                mons8=monster(6)
                money+=1
                hero1.getexp(1)
                get_treasure()
        elif time.time()-mons8.time>10 and mons8.N!=6:
            hero1.hp-=int(mons8.atk*0.7)
            mons8=monster(6)
    def mons9_dead():
        global hero1
        global mons9
        global money
        import random
        if mons9.hp<=0:
            if mons9.N==1:
                mons9=monster(6)
                hero1.getexp(30)
                money+=random.randint(700,1000)
            elif mons9.N==2:
                mons9=monster(6)
                hero1.getexp(50)
                money+=random.randint(1300,1700)
            elif mons9.N==3:
                mons9=monster(6)
                hero1.getexp(70)
                money+=random.randint(2100,2600)
            elif mons9.N==4:
                mons9=monster(6)
                hero1.getexp(55)
                money+=1800
            elif mons9.N==5:
                mons9=monster(6)
                get_treasure()
        elif time.time()-mons9.time>10 and mons9.N!=6:
            hero1.hp-=int(mons9.atk*0.7)
            mons9=monster(6)
    def saving():
        pygame.init()
        global proceed
        global start_time
        proceed=False
        savename=""
        main_surface = pygame.display.set_mode((1530,800))
        font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 20)
        new_font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 60)
        some_color = (255,255,200)
        somerect = (500,400,450,50)
        the_text = font.render('請輸入要存檔的檔案名字(不須加".txt")，輸入完後按Enter:',True,(255,255,255))
        new_text = new_font.render(savename,True,(0,0,0))
        main_surface.blit(the_text,(500,375))
        main_surface.blit(new_text,(520,405))
        while True:
            main_surface.fill((0,0,0))
            main_surface.fill(some_color,somerect)
            new_text = new_font.render(savename,True,(0,0,0))
            main_surface.blit(the_text,(500,375))
            main_surface.blit(new_text,(520,405))
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            if ev.type==pygame.KEYDOWN:
                key = ev.dict["key"]
                if key == 13:
                    savename+=".txt"
                    save(savename)
                    start_time=time.time()-timing
                    break
                elif key == 8:
                    savename=savename[:(-1)]
                if key==ord("q"):
                    savename+="q"
                elif key==ord("w"):
                    savename+= 'w'
                elif key==ord("e"):
                    savename+= 'e'
                elif key==ord("r"):
                    savename+= 'r'
                elif key==ord("t"):
                    savename+= 't'
                elif key==ord("y"):
                    savename+= 'y'
                elif key==ord("u"):
                    savename+= 'u'
                elif key==ord("i"):
                    savename+= 'i'
                elif key==ord("o"):
                    savename+= 'o'
                elif key==ord("p"):
                    savename+= 'p'
                elif key==ord("a"):
                    savename+= 'a'
                elif key==ord("s"):
                    savename+= 's'
                elif key==ord("d"):
                    savename+= 'd'
                elif key==ord("f"):
                    savename+= 'f'
                elif key==ord("g"):
                    savename+= 'g'
                elif key==ord("h"):
                    savename+= 'h'
                elif key==ord("j"):
                    savename+= 'j'
                elif key==ord("k"):
                    savename+= 'k'
                elif key==ord("l"):
                    savename+= 'l'
                elif key==ord("z"):
                    savename+= 'z'
                elif key==ord("x"):
                    savename+= 'x'
                elif key==ord("c"):
                    savename+= 'c'
                elif key==ord("v"):
                    savename+= 'v'
                elif key==ord("b"):
                    savename+= 'b'
                elif key==ord("n"):
                    savename+= 'n'
                elif key==ord("m"):
                    savename+= 'm'
                elif key==49 or key==257:
                    savename+="1"
                elif key==50 or key==258:
                    savename+="2"
                elif key==51 or key==259:
                    savename+="3"
                elif key==52 or key==260:
                    savename+="4"
                elif key==53 or key==261:
                    savename+="5"
                elif key==54 or key==262:
                    savename+="6"
                elif key==55 or key==263:
                    savename+="7"
                elif key==56 or key==264:
                    savename+="8"
                elif key==57 or key==265:
                    savename+="9"
                elif key==48 or key==256:
                    savename+="0"
            pygame.display.flip()
    槌子count=0
    global proceed
    proceed = True
    money=0
    global a
    if loadin==True:
        proceed=False
        global loadname
        with open(loadname,"r")as f:
            aa=f.read()
        aa=aa[1:(-1)]
        aa=aa.split(", ")
        if aa!=[]:
            global hero1
            global weapon1
            hero1=hero(int(aa[0]))
            weapon1=weapon(int(aa[1]))
            money+=int(aa[2])
            a=int(aa[3])
            mons1.N=int(aa[4])
            mons2.N=int(aa[5])
            mons3.N=int(aa[6])
            mons4.N=int(aa[7])
            mons5.N=int(aa[8])
            mons6.N=int(aa[9])
            mons7.N=int(aa[10])
            mons8.N=int(aa[11])
            mons9.N=int(aa[12])
            package1.p1=int(aa[13])
            package1.p2=int(aa[14])
            package1.p3=int(aa[15])
            package1.p4=int(aa[16])
            package1.p5=int(aa[17])
            hero1.getexp(int(aa[18]))
            hero1.hp=int(aa[19])
            weapon1.alv=int(aa[20])
            weapon1.atk+=int(aa[20])*38
            weapon1.slv=int(aa[21])
            weapon1.shd+=int(aa[21])*20
            weapon1.dur=int(aa[22])
            mons1.hp=int(aa[23])
            mons2.hp=int(aa[24])
            mons3.hp=int(aa[25])
            mons4.hp=int(aa[26])
            mons5.hp=int(aa[27])
            mons6.hp=int(aa[28])
            mons7.hp=int(aa[29])
            mons8.hp=int(aa[30])
            mons9.hp=int(aa[31])
            mons1.atk=int(aa[32])
            mons2.atk=int(aa[33])
            mons3.atk=int(aa[34])
            mons4.atk=int(aa[35])
            mons5.atk=int(aa[36])
            mons6.atk=int(aa[37])
            mons7.atk=int(aa[38])
            mons8.atk=int(aa[39])
            mons9.atk=int(aa[40])
    start_time = time.time()-a
    while True:
        now = time.time()
        timing = now -start_time
        turn = timing//20
        ev = pygame.event.poll()
        main_surface.fill((150, 200, 0))
        if ev.type == pygame.QUIT : # Window close button clicked?
            break # Leave game loop
        if hero1.hp<=0:
            main_surface.fill((0,0,0))
            my_font = pygame.font.Font("TaipeiSansTCBeta-Regular.ttf", 30)
            string=my_font.render("世界因為勇者死亡而毀滅了",True,(250,250,250))
            main_surface.blit(string,(500,400))
            pygame.display.flip()
            time.sleep(3)
            main_surface.fill((0,0,0))
            string=my_font.render("Game Over",True,(250,250,250))
            main_surface.blit(string,(500,400))
            pygame.display.flip()
            time.sleep(2)
            break
        for i in range(3):
            for j in range(3):
                draw_grid(250*i,250*j)    
        畫背包()
        選單格("暫停: J",0)
        選單格("技能: I",1)
        選單格("ATK up: N",2)
        選單格("DUR heal: K",3)
        選單格(str(int(timing))+"s",4)
        選單格("Slv_up：s",5)
        選單格("背包格:ZXCV(順序)",6)
        main_surface.blit(man, (25, 10))
        data1 = my_font.render(f"hp: {int(hero1.hp)}/ {hero1.hp_max}",True,(0,0,0))
        data2 = my_font.render(f"lv: {hero1.lv}",True,(0,0,0))
        data3 = my_font.render(f"exp: {hero1.exp}/500",True,(0,0,0))
        data4 = my_font.render(f"endurance: {weapon1.dur}",True,(0,0,0)) 
        data5 = my_font.render(f"money: {money}",True,(0,0,0))
        data6 = my_font.render(f"技能CD: {max(int(weapon1.cd-timing),0)}",True,(0,0,0))
        data7 = my_font.render(f"shield: {weapon1.shd}",True,(0,0,0))
        data8 = my_font.render(f"attack: {weapon1.atk}",True,(0,0,0))
        main_surface.blit(data1,(30,180))
        main_surface.blit(data2,(30,220))
        main_surface.blit(data3,(30,260))
        main_surface.blit(data4,(30,300))
        main_surface.blit(data5,(30,340))
        main_surface.blit(data6,(30,380))
        main_surface.blit(data7,(30,420))
        main_surface.blit(data8,(30,460))
        if proceed == True:
            generate_mons1()
            generate_mons2()
            generate_mons3()
            generate_mons4()
            generate_mons5()
            generate_mons6()
            generate_mons7()
            generate_mons8()
            generate_mons9()
            mons1_dead()
            mons2_dead()
            mons3_dead()
            mons4_dead()
            mons5_dead()
            mons6_dead()
            mons7_dead()
            mons8_dead()
            mons9_dead()
            package1.p4_skill()
        else:
            start_time=time.time()-a
            mons1.time=time.time()
            mons2.time=time.time()
            mons3.time=time.time()
            mons4.time=time.time()
            mons5.time=time.time()
            mons6.time=time.time()
            mons7.time=time.time()
            mons8.time=time.time()
            mons9.time=time.time()
        if ev.type==pygame.KEYDOWN:
            key = ev.dict["key"]
            if key==ord("i"):   #按i鍵發動技能
                weapon1.skill()
            if key==ord("k"):
                weapon_dur_heal()
            if key==ord("n"):
                weapon_alv_up()
            if key ==ord("s"):
                weapon_slv_up()
            if key == ord("j"):
                proceed = proceed^True
                a=int(timing)
            if key==ord("v") and package1.p4_cd<timing and package1.p4>=1:
                package1.use_p4()
                weapon1.shd+=100000
            if key==ord("z"):
                package1.use_p1()
            if key==ord("x"):
                package1.use_p2()
            if key==ord("c"):
                package1.use_p3()
            if key==ord("q"):
                saving()
            槌子count=15
            KEY=key-256
        if 槌子count>0 and KEY >= 1 and proceed == True:
            槌子count-=1
            槌子攻擊(KEY,槌子count)
        pygame.display.flip()
    pygame.quit()
def main():
    package1=package
    import pygame
    新遊戲_end = False
    global loadin
    menu()
    if loadin==False:
        global st
        st=新遊戲螢幕(新遊戲_end)
        新遊戲螢幕2()
    遊戲螢幕() 
main()