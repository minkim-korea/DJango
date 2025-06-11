from django.db import models

# class Product(models.Model):
#    product_code = models.PositiveIntegerField(unique=True)  # 상품코드 (숫자)
#    name = models.CharField(max_length=200)  # 상품명 (문자)
    
#     top_category = models.CharField(max_length=100)  # 상위 카테고리 (문자)
#     sub_category = models.CharField(max_length=100)  # 하위 카테고리 (문자)

#     origin = models.CharField(max_length=100)  # 원산지 (문자)
#     weight = models.PositiveIntegerField(help_text="단위: g 또는 ml")  # 중량 (숫자)

#     price = models.PositiveIntegerField()  # 소비자가격 (숫자)
#     discount_price = models.PositiveIntegerField(null=True, blank=True)  # 할인가 (숫자)

#     stock = models.PositiveIntegerField()  # 재고 (숫자)

#     main_image = models.ImageField(upload_to='products/main/', null=True, blank=True)  # 메인이미지
#     sub_image1 = models.ImageField(upload_to='products/sub/', null=True, blank=True)  # 서브이미지
#     sub_image2 = models.ImageField(upload_to='products/sub/', null=True, blank=True)  # 서브이미지2

#     created_at = models.DateField(auto_now_add=True)  # 등록일자
#     updated_at = models.DateField(auto_now=True)      # 수정일자

#     status = models.CharField(max_length=20, choices=[
#         ('판매중', '판매중'),
#         ('품절', '품절'),
#         ('판매중지', '판매중지')
#     ])  # 판매여부 (문자)

#     priority = models.PositiveIntegerField(default=0, help_text="숫자가 클수록 상단에 노출됨")  # 상위노출 (숫자)

#     def __str__(self):
#         return f"{self.name} ({self.product_code})"