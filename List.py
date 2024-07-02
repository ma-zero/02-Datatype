mazero = ["임하영", "26", "010-6213-****"]
name = mazero[0]
age = mazero[1]
phone = mazero[2]

print(type(mazero))
print(mazero[0])
print(name, age, phone)

names = [["임하영", "이승연", "정세림"], ["26", "26", "25"], ["010-6213-****", "010-****-****", "010-****-****"]]
print(names[1][2])
## 위 내용 (names[1][2]) 같은 경우 1번째 그룹(나이)에 2번째 데이터를 추출하는 것임.
## 숫자 인덱싱은 1이 아니라 0부터!

numbers = [1,2,3,4,5]
result = numbers[2] + numbers[-1]
print(result)

print(len(names))
print(len(names[0]))
## 요소의 갯수로 표시됨. names는 3개, numbers는 5개
## 20줄의 len은 names의 0번째의 갯수. 즉, 이름 3개


## 리스트에 요소 추가 및 제거하기
last = [1,2,3]
last.append(30)
print(last)
## 27줄 함수는 리스트 변수에 추가 하는것임. 즉 last의 1,2,3에 30을 추가하는 함수.
last.remove(3)
print(last)
## 30줄 함수는 리스트 변수에 제거 하는것임. 즉 last의 1,2,3에 3을 제거하는 함수.
