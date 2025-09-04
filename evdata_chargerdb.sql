use cardb;

create table if not exists ev_data(
city_code int,
city_name varchar(50) not null,
ev_sum int not null
) ENGINE=INNODB;

select * from ev_data;

update ev_data set city_code = 11
where city_name  like '서울%';
update ev_data set city_code = 26
where city_name  like '부산%';
update ev_data set city_code = 27
where city_name  like '대구%';
update ev_data set city_code = 28
where city_name  like '인천%';
update ev_data set city_code = 29
where city_name  like '광주%';
update ev_data set city_code = 30
where city_name  like '대전%';
update ev_data set city_code = 31
where city_name  like '울산%';
update ev_data set city_code = 36
where city_name  like '세종%';
update ev_data set city_code = 41
where city_name  like '경기%';
update ev_data set city_code = 43
where city_name  like '충북%';
update ev_data set city_code = 44
where city_name  like '충남%';
update ev_data set city_code = 46
where city_name  like '전남%';
update ev_data set city_code = 47
where city_name  like '경북%';
update ev_data set city_code = 48
where city_name  like '경남%';
update ev_data set city_code = 50
where city_name  like '제주%';
update ev_data set city_code = 51
where city_name  like '강원%';
update ev_data set city_code = 52
where city_name  like '전북%';
update ev_data set city_code = 47
where city_name  like '경상북도%';

select city_code from ev_data
where city_code = null;

update ev_data set city_name = '서울특별시'
where city_code = 11;
update ev_data set city_name = '부산광역시'
where city_code = 26;
update ev_data set city_name = '대구광역시'
where city_code = 27;
update ev_data set city_name = '인천광역시'
where city_code = 28;
update ev_data set city_name = '광주광역시'
where city_code = 29;
update ev_data set city_name = '대전광역시'
where city_code = 30;
update ev_data set city_name = '울산광역시'
where city_code = 31;
update ev_data set city_name = '세종특별자치시'
where city_code = 36;
update ev_data set city_name = '경기도'
where city_code = 41;
update ev_data set city_name = '충청북도'
where city_code = 43;
update ev_data set city_name = '충청남도'
where city_code = 44;
update ev_data set city_name = '전라남도'
where city_code = 46;
update ev_data set city_name = '경상북도'
where city_code = 47;
update ev_data set city_name = '경상남도'
where city_code = 48;
update ev_data set city_name = '제주특별자치도'
where city_code = 50;
update ev_data set city_name = '강원특별자치도'
where city_code = 51;
update ev_data set city_name = '전북특별자치도'
where city_code = 52;

CREATE TABLE ev_data_sum AS
SELECT city_code, city_name, SUM(ev_sum) as ev_sum from ev_data
GROUP BY city_code, city_name;

select * from ev_data_sum;

drop table ev_data;

rename table ev_data_sum to ev_data;

select * from ev_data;

ALTER TABLE ev_data ADD PRIMARY KEY (city_code);

SHOW CREATE TABLE ev_data;





