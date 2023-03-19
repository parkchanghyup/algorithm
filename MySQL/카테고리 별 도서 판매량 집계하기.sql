-- 코드를 입력하세요
select category, sum(sales) as total_sales
from Book_sales b2
join BOOK b1
on b2.BOOK_ID = b1.BOOK_ID
where b2.sales_date like '2022-01%'
group by category
order by category