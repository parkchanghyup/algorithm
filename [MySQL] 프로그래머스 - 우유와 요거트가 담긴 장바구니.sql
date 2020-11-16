-- 코드를 입력하세요
select cart_id
from cart_products
where cart_id in  (SELECT cart_id
                   from cart_products
                   where name = 'milk') and name =  'yogurt'
order by cart_id ;