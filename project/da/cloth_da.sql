

create database clothing_shop_db;


use clothing_shop_db;

create table if not exists cloths (
    id int auto_increment primary key,
    name varchar(255) not null,
    size varchar(50),
    price dec(10, 2) not null,
    quantity int not null default 0

);