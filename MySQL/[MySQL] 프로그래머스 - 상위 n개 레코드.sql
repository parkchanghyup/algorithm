SELECT name
from animal_ins
where datetime = (select min(datetime)
                  from animal_ins)