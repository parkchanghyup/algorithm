SELECT NAME,count(name) as COUNT
from animal_ins
group by name
having count(name)>1
order by name