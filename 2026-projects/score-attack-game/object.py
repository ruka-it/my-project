import random

class Player:
    def __init__(self):
        self.hp=120
        self.point=0
        
    def sleep(self):
        self.hp=min(self.hp+20, 120)
        print(f"HPが回復した!\nあなたのHPは{self.hp}になった!")
    def __str__(self):
        return f"<今>HP：{self.hp}  point：{self.point}"
        
        
class Monster:
    def __init__(self,attack):
        
        self.attack=attack
        
        
        
        
class Silme(Monster):
    pass

class N_Slime(Silme):
    def attack_slime(self,player): 
        print("ぷにぷに")
        hit_rate=55
        number=random.randint(1,100)
        if number<=hit_rate:
            print("攻撃が命中した！\nKNCスライムは亡くなった。")
            player.point+=120
            print("あなたは120ポイント獲得した")
               
        else:
            print("あなたの攻撃はミスした！\nKNCスライムの攻撃")
            attack_rate=70
            number=random.randint(1,100)
            if number<=attack_rate:
                print("KNCスライムの攻撃が命中した!")
                player.hp-=self.attack
                print(f"あなたに{self.attack}のダメージ!")
            else:
                print("KNCスライムの攻撃は当たらなかった")  


class KncSlime(Silme):
    def attack_Kslime(self,player): 
        print("KNCスライムと遭遇した。\nKNCスライム：ぷにぷに")
        hit_rate=55
        number=random.randint(1,100)
        if number<=hit_rate:
            print("攻撃が命中した！\nKNCスライムは亡くなった。")
            player.point+=200
            print("あなたは200ポイント獲得した")
               
        else:
            print("あなたの攻撃はミスした！\nKNCスライムの攻撃")
            attack_rate=70
            number=random.randint(1,100)
            if number<=attack_rate:
                print("KNCスライムの攻撃が命中した!")
                player.hp-=self.attack
                print(f"あなたに{self.attack}のダメージ!")
            else:
                print("KNCスライムの攻撃は当たらなかった")     
    
        
        
class PRabbit(Monster):
    def attack_PR(self, player):
        print("毒ウサギと遭遇した.\n毒ウサギ：ここは私たちの土地よ")
        hit_rate=55
        number=random.randint(1,100)
        if number<=hit_rate:
            print("攻撃が命中した！\n毒ウサギは亡くなった。")
            player.point+=150
            print("あなたは150ポイント獲得した")
            
        else:
            print("あなたの攻撃はミスした！\n毒ウサギの攻撃")
            attack_rate=70
            number=random.randint(1,100)
            if number<=attack_rate:
                print("毒ウサギの攻撃が命中した！")
                player.hp-=30
                print("あなたに30のダメージ!")
            else:
                print("毒ウサギの攻撃は当たらなかった")
            
class Hyouga(Monster):
    def attack_hyouga(self, player):
        print("氷河：..........")
        hit_rate=50
        number=random.randint(1,100)
        if number<=hit_rate:
            print("攻撃が命中した！\n氷河は水になった。")
            player.point+=1000
            print("あなたは1000ポイント獲得した")
            
        else:
            print("あなたの攻撃はミスした！\n氷河の攻撃")
            attack_rate=80
            number=random.randint(1,100)
            if number<=attack_rate:
                print("氷河の攻撃が命中した！")
                player.hp-=self.attack
                print(f"あなたに{self.attack}のダメージ!")
            else:
                print("氷河の攻撃は当たらなかった")
        
