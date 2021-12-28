SELECT hour(datetime) as hour,count(datetime) as count
from animal_outs
where hour(datetime ) between 9 and 20
group by hour(datetime)
order by hour(datetime)
