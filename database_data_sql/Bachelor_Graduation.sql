set global local_infile=on;

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

drop table if exists favorite;
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

drop table if exists news;
create table news (
	Id int(11) collate utf8_unicode_ci not null auto_increment,
	Category varchar(20) collate utf8_unicode_ci not null,
	Content text collate utf8_unicode_ci not null,
	primary key (Id)
) ENGINE=InnoDB default charset=utf8 collate=utf8_unicode_ci;
lock tables news write;
load data local infile 'D:/Bachelor_Graduation/train_text_data/dev.txt' into table news(Category,Content);
unlock tables;

set foreign_key_checks=0;

create table favorite (
	Id int(11) collate utf8_unicode_ci not null auto_increment,
	UserId int(11) collate utf8_unicode_ci not null,
	NewsId int(11) collate utf8_unicode_ci not null,
	primary key (Id),
	foreign key (UserId) references users(Id),
	foreign key (NewsId) references news(Id)
) ENGINE=InnoDB default charset=utf8 collate=utf8_unicode_ci;
lock tables favorite write;
insert into favorite values (1,2,0);
insert into favorite values (2,2,1);
insert into favorite values (3,1,0);
insert into favorite values (4,1,6);