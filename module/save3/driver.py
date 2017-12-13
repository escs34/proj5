######################################################################
#작성일: 11/1
#마지막 변경일: 11/1
#작성자: 20132885 손태선
#기능: 차를 운전함. 실행파일
#입력: 좌회전 또는 우회전 키보드 입력
#출력: car module로 방향, 속도 출력
######################################################################
'''운전자가 휠을 돌리고 엑셀을 밟는 것 처럼 차에 신호를 보냅니다.
이렇게 car와 driver를 나누면 이후 추가될 다른 요구에도 driver의
행동만 바꾸면 되니 car 모듈을 수정할 필요가 없습니다.

예시 코드와의 차이점
1.자동차에서 해결해야 할 일부 기능을 여기서 해결하던 점 수정 (GPIO.setwarnings(false))
2.주행환경이 바뀔때 마다 출력의 세부수치를 바꿔줘야 하기 때문에
자주 수정할 수 있는 여기서 차량의 전후진, 회전을 결정

'''

import car
import trackingModule
import time

def decision():#여기서 회전안해도되 판정 나올때 까지 회전 하고  풀어줌
	pass


def turn(count):
	direction=False
	if count==1:#우회전
		direction=True
	elif count==0:
		return 0
	time.sleep(0.5)

	car.engine(direction, not direction, 36, 39)
	time.sleep(0.3)
	while not (trackingModule.navigator()&4):
		car.engine(direction, not direction, 36, 39)
		time.sleep(0.001)
	car.engine(True, True, 0, 0)
	time.sleep(0.3)

	while not (trackingModule.navigator()&4):
		car.engine(not direction, direction, 36, 39)
		time.sleep(0.0001)
	car.engine(True,True,0,0)
	time.sleep(0.3)

def lineTracking():
	print("자동주행을 시작합니다.")
	#전진후 좌우 교정과 판단을 동시에

	while True:
		count=0
		turn_finish=False
		car.engine(True, True, 42, 42)
		time.sleep(0.001)

		bit=2	

		while True:
			bit=trackingModule.bitCount()
			if bit>2 or bit==0:
				while True:
					if bit==1 or bit==0:
						break
					bit=trackingModule.bitCount()
				break
			li = trackingModule.li[len(trackingModule.li)-1]

			if li[2]==False:
				car.engine(True,True,0,0)
				time.sleep(0.05)
				if li[1]==True:
					while trackingModule.bit4()!=True:
						car.engine(False, True, 35, 35)
						time.sleep(0.001)
						if trackingModule.bitCount()==0:
							break
				else:
					while trackingModule.bit4()!=True:
						car.engine(True, False, 35, 35)
						time.sleep(0.001)
						if trackingModule.bitCount()==0:
							break
				car.engine(True, True, 0,0)
				time.sleep(0.05)
				car.engine(True, True, 42, 42)
		print(bit, "cdcd")

		#decision
		count=trackingModule.where_to_go()
		print(count)

		for a in reversed(trackingModule.li):
			print(a)
		print()

		turn(count)
		
		trackingModule.li_clear()


	print("자동주행을 마칩니다.")


if __name__ == "__main__":
	try:
		#차 시동을 건다.
		car.startUp()

		lineTracking()
				
		#차 시동을 끈다.
		car.turnOff()
	#ctrl + c 키로 종료한 경우
	except KeyboardInterrupt:
		print("강제종료 하셨습니다.")
	#오류로 인한 종료 시 시동끄기 함수 호출. 없다면 오류로 프로그램이 종료된 이후에도 바퀴가 돌 수 있다.
	finally:
		car.turnOff()


