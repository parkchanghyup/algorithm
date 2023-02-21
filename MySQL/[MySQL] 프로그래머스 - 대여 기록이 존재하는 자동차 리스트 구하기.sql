SELECT DISTINCT t1.CAR_ID
from CAR_RENTAL_COMPANY_CAR t1
left join CAR_RENTAL_COMPANY_RENTAL_HISTORY t2
on t1.CAR_ID = t2.CAR_ID
where t1.CAR_TYPE = '세단' 
and month(t2.start_date) = 10
order by t1.car_id desc