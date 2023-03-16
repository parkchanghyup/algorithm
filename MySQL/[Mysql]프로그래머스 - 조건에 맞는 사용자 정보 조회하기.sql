-- 코드를 입력하세요
SELECT T1.USER_ID, T1.NICKNAME, TOTAL_SALES as TOTAL_SALES
from USED_GOODS_USER T1
join  (select writer_id, sum(PRICE) as TOTAL_SALES
       from used_goods_board 
       where STATUS = 'DONE'
      group by WRITER_ID
        having sum(PRICE) >= 700000) T2
on T2.WRITER_ID = T1.USER_ID
order by total_sales
