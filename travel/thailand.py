class ThailandPackage:
  def detail(self):
    print("여행 50만원")

if __name__ == "__main__":
  print("thailand")
  print("모듈을 실행할 때만 실행")
  trip_to = ThailandPackage()
  trip_to.detail()
else:
  print("외부에서 호출")
