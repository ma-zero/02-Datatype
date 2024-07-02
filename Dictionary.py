dic = {"임하영" : 25 , "마지로" : 26 }
print(dic["마지로"])

## 딕셔너리 데이터 업데이트
dic["임하영"] = 27
dic["마지로"] = 36
print(dic["마지로"])
## 5,6줄 작성 시 기존에 있던 딕셔너리 데이터를 업데이트 함.


dic_1 = {"임하영" : [25, 163, "010-6213-****"], "마지로" : [26, 168, "010-1234-5678"]}
print(dic_1["임하영"][1])
## 12줄 "임하영"에 대한 "1"번째 데이터 추출.


dic_2 = {"임하영" : {"나이" : 25, "키" : 163, "연락처" : "010-6213-****"},
         "마지로" : {"나이" : 26, "키" : 168, "연락처" : "010-1234-5678"}}
print(dic_2["임하영"]["연락처"])
## 16줄 ["임하영"]으로 하면 임하영에 대한 전체 나옴. 뒤에 ["나이"] or ["키"] or ["연락처"] 등을 쓰면 그것에 대한 정보.
## 출력시 중괄호가 나오면 거기서 더 데이터를 뽑을 수 있음.