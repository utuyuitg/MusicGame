

import os
import time
import shelve
import shutil

music = []


def mus():
	ver = 'v0.3.0 beta'
	return ver


if not os.path.exists('arcaea'):
	os.makedirs('arcaea')
mg = shelve.open('arcaea/music_game')


try:
	music.extend(mg['arc'])
except Exception:
	pass
	


def game_help():
        print("arcaea 輸入arc的遊玩記錄")
        print("read   讀取遊玩記錄")
        print("pure   統計pure總數")
        print("far    統計far總數")
        print("lost   統計lost總數")
        print("del    刪除遊玩記錄")
        input()


def arcaea():
	name = input("標題:")
	way = input("方法:")
	py = input("偏移率:")
	speed = input("速度:")
	level = input("難度:")
	track = input("通關狀態:")
	mr = input("MAX RECALL:")
	pure = int(input("PURE:"))
	late = int(input("LATE:"))
	early = int(input("EARLY:"))
	lp = int(input("LATE PURE:"))
	ep = int(input("EARLY PURE:"))
	lost = int(input("LOST:"))
	far = late + early
	score = int((pure + far / 2) / (pure + far + lost) * 10000000 + pure - lp - ep)
	if score > 9900000:
		exx = 'EX+'
	else:
		if score > 9800000:
			exx = 'EX'
		else:
			if score > 9500000:
				exx = 'AA'
			else:
				if score > 9200000:
					exx = 'A'
				else:
					if score > 8900000:
						exx = 'B'
					else:
						if score > 8600000:
							exx = 'C'
						else:
							exx = 'D'
	arc = {'標題':name,
	'日期':time.strftime('%Y/%m/%d'),
	'時間':time.strftime('%X'),
	'方法':way,
	'偏移率':py,
	'速度':speed,
	'難度':level,
	'評級':exx,
	'評分':score,
	'通關狀態':track,
	'MAX RECALL':mr,
	'PURE':pure,
	'FAR':far,
	'LOST':lost,
	'LATE':late,
	'EARLY':early,
	'LATE PURE':lp,
	'EARLY PURE':ep}
	music.append(arc)
	mg['arc'] = music
	

def read():
        if note == 'help':
              game_help()
        if note == 'arcaea':
                arcaea()
        elif note == 'del':
                shutil.rmtree('arcaea')
                exit()
        elif note == 'read' or note == 'pure' or note == 'far' or read == 'lost':
                try:
                        pu = 0
                        fa = 0
                        lo = 0
                        for x in mg['arc']:
                                for y,z in x.items():
                                        if note == 'read':
                                                if y == '標題':
                                                        y_name = y
                                                        z_name = z
                                                if y == '日期':
                                                        y_date = y
                                                        z_date = z
                                                if y == '時間':
                                                        y_time = y
                                                        z_time = z
                                                if y == '方法':
                                                        y_way = y
                                                        z_way = z
                                                if y == '偏移率':
                                                        y_py = y
                                                        z_py = z
                                                if y == '速度':
                                                        y_speed = y
                                                        z_speed = z
                                                if y == '難度':
                                                        y_level = y
                                                        z_level = z
                                                if y == '評級':
                                                        y_exx = y
                                                        z_exx = z
                                                if y == '評分':
                                                        y_score = y
                                                        z_score = z
                                                if y == '通關狀態':
                                                        y_track = y
                                                        z_track = z
                                                if y == 'MAX RECALL':
                                                        y_mr = y
                                                        z_mr = z
                                                if y == 'PURE':
                                                        y_pure = y
                                                        z_pure = z
                                                if y == 'FAR':
                                                        y_far = y
                                                        z_far = z
                                                if y == 'LOST':
                                                        y_lost = y
                                                        z_lost = z
                                                if y == 'LATE':
                                                        y_late = y
                                                        z_late = z
                                                if y == 'EARLY':
                                                        y_early = y
                                                        z_early = z
                                                if y == 'LATE PURE':
                                                        y_lp = y
                                                        z_lp = z
                                                if y == 'EARLY PURE':
                                                        y_ep = y
                                                        z_ep = z
                                        elif note == 'pure':
                                                if y == 'PURE':
                                                        pu += z
                                        elif note == 'far':
                                                if y == 'FAR':
                                                        fa += z
                                        elif note == 'lost':
                                                if y == 'LOST':
                                                        lo += z
                                if note == 'read':
                                        print(y_name,z_name)
                                        print(y_date,z_date)
                                        print(y_time,z_time)
                                        print(y_way,z_way)
                                        print(y_py,z_py)
                                        print(y_speed,z_speed)
                                        print(y_level,z_level)
                                        print(y_exx,z_exx)
                                        print(y_score,z_score)
                                        print(y_track,z_track)
                                        print(y_mr,z_mr)
                                        print(y_pure,z_pure)
                                        print(y_far,z_far)
                                        print(y_lost,z_lost)
                                        print(y_late,z_late)
                                        print(y_early,z_early)
                                        print(y_lp,z_lp)
                                        print(y_ep,z_ep)
                                        input()
                        if note == 'pure':
                                print(pu)
                                input()
                        if note == 'far':
                                print(fa)
                                input()
                        if note == 'lost':
                                print(lo)
                                input()
                except Exception:
                        print('暫無遊玩記錄')
                        input()


while True:
	print("Music Game")
	print(mus())
	note = input('>>>')
	read()
	os.system('cls')

