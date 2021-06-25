# 우리를 위한 프로그래밍: 파이썬 중급
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩

# 차량 1
car_company_1 = "Ferrari"
car_detail_1 = [{"color": "White", "horsepower": 400}, {"price": 8000}]

# 차량 2
car_company_2 = "Bmw"
car_detail_2 = [{"color": "Black"}, {"horsepower": 270}, {"price": 5000}]

# 차량 3
car_company_3 = "Audi"
car_detail_3 = [{"color": "Silver"}, {"horsepower": 300}, {"price": 6000}]

# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 할 수 있음. 삭제 불편함.
car_company_list = ["Ferrari", "Bmw", "Audi"]
car_detail_list = [
    {"color": "White", "horsepower": 400, "price": 8000},
    {"color": "Black", "horsepower": 270, "price": 5000},
    {"color": "Silver", "horsepower": 300, "price": 6000},
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)


print("\n\n")

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키는 중복을 허용하지 않음) 있을 수 있음, 정렬 문제가 있을 수 있음.
# 키 조회 예외 처리 등

car_dicts = [
    {
        "car_company": "Ferrari",
        "car_detail": {"color": "White", "horsepower": 400, "price": 8000},
    },
    {
        "car_company": "Bmw",
        "car_detail": {"color": "Black", "horsepower": 270, "price": 5000},
    },
    {
        "car_company": "Audi",
        "car_detail": {"color": "Silver", "horsepower": 300, "price": 6000},
    },
]

# key로 값을 지울 때, pop(key, 'default')
del car_dicts[1]
print(car_dicts)

print("\n\n")

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드를 활용
class Car(object):
    def __init__(self, company, details):
        self._company = company
        self._details = details


car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
print(car1)  # <__main__.Car object at 0x0000020323B30FD0>


class Car(object):
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # Magic Method, 파이썬에서 만들어놓은 함수를 활용하면
    # 클래스의 디테일한 정보를 출력할 수 있음.
    # REF에서 사용자 입장의 출력을 원할 땐, 이 함수를 사용
    def __str__(self):
        return "str: {} - {}".format(self._company, self._details)

    # __str__과 비슷한 역할, 개발자용
    # 객체, 자료형의 타입에 따른 출력을 원할 땐, 이 함수를 사용
    def __repr__(self):
        return "repr: {} - {}".format(self._company, self._details)


car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})
# __str__이 있으면, str을 출력하고, 없으면 __repr__를 출력함
print(car1)  # str: Ferrari - {'color': 'White', 'horsepower': 400, 'price': 8000}
print(car2)
print(car3)
# 안의 속성 정보를 볼 수 있음.
print(
    car1.__dict__
)  # {'_company': 'Ferrari', '_details': {'color': 'White', 'horsepower': 400, 'price': 8000}}
print(car2.__dict__)
print(car3.__dict__)
# dir을 사용하면 안의 모든 메타 정보가 보여짐
print(
    dir(car1)
)  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_company', '_details']

print("\n\n")

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 이렇게 할 땐, repr가 출력.
print(
    car_list
)  # [repr: Ferrari - {'color': 'White', 'horsepower': 400, 'price': 8000}, repr: Bmw - {'color': 'Black', 'horsepower': 270, 'price': 5000}, repr: Audi - {'color': 'Silver', 'horsepower': 300, 'price': 6000}]

# 반복문에서는 str 출력
for x in car_list:
    # 명시적으로 repr를 사용하면 repr를 출력함
    # print(repr(x))
    print(x)
