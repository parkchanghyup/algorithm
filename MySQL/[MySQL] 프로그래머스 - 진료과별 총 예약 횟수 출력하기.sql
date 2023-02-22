SELECT MCDP_CD as '진료과목코드', count(MCDP_CD) as '5월예약건수'
from APPOINTMENT 
where APNT_YMD LIKE '2022-05%'
group by MCDP_CD
order by  count(mcdp_cd) , mcdp_cd
