-- 코드를 입력하세요
SELECT DISTINCT(CAR_ID), (CASE
WHEN CAR_ID IN (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
      WHERE END_DATE = '2022-10-16' or (START_DATE <='2022-10-16' AND END_DATE>='2022-10-16') OR
      START_DATE = '2022-10-16')
                THEN '대여중'
else '대여 가능'
END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER by CAR_ID DESC
