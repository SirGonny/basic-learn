class BigNumError(Exception):
  def __init__(self, msg):
    self.msg = msg
  def __str__(self):
    return self.msg

try:
  print("한 자리 숫자 나누기 전용 계산기")
  num1 = int(input("첫번째 숫자 입력하세요"))
  num2 = int(input("두번째 숫자 입력하세요"))
  if num1 >= 10 or num2 >= 10:
    raise BigNumError("입력값:{0}, {1}".format(num1, num2))
  print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
  print("에러!! 잘못입력했어요 한자리만 입력하세요")
except BigNumError as err:
  print("에러 발생..")
  print(err)
except Exception as err:
  print("에러를 알수 없음")
  print(err)
finally:
  print("계산기 종료")
