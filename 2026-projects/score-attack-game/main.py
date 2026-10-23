from object import Player, N_Slime, PRabbit, KncSlime, Hyouga
import random
import sqlite3
import csv

con = sqlite3.connect('ranking.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS ranking
    (name TEXT, point INTEGER)""")
con.commit()

name=input("あなたの名前を教えてください>>")
player=Player() #Playerclassなのでhp/pointは120/0からスタート
n=0 #これは回数計算に利用します。

while n<=14:
    
    try:
        menu = int(input("何をしますか？\n1:バトルに行く 2:休憩する(HP:20回復) 3:スキップ 4:ランキングを見る 9:ゲーム終了>>"))
    
    except ValueError:
        print("エラー！あなたはバトルに行かされる！")

    if menu==1:
        
        dungeon=int(input("どこのダンジョンに行く？\n1:ヤバ谷 2:白銀の氷河>>"))
        if dungeon==1:
            print("あなたはヤバ谷に行った。")
            number=random.randint(1,100)
            if number<=70:
                nslime=N_Slime(10)
                nslime.attack_slime(player)
            elif number<=90:
                Prabbit=PRabbit(30)
                Prabbit.attack_PR(player)
            else:
                KNCslime=KncSlime(60)
                KNCslime.attack_Kslime(player)
        if dungeon==2:
            print("あなたは白銀の氷河に行った")
            number=random.randint(1,100)
            if number<=50:
               Prabbit=PRabbit(30)
               Prabbit.attack_PR(player)
            elif number<=90:
                KNCslime=KncSlime(50)
                KNCslime.attack_Kslime(player)
                
            else:
                hyouga=Hyouga(80)
                hyouga.attack_hyouga(player)
    if player.hp==0:
        print("GAMEOVER")
        break
             
            

    if menu==2:
        print("あなたは眠った")
        player.sleep()
        
    if menu==3:
        print("あなたは行動をスキップした")
        
    if menu==4:
        print("ランキングは以下の通りです。")
        cur.execute("""SELECT name, point,
            RANK() OVER(ORDER BY point DESC) AS rank
                FROM ranking""")
        ranking=cur.fetchall()
        for data in ranking:
            print(f"{data[2]}位：{data[0]}さん   {data[1]}ポイント")
            
        
        
        
    if menu==9:
        print("プレイを中止します。")
        cur.execute("""INSERT INTO ranking (name, point)
            VALUES(?, ?)""", (name, player.point))
        con.commit()
        print("お疲れさまでした。")
        break
    
    print(player)
    n+=1 #最後に1を足して回数を上げる
    print(f"現在のターン：{n}/15")
    

print(f"あなたのポイントは{player.point}です。")
cur.execute("""INSERT INTO ranking (name, point)
            VALUES(?, ?)""", (name, player.point))
con.commit()



#txt/csvゾーン    
cur.execute("""SELECT name, point,
            RANK() OVER(ORDER BY point DESC) AS rank
                FROM ranking""")
ranking=cur.fetchall()    
    
with open('BattleResult.txt','a', encoding='utf-8') as f:
    f.write(f"{name}は{player.point}ポイント獲得しました。")#txtファイル
    
with open("BattleResult.csv", "a", encoding="utf-8", newline="") as file:
    csv.writer(file).writerow([name, player.point])#csv
    
con.close()
