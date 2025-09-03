use chargerdb;

select * from tbl_charger;

select city_code, count(*) as charger_count from tbl_charger
group by city_code; 

create table tbl_charger_sum as
select city_code, count(*) as charger_count from tbl_charger
group by city_code; 

select * from tbl_charger_sum;



