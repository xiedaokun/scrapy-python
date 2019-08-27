/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1_3306
Source Server Version : 50505
Source Host           : 127.0.0.1:3306
Source Database       : article_spider

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2019-08-27 16:23:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jobbole_article
-- ----------------------------
DROP TABLE IF EXISTS `jobbole_article`;
CREATE TABLE `jobbole_article2` (
  `url_object_id` varchar(50) NOT NULL COMMENT '封面图',
  `first_image` varchar(300) NOT NULL DEFAULT '',
  `front_image_url` varchar(300) DEFAULT NULL,
  `front_image_path` varchar(200) DEFAULT NULL,
  `title` varchar(200) NOT NULL DEFAULT '',
  `content` longtext DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `give_sums` int(11) DEFAULT 0,
  `download_nums` int(11) DEFAULT 0,
  `source_letters` varchar(200) DEFAULT NULL,
  `update_time` date DEFAULT NULL,
  `subtitle_size` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`url_object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
