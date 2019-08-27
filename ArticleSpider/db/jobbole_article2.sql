/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1_3306
Source Server Version : 50505
Source Host           : 127.0.0.1:3306
Source Database       : article_spider

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2019-08-27 16:24:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jobbole_article
-- ----------------------------
DROP TABLE IF EXISTS `jobbole_article`;
CREATE TABLE `jobbole_article` (
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

-- ----------------------------
-- Records of jobbole_article
-- ----------------------------
INSERT INTO `jobbole_article` VALUES ('0', 'http://www.zimuku.la/images/v2/no_litpic.gif', '', 'full/aca5ba0cd01a99de31f6a83d4c437e145fc27acd.jpg', '', null, '', '0', '0', '', '0000-00-00', null);
INSERT INTO `jobbole_article` VALUES ('060fde4a69847b060747fdd8a01515e9', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '桑迪顿 第1集【YYeTs字幕组 简繁英双语字幕】sanditon.s01e01.720p.hdtv.x264-mtb', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('09b4e027b5096ba1f8dd1ed87c9177ec', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '黑衣人：全球追缉(Men.in.Black.International) 【YYeTs字幕组 简繁英双语字幕】Men.in.Black.International.2019.720p/1080p.BluRay.x264-GECKOS；Men.in.Black.International.2019.720p/1080p.WEB-DL.DD5.1.H264-FGT', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('0e5b2d75d3368db63c1712742e3d4d2a', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, 'aladdin.2019.720p.bluray.x264-sparks.srt', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('3094a977a890b88e96f167df7a28aad2', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '虎兄虎弟 Two Brothers (2004) 雙虎奇緣', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('410ef241b29e66df940fdadfc297eba8', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '传教士 第四季第五集【YYeTs字幕组 简繁英双语字幕】preacher.s04e05.720p.web.h264-tbs', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('5e9d53d13393200460ed5c78cb187419', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '生活向上 第1季第4集【YYeTs字幕组 简繁英双语字幕】This.Way.Up.S01E04.Episode.4.720p/1080p.HULU.WEB-DL.AAC2.0.H.264-monkee', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('61aca46988ed72828f5fef76d34b968d', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '栋笃特工[5.4](粤)Agent.Mr.Chan.2018.CHINESE.1080p.BluRay.x264.DD5.1-CHD.rar', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('64a40b474dc1b31d66818e3d275d37b6', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '母子情深 Sweet Mud (2006) 甜蜜大地 Adama Meshuga\'at', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('6a794713e10f2852367d91ed07e5be7a', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '黑衣人：全球追缉（双语特效字幕）Men.in.Black.International.2019.1080p.AMZN.WEBRip.DDP5.1.x264-NTG.ass', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('6fe41a2fa05bd5e55df5dc6ecd09ee52', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '【精校特效双语】疾速追杀3.John.Wick.3.2019.1080p.Bluray.X264-EVO.ass', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('7882486062ec38a57e24f43cd0ff5c10', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '潜水钟与蝴蝶 The Diving Bell and the Butterfly (2007) Le scaphandre et le papillon', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('8', 'http://www.zimuku.la/images/v2/no_litpic.gif', '', 'full/b971eced463fe739e9efc95de21a769f686bcb8b.jpg', '', null, '', '0', '0', '', '0000-00-00', null);
INSERT INTO `jobbole_article` VALUES ('8461f255959db5dff687c2a42c7068e3', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '一条狗的使命2(A Dog\'s Journey) 【YYeTs字幕组 简繁英双语字幕】A.Dogs.Journey.2019.720p/1080p.WEB-DL.DD5.1.H264-FGT', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('8924deba1cee75cf1e447b04f4fce57c', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '虫洞效应 The Last Mimzy (2007) 神秘寶盒', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('8b5d397ac6d78f5133179155ef7eb1c8', 'http://www.zimuku.la/images/v2/no_litpic.gif', '', 'full/b971eced463fe739e9efc95de21a769f686bcb8b.jpg', '', null, '', '0', '0', '', '0000-00-00', null);
INSERT INTO `jobbole_article` VALUES ('8c1bb31a2478ef734e0129e2dfe80257', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '雷和莉兹(中英双语字幕)Ray.and.Liz.2018.1080p.BluRay.H264.AAC-RARBG.zip', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('a75ab32de2719db65bd5fd4cab6a2d68', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '浴血黑帮 第5季第1集【YYeTs字幕组 简繁英双语字幕】Peaky.Blinders.S05E01.Black.Tuesday.720p/1080p.AMZN.WEB-DL.DD+5.1.H.264-AJP69', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('af154cadaf3ba916acc07f7d61997018', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '波达克 第五季 第8集【YYeTs字幕组 简繁英双语字幕】Poldark.2015.S05E08.720p.HDTV.x264-BRISK.rar', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('cef676d4edbf8f9b5072dce23bff6b2d', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '【蓝光精校双语】爱宠大机密2.The.Secret.Life.of.Pets.2.2019.1080p.BluRay.x264.DTS-FGT.ass', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('d64740ddc99a34d93b6094fd101b282e', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '铁狱魔难 Brokedown Palace (1999) 強迫入境', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('dd58e16628f69c9ee6d66e5f992863c9', 'http://www.zimuku.la/images/v2/no_litpic.gif', '', 'full/b4f24e5922ccbe9f14dca360be826e90e9e2ba05.jpg', '', null, '', '0', '0', '', '0000-00-00', null);
INSERT INTO `jobbole_article` VALUES ('e12de6afb3040e8f441316811b98f64b', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '球手 第五季第一集【YYeTs字幕组 简繁英双语字幕】Ballers.S05E01.Protocol.Is.for.Losers.720p/1080p.AMZN.WEB-DL.DDP5.1.H.264-NTb', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('e8d138901e71dff19f64a28aa9da25de', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '阿拉丁(Aladdin) 【YYeTs字幕组 简繁英双语字幕】Aladdin.2019.1080p.HDRip.x264.DD5.1-SHITBOX', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('ec508d333447f82446e1957a439334a0', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '传教士 第四季(第5集-简繁英双语字幕)preacher.s04e05.1080p.web.h264-tbs.chs.eng.rar', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('f5fa1f2bb423825bfa2db5edf17f303d', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '我亲爱的表哥.Primos(Cousins).2019.720p.WEB-DL.x264.ass', null, null, '0', '0', null, null, null);
INSERT INTO `jobbole_article` VALUES ('f9c6b9a4f76707d3b7c4cb64b8ecabb4', 'http://www.zimuku.la/images/v2/no_litpic.gif', null, null, '荒野寻踪 The Missing (2003) 鬼影迷蹤', null, null, '0', '0', null, null, null);
