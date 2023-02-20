SELECT CAR_TYPE, count(*) as CARS
from car_rental_company_car
where OPTIONS like '%시트%'
group by car_type
order by car_type 

