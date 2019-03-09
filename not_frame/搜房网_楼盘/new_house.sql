/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50723
Source Host           : localhost:3306
Source Database       : soufang

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-10-15 22:22:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for new_house
-- ----------------------------
DROP TABLE IF EXISTS `new_house`;
CREATE TABLE `new_house` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `city` varchar(50) DEFAULT NULL,
  `province` varchar(50) DEFAULT NULL,
  `lp_name` varchar(50) DEFAULT NULL,
  `rooms` varchar(50) DEFAULT NULL,
  `area` varchar(20) DEFAULT NULL,
  `addr` varchar(80) DEFAULT NULL,
  `district` varchar(10) DEFAULT NULL,
  `sale_state` varchar(10) DEFAULT NULL,
  `house_type` varchar(80) DEFAULT NULL,
  `sale` varchar(40) DEFAULT NULL,
  `origin_url` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
