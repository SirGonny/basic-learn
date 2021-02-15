# 클래스 테스트

# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
  #매물 초기화
  def __init__(self, location, house_type, deal_type, price, completion_year):
    self.location = location
    self.house_type = house_type
    self.deal_type = deal_type
    self.price = price
    self.completion_year = completion_year

  #매물 정보 표시
  def show_detail(self):
    print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []

h1= House("강남", "아파트", "매매", "10억", "2010년")
h2= House("마포", "오피스텔", "전세", "5억", "2007년")
h3= House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(h1)
houses.append(h2)
houses.append(h3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))

# for house in houses:
#   house.show_detail()

# 예외 테스트

# 1보다 작거나 숫자가 아닌 입력값이 들어올 때 ValueError 처리
# "잘못된 값을 입력했습니다."
# 치킨 소진시 SoldOutError 발생
# "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldOutError(Exception):
  pass

chicken = 10
waiting = 1

while(True):
  try:
    print("[남은 치킨 : {0}]".format(chicken))
    order = int(input("치킨 몇마리를 주문하시겠습니까?"))
    if order > chicken:
      print("재료가 부족합니다.")
    elif order < 1:
      raise ValueError
    else:
      print("[대기번호 {0}] {1}".format(waiting, order))
      waiting += 1
      chicken -= order

    if chicken == 0:
      raise SoldOutError
  except ValueError:
    print("잘못된 값을 입력했습니다.")
  except SoldOutError:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    break