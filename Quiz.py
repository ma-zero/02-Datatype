# Quiz 1. 회원가입 폼, 이름, 나이, 이메일 주소, 연락처, 딕셔너리 타입, 2사람 데이터 입력

name_1 = input("이름을 입력하세요. : ")
age_1 = input("나이를 입력하세요. : ")
email_1 = input("이메일을 입력하세요. : ")
phone_1 = input("연락처를 입력하세요. : ")

dic_1 = {name_1 : {"나이" : age_1, '이메일' : email_1, '연락처' : phone_1}}
print(dic_1[name_1]["이메일"])

name_2 = input("이름을 입력하세요. : ")
age_2 = input("나이를 입력하세요. : ")
email_2 = input("이메일을 입력하세요. : ")
phone_2 = input("연락처를 입력하세요. : ")

dic_2 = {name_2 : {"나이" : age_2, '이메일' : email_2, '연락처' : phone_2}}
print(dic_2[name_2]["나이"])



# Quiz 2. 환율, 표에 따라 원화가치 계산시 한화로 얼마 가지고 있는가?

money = [13, 200, 13]
dic_2 = {"달러" : 1320, "엔" : 950, "위안" : 182}
X = [dic_2["달러"] * money[0] + dic_2["엔"] * money[1] + dic_2["위안"] * money[2]]

print("철수가 가지고 있는 돈의 원화 가치는 ", X[0] , "원 입니다.")