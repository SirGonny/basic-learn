# # from random import *

# # # 일반 유닛
# # class Unit:
# #   def __init__(self, name, hp, speed):
# #       self.name = name
# #       self.hp = hp
# #       self.speed = speed
# #       print("{0} 유닛 생성".format(name))

# #   def move(self, location):
# #     print("{0}: {1}방향 이동. 속도{2}".format(self.name, location, self.speed))

# #   def damaged(self, damage):
# #     print("{0}: {1} 데미지 받음".format(self.name, damage))
# #     self.hp -= damage
# #     print("{0}: 현재 체력 {1}".format(self.name, self.hp))
# #     if self.hp <= 0 :
# #       print("{0}: 파괴됨".format(self.name))

# # # 공격 유닛    
# # class AttackUnit(Unit):
# #   def __init__(self, name, hp, speed, damage):
# #     Unit.__init__(self, name, hp, speed)
# #     self.damage = damage

# #   def attack(self, location):
# #     print("{0}: {1}방향으로 공격. 공격력{2}".format(self.name, location, self.damage))
  
# # class Marine(AttackUnit):
# #   def __init__(self):
# #     AttackUnit.__init__(self, "마린", 40, 1, 5)
# #   def stimpack(self):
# #     if self.hp > 10:
# #       self.hp -= 10
# #       print("{0}: 스팀팩 사용".format(self.name))
# #     else:
# #       print("{0}: 체력이 부족".format(self.name))

# # class Tank(AttackUnit):
# #   seize_developed = False

# #   def __init__(self):
# #     AttackUnit.__init__(self, "탱크", 150, 1, 40)
# #     self.seize_mode = False
# #   def set_seize_mode(self):
# #     if Tank.seize_developed == False:
# #       return
    
# #     #시즈모드가 아닐 때
# #     if self.seize_mode == False:
# #       print("{0} : 시즈모드로 전환".format(self.name))
# #       self.damage = 70
# #       self.seize_mode = True
# #     else:
# #       print("{0} : 시즈모드로 해제".format(self.name))
# #       self.damage = 40
# #       self.seize_mode = False
# #     #시즈모드 일 떄  

# # #공중유닛 
# # class Flyable:
# #   def __init__(self, flying_speed):
# #     self.flying_speed = flying_speed
  
# #   def fly(self, name, location):
# #     print("{0}: {1} 방향 날아서 이동. 속도{2}".format(name, location, self.flying_speed))

# # class FlyableAttack(AttackUnit, Flyable):
# #   def __init__(self, name, hp, damage, flying_speed):
# #     AttackUnit.__init__(self, name, hp, 0, damage)
# #     Flyable.__init__(self, flying_speed)

# #   def move(self, location):
# #     self.fly(self.name, location)

# # class Wraith(FlyableAttack):
# #   def __init__(self):
# #     FlyableAttack.__init__(self, "레이스", 80, 8, 5)
# #     self.clocked = False
  
# #   def clocking(self):
# #     if self.clocked == True:
# #       print("{0} : 클로킹 모드 해제".format(self.name)) 
# #       self.clocked = False
# #     else:
# #       print("{0} : 클로킹 모드 설정".format(self.name))
# #       self.clocked = True

# # def game_start():
# #   print("[알림] 새로운 게임을 시작합니다.")

# # def game_over():
# #   print("GAME OVER")

# # #게임 시작
# # game_start()

# # m1 = Marine()
# # m2 = Marine()
# # m3 = Marine()

# # t1 = Tank()
# # t2 = Tank()

# # w1 = Wraith()

# # attack_units = []
# # attack_units.append(m1)
# # attack_units.append(m2)
# # attack_units.append(m3)
# # attack_units.append(t1)
# # attack_units.append(t2)
# # attack_units.append(w1)

# # #부대 이동
# # for unit in attack_units:
# #   unit.move("1시")

# # Tank.seize_developed = True
# # print("[알림] 시즈모드 개발이 완료됨")

# # #부대 특수능력 사용
# # for unit in attack_units:
# #   if isinstance(unit, Marine):
# #     unit.stimpack()
# #   elif isinstance(unit, Tank):
# #     unit.set_seize_mode()
# #   elif isinstance(unit, Wraith):
# #     unit.clocking()

# # #부대 공격
# # for unit in attack_units:
# #   unit.attack("1시") 

# # #부대 피해
# # for unit in attack_units:
# #   unit.damaged(randint(5, 31))

# # #게임종료
# # game_over()

# # import travel.thailand as th
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))