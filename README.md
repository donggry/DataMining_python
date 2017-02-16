#DataMining_python

    데이터 분석을 위한 파이썬 프로그래밍과 수학 통계 기초 예제 공부
    책: 밑바닥부터 시작하는 데이터 과학 실습
    기간 : 3월말까지 공부!
## ***Wiki 에 개념정리 및 파이썬 팁들을 정리!

# 1장의 개념
        데이터 과학이란?.....
# Python Tip
 *  for문을 일렬로 나열하고 if를 넣어서 한 줄에 리스트를 만드는 경우 
 *  all() 함수는 ()안에 있는 값들이 모두 참이여만 true 반환 ,(any는 하나라도 참이면 참)
    
        list1=['a','b','c','d']
        list2=[1,2,3,4,5]
        print all((a,b) for a in list1 for b in list2 if  a=='a' and b != 3)
         >> True ([('a', 1), ('a', 2), ('a', 4), ('a', 5)] all 대신 []으로 감쌌을 경우 결과 값)
    

 * Counter()는 ()안에 있는 원소들의 중복 갯수를 세어 딕셔너리 형태로 반환 

        from collections import Counter
        dic={'aa':[1,2,1,1,4],"bb":[2,1,1,1,1,6,6,6,32]}
        print Counter(dic['aa'])
        >> Counter({1: 3, 2: 1, 4: 1})
 * 축약함수 (Lambda) 
    * lambda 인자 : 표현식

            (lambda x,y: x + y)(10, 20)
            >>>30
    * reduce(함수, 순서형 자료)-순서형 자료(문자열, 리스트, 튜플)의 원소들을 누적적으로 함수에 적용

            reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
            >>>10
            (lambda x, y,z,k: x + y+z+k)(1, 2, 3, 4)
            >>>10
    * map(함수, 리스트)-  리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음, 그 결과를 새로운 리스트로 반환 

            map(lambda x: x ** 2, range(5))
            >>>[0,1,4,9,16]
    * filter(함수, 리스트) - 리스트에 들어있는 원소들을 함수에 적용시켜서 결과가 참인 값들로 새로운 리스트를 반환

            filter(lambda x: x < 5, range(10))    
            >>>[0, 1, 2, 3, 4]  
 * sorted() 다양한 조건으로 정렬하기
    * sorted(정렬할 리스트 혹은 투플 등,key=lambda(정렬할 대상의 형식들 정의)

        `:정렬할 key,reverse=True(내림차순,(오름차순은 False)`
 * defaultdict()
    
        dictionary 에 기본값을 정의하고 키값이 없더라도 에러를 출력하지않고 기본값을 출력
        dict.set_default를 사용하는것보다 빠른것이 장점
        from collections import defaultdict 
        d = defaultdict(object(list,,,등) # Default dictionary를 생성
        d = defaultdict(lambda: 0) # Default 값을 0으로 설정
        key 값이 존재하지 않아도 에러가 나지 않고 0을 반환