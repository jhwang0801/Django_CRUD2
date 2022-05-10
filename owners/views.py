from ast import comprehension
import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog


class OwnersView(View): 
# """
# 목적: Client가 보내주는 owner정보(name, age, email) 등록 요청에 맞게 owner테이블 in database 에 저장

# Input: 
#     {
# 'name'  = '홍길동'
# 'age'   = 20
# 'email' = asd@gmail.com
#     }

# Logic: 
#     1. owner 모델을 사용해서 owner 테이블에 데이터 입력
#     2. Owner.objects.create(...)

# Output: 
#     {
# "message": "SUCCESS"
#     }, status = 201

# """
    def post(self, request): 
        data = json.loads(request.body)

        Owner.objects.create(
            name  = data['name'],
            age   = data['age'],
            email = data['email']
        )
        return JsonResponse({"message" : "SUCCESS"}, status = 201)


# """
# 목적: owners의 정보를 client 요청하는 바와 맞게 database에서 호출하고, 가공해서 응답(반환)

# Logic: 
# 1. 응답해야할 방식에 맞춰주기 위해서 빈 리스트 생성 / results = []

# 2. 모든 owner의 정보 추출 / owners = Owner.Objects.all()

#     3. for loop으로 강아지 리스트(name , age 포함되도록)가 함께 응답될 수 있도록 짜야함
        

# Output: 
#     {
# "results" = result
# },         status = 200

# """

# list comprehension
# dict comprehension

    def get(self, request): 

        # 신버전 ver3
        results = [
            {
                    'name' : owner.name,
                    'age'  : owner.age,
                    'email': owner.email,
                    'dogs' : [{
                        'name': dog.name,
                        'age' : dog.age,
                    } for dog in owner.dog_set.all()]             
            } for owner in Owner.objects.all()
        ]


        # # 구버전 ver 2
        # results = []
        # owners  = Owner.objects.all()

        # for owner in owners: 
        #     results.append(
        #         {
        #             'name' : owner.name,
        #             'age'  : owner.age,
        #             'email': owner.email,
        #             'dogs' : [{
        #                 'name': dog.name,
        #                 'age' : dog.age,
        #             } for dog in owner.dog_set.all()]
        #         }
        #     )




        # # 구버전 ver 1
        # for owner in owners: 
        #     dogs = list(Dog.objects.filter(owner=owner.id).values('name', 'age'))
        #     results.append(
        #         {
        #             'name' : owner.name,
        #             'age'  : owner.age,
        #             'email': owner.email,
        #             'dogs' : dogs,
        #         }
        #     )


        return JsonResponse({'results' : results}, status = 200)







class DogsView(View): 

# """
# 목적: Client가 보내주는 dog정보(name, age, owner_id) 등록 요청에 맞게 dog테이블 in database 에 저장

# Input: 
#     {
# 'name'  = '라온'
# 'age'   = 1
# 'owner' = '홍길동'
#     }

# Logic: 
#     1. dog 모델을 사용해서 dog 테이블에 데이터 입력
#     2. Dog.objects.create()

# Output: 
#     {
# "message": "SUCCESS"
#     }, status = 201

# """

    def post(self, request): 
        data = json.loads(request.body)

        owner = Owner.objects.get(name=data['owner'])

        Dog.objects.create(
            name     = data['name'],
            age      = data['age'],
            owner_id = owner.id
        )
        return JsonResponse({"message" : "SUCCESS"}, status = 201)


# """
# 목적: dogs의 정보를 client 요청하는 바와 맞게 database에서 호출하고, 가공해서 응답(반환)

# Logic: 
# 1. 응답해야할 방식에 맞춰주기 위해서 빈 리스트 생성 / results = []

# 2. 모든 dog의 정보 추출 / dogs = Dog.Objects.all()
        

# Output: 
#     {
# "results" = result
# },         status = 200

# """

    def get(self, request): 
        results = []
        dogs    = Dog.objects.all()
        
        for dog in dogs: 
            results.append(
                {
                    'name' : dog.name,
                    'age'  : dog.age,
                    'owner': dog.owner.name
                }
            )
        return JsonResponse({"results" : results}, status=200)