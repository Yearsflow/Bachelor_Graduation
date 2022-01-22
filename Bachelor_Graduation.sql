drop table if exists administrator;
create table administrator (
	Id varchar(8) collate utf8_unicode_ci not null,
	Name varchar(10) collate utf8_unicode_ci not null,
	Email varchar(20) collate utf8_unicode_ci not null,
	Password text collate utf8_unicode_ci not null,
	primary key (Id)
) ENGINE=InnoDB default charset=utf8 collate=utf8_unicode_ci;

lock tables administrator write;
insert into administrator values ('0000','admin','admin@tust.edu.cn','admin');
unlock tables;

drop table if exists users;
create table users (
	Id varchar(8) collate utf8_unicode_ci not null,
	Name varchar(8) collate utf8_unicode_ci not null,
	Email varchar(20) collate utf8_unicode_ci not null,
	Password text collate utf8_unicode_ci not null,
	primary key (Id)
) ENGINE=InnoDB default charset=utf8 collate=utf8_unicode_ci;

lock tables users write;
insert into users values ('0000','test','test@tust.edu.cn','123456');
insert into users values ('0001','DCrusher','yearsflow@126.com','123456');
unlock tables;