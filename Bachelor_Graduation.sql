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