create user 'root'@'%' identified by '0912';

create database chargerdb;
grant all privileges on chargerdb.* to root@'%';

show databases;
show grants for root@'%';

use chargerdb;

drop table tbl_charger;

create table tbl_charger
(
	charger_code int auto_increment primary key,
	city_code int,
	company varchar(50),
	charger_name varchar(100),
	charger_type varchar(2),
    facility_type varchar(2),
	lat float,
    lng float
) engine=innodb;

select * from tbl_charger;