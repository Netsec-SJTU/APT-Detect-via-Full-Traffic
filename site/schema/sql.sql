DROP DATABASE IF EXISTS `aptd`;
-- apt detect

CREATE DATABASE `aptd` DEFAULT CHARACTER SET utf8 collate utf8_general_ci;

use `aptd`;

CREATE TABLE `traffic` (
    `uid` VARCHAR(32) NOT NULL,
    `srcip` VARCHAR(32) NOT NULL,
    `dstip` VARCHAR(32) NOT NULL,
    `dstport` INT NOT NULL,
    `info` VARCHAR(600) NOT NULL,
    `comment` VARCHAR(600) NOT NULL
);

CREATE TABLE `malware` (
    `uid` VARCHAR(32) NOT NULL,
    `md5` VARCHAR(32) NOT NULL,
    `sha1` VARCHAR(64) NOT NULL,
    `mtype` VARCHAR(20) NOT NULL,
    `info` VARCHAR(600) NOT NULL,
    `comment` VARCHAR(600) NOT NULL
);


-- CREATE USER 'aptd'@'localhost' IDENTIFIED BY 'random_password';
GRANT all privileges ON aptd.* TO 'aptd'@'localhost';
