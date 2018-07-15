DROP DATABASE IF EXISTS `aptd`;
-- apt detect

CREATE DATABASE `aptd` DEFAULT CHARACTER SET utf8 collate utf8_general_ci;

use `aptd`;

CREATE TABLE `traffic` (
    `uid` VARCHAR(32) NOT NULL,
    `srcip` VARCHAR(32) NOT NULL,
    `srcport` INT NOT NULL,
    `dstip` VARCHAR(32) NOT NULL,
    `dstport` INT NOT NULL,
    `threat` VARCHAR(30) NOT NULL,
    `severity` VARCHAR(10) NOT NULL,
    `proto` VARCHAR(10) NOT NULL,
    `time` TIMESTAMP,
    `reference` VARCHAR(100) NOT NULL,
    `comment` VARCHAR(600) NOT NULL
);

CREATE TABLE `malware` (
    `uid` VARCHAR(32) NOT NULL,
    `sha256` VARCHAR(64) NOT NULL,
    `filename` VARCHAR(100) NOT NULL,
    `time` TIMESTAMP,
    `mtype` VARCHAR(20) NOT NULL,
    -- malware type
    `severity` VARCHAR(10) NOT NULL,
    `reference` VARCHAR(100) NOT NULL,
    -- refer to how to make sure that
    `comment` VARCHAR(600) NOT NULL
    -- some info, such as come from where
);

CREATE TABLE `http`  (
    `uid` VARCHAR(32) NOT NULL,
    `method` VARCHAR(32) NOT NULL,
    `url` VARCHAR(32) NOT NULL,
    `host` VARCHAR(32) NOT NULL,
    `ua` VARCHAR(32) NOT NULL,
    `get` VARCHAR(32) NOT NULL,
    `post` VARCHAR(32) NOT NULL,
    `cookie` VARCHAR(32) NOT NULL
);

CREATE TABLE `tcp`  (
    `uid` VARCHAR(32) NOT NULL,
    `srcip` VARCHAR(32) NOT NULL,
    `srcport` INT NOT NULL,
    `dstip` VARCHAR(32) NOT NULL,
    `dstport` INT NOT NULL,
    `payload` TEXT NOT NULL
);

CREATE TABLE `udp`  (
    `uid` VARCHAR(32) NOT NULL,
    `srcip` VARCHAR(32) NOT NULL,
    `srcport` INT NOT NULL,
    `dstip` VARCHAR(32) NOT NULL,
    `dstport` INT NOT NULL,
    `payload` TEXT NOT NULL
);

CREATE TABLE `httpids` (
    `uid` VARCHAR(32) NOT NULL,
    `key` VARCHAR(30) NOT NULL, 
    -- *
    -- ua
    -- url
    -- get
    -- post
    -- cookie
    -- file
    -- split by '|'
    `value` VARCHAR(200) NOT NULL,
    -- regex
    `threat` VARCHAR(30) NOT NULL,
    `severity` VARCHAR(10) NOT NULL,
    `reference` VARCHAR(100) NOT NULL
);

CREATE TABLE `fileids` (
    `uid` VARCHAR(32) NOT NULL,
    `mtype` VARCHAR(20) NOT NULL,
    -- malware type
    `severity` VARCHAR(10) NOT NULL,
    `reference` VARCHAR(100) NOT NULL
    -- refer to how to make sure that
);

CREATE TABLE `freq` (
    `uid` VARCHAR(32) NOT NULL,
    `srcip` VARCHAR(32) NOT NULL,
    `srcport` INT NOT NULL,
    `dstip` VARCHAR(32) NOT NULL,
    `dstport` INT NOT NULL,
    `time` TIMESTAMP
);

CREATE USER 'aptd'@'localhost' IDENTIFIED BY 'random_password';
GRANT all privileges ON aptd.* TO 'aptd'@'localhost';
