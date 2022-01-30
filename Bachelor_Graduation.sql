drop table if exists administrator;
create table administrator (
	Id int(11) collate utf8_unicode_ci not null auto_increment,
	Name varchar(10) collate utf8_unicode_ci not null,
	Email varchar(20) collate utf8_unicode_ci not null,
	Password text collate utf8_unicode_ci not null,
	primary key (Id)
) ENGINE=InnoDB default charset=utf8 collate=utf8_unicode_ci;

lock tables administrator write;
insert into administrator values (100,'admin','admin@tust.edu.cn','admin');
unlock tables;

drop table if exists users;
create table users (
	Id int(11) collate utf8_unicode_ci not null auto_increment,
	Name varchar(8) collate utf8_unicode_ci not null,
	Email varchar(20) collate utf8_unicode_ci not null,
	Password text collate utf8_unicode_ci not null,
	primary key (Id)
) ENGINE=InnoDB default charset=utf8 collate=utf8_unicode_ci;

lock tables users write;
insert into users values (1,'test','test@tust.edu.cn','123456');
insert into users values (2,'DCrusher','yearsflow@126.com','123456');
unlock tables;