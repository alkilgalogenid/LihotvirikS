x=683
y=384
q=0
b1=28
b2=250
b3=0
d=0
f=150
b=0
x1=90
y1=90
v=0
title=""
pl=0
sl=0

class Stone:
    def __init__(self,x,y,dx,dy, speed = 1.35):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.speed = speed
    def draw_(self):
        print self.x
        push()
        rect(self.x,self.y,self.dx,self.dy)
        fill(100,100,100)
        pop()
    def check_(self,x,y):
        if x >= self.x and x <= self.x+self.dx and y >= self.y and y <= self.y + self.dy:
            return 0
        else:
            return 1
class StoneList:
    def __init__(self):
        self.charge_(1)
    def charge_(self,Level):
        self.lst=[]
        if Level == 1:
            self.append_(100,0,50,50, random(1.5,4.5))
            self.append_(200,0,50,50, random(1.5,4.5))
            self.append_(300,0,50,50, random(1.5,4.5))
            self.append_(400,0,50,50, random(1.5,4.5))
            self.append_(500,0,50,50, random(1.5,4.5))
            self.append_(600,0,50,50, random(1.5,4.5))
            self.append_(700,0,50,50, random(1.5,4.5))
            self.append_(800,0,50,50, random(1.5,4.5))
            self.append_(900,0,50,50, random(1.5,4.5))
            self.append_(1000,0,50,50, random(1.5,4.5))
    def append_(self,x,y,dx,dy,speed = 1.35):
        Opasnost = Stone(x,y,dx,dy , speed)
        self.lst.append(Opasnost)
    def fall_(self, diff):
        for item in self.lst:
            item.y += item.speed
    def draw_(self):
        for item in self.lst:
            item.draw_()
    def check_(self,player):
        check = 1
        for item in self.lst:
            check = item.check_(player.x , player.y)*\
            item.check_(player.x + 75 , player.y)*\
            item.check_(player.x , player.y + 75)*\
            item.check_(player.x +75, player.y + 75)
            if check == 0:
                return check
        return check
#class PlayerList:
#    def __init__(self):
#        self.charge_()    
#    def charge_(self):
#        self.lst=[]
#            self.append_(100,0,50,50, random(1.5,4.5))
#    def append_(self,x,y,key_up,key_dn,key_rt,key_lt,step):
#        pln = Player(x,y,key_up,key_dn,key_rt,key_lt,step)
#        self.lst.append(pln)
#    def draw_(self):
#        for item in self.lst:
#            item.draw_()
class Player:
    def __init__(self,x,y,key_up,key_dn,key_rt,key_lt,step):
        self.init_x=x
        self.init_y=y
        self.x=x
        self.y=y
        self.key_up = key_up
        self.key_dn = key_dn
        self.key_rt = key_rt
        self.key_lt = key_lt
        self.step = step
    def start_(self):
        self.x = self.init_x
        self.y = self.init_y
    def draw_(self):
        rect(self.x,self.y,20,20)
        fill(0)
#        image(img6,self.x,self.y,75,75)
    def control_(self, key_):
        if key == self.key_up:
            self.y = self.y - self.step
        if key == self.key_dn:
            self.y = self.y + self.step
        if key == self.key_lt:
            self.x = self.x - self.step
        if key == self.key_rt:
            self.x = self.x + self.step
#        print(self.key_up)
#        print(key)

def setup():
    global pl, sl
    size(1366,768)
#    pl=Player(600, 300, UP, DOWN, RIGHT, LEFT, 5)
#    pl=Player(600, 300, 'w', 's', 'd', 'a', 5)
    pl=Player(600, 300, 'i', 'k', 'l', 'j', 5)
    
def draw():
    global x,y,q,b1,b2,b3,d,f,t,b,x1,y1,v, pl, sl
#    print(q)
    background(b1,b2,b3)

    step=5
    if q==0:
        b1=28
        b2=250
        b3=0
        title = u"ЛЕС"
    if q==1:
        b1=133
        b2=133
        b3=133
        title = u"ГОРЫ"
        pl.y = pl.y+1
        sl.draw_()
        sl.fall_(1)
    if q==2:
        b1=170
        b2=27
        b3=154
        step=3
        title = u"БОЛОТО"
    if q==3:
        b1=133
        b2=133
        b3=133
        title = u"ПУСТОТА"
    if q==4:
        b1=133
        b2=133
        b3=133 
        title = u"ПУСТОТА"
#    rect(x,y,20,20)
#    fill(0)

    if q == 1:
        check = sl.check_(pl)
        if check == 0:
            q = 0
            pl.start_()
        

    if keyPressed:
#        if key == 'w':
#            pl.y = pl.y - step
#        if key == 'a':
#            pl.x = pl.x - step
#        if key == 's':
#            pl.y = pl.y + step
#        if key == 'd':
#            pl.x = pl.x + step

#        if keyCode == UP:
#            pl.y = pl.y - step
#        if keyCode == LEFT:
#            pl.x = pl.x - step
#        if keyCode == DOWN:
#            pl.y = pl.y + step
#        if keyCode == RIGHT:
#            pl.x = pl.x + step
        pl.control_(key)
    # смена уровней
    if pl.y<10 and q <4:
        q=q+1
        pl.y=700
        if q == 1:
             sl=StoneList()
    if pl.y>730 and q >0:
        q=q-1
        pl.y=30
        if q == 1:
             sl=StoneList()
    # ограничения по вертикали
    if pl.y < 10 and q == 4:
        pl.y = pl.y + 5

    if q==0 and pl.y > 730:
        pl.y = 730
    # ограничения по горизонтали
    if pl.x < 0:
        pl.x = 0
    if pl.x > 1350:
        pl.x = 1350

    # отрисовка монстра
    if q == 0 and v==0:
        push()
        rect(90,90,30,30)   #монстр
        fill(39,142,0)
        pop()
    if pl.x > 90 and pl.x < 120 and pl.y > 90 and pl.y < 120 and b==0:    #Монстр
        d=d+1 
    if pl.x>90 and pl.x < 120 and pl.y > 90 and pl.y < 120 and b==1 and key=="e":   #Монстр
        v=1    
    #if d ==4:
        #d=d-1
    frameRate(70)
    push()
    fill(255,0,60)    #здоровье
    rect(1000,650,f,20)
    pop()
    if d == 0:  
        f=250
    if d == 1:
        f=150
    if d == 2:
        f=100
    if d == 3:
        f=50
    if d == 4:
        f=0 
    if d > 4:
        pl.y=700
        pl.x=384
        q=0
        d=0
    if b==0 and q==0:
        rect(1000,50,10,30)
    if pl.x > 990 and pl.x < 1020 and pl.y > 50 and pl.y < 80 and key=="e":
        b=1
    #text(u"е - использовать",10,150)
    #textSize(20) 

        
    push()
    text(title,20,50)
    textSize(20) 
    pop()

#    if q == 1:
#        rect(0,450,500,20)
#        if x>0 and x<500 and y>450 and y<470:
#            y=700
#            x=384
#            q=0
#        rect(1000,350,500,20)
#        if x>1000 and x<1500 and y>350 and y<370:
#            y=700
#            x=384
#            q=0
    pl.draw_()
