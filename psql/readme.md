> \c - подключение к бд
> \du - показывает всех пользователей
> \dt - показывает все таблицы внутри бд
> \d <название таблицы> - более подробная информация о таблице
> \l - показывает весь список бд
> \q - выход из субд(quit)

sudo -u postgres psql - команда для захода через юзера postgres

CREATE USER <username> WITH PASSWORD 'password';
ALTER ROLE <username> <привелегии>;
CREATE DATABASE <username> WITH OWNER <username>;

int:
    bigint - 8-байтовое число
    integer - 4-байтовое число
    smallint - 2-батовое число
    serial - авто инкрементация
str:
    char(10) - фиксированная длина строки
    varchar(10) - фиксированная длина строки
    text - безграничная длина строки
date:
    timestamp - дата и время
    time - время
    date - дата
boolean - true|false

<!-- char | varchar -->
CREATE DATABASE <название бд>;
CREATE TABLE <название таблицы> (
    column1 varchar NOT NULL
);