/*

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50527
 Source Host           : localhost
 Source Database       : cc98

 Target Server Type    : MySQL
 Target Server Version : 50527
 File Encoding         : utf-8

*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ---------------------------
--  Table structure for `user`
-- ---------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
	`uid` int(11) NOT NULL AUTO_INCREMENT,
	`email` text,
	`username` text,
	`nickname` text,
	`password` text,
	`avatar` text,
	`signature` text,
	`location` text,
	`website` text,
	`company` text,
	`role` int(11) DEFAULT NULL,
	`balance` int(11) DEFAULT NULL,
	`reputation` int(11) DEFAULT NULL,
	`self_intro` text,
	`github` text,
	`wechat` text,
	`created_at` datetime DEFAULT NULL,
	`updated_at` datetime DEFAULT NULL,
	`last_login` datetime DEFAULT NULL,
	PRIMARY KEY (`uid`)
) ENGINE=MyISAM AUTO_INCREMENT=169 DEFAULT CHARSET=utf8;
delimiter ;;
CREATE TRIGGER `user_delete_trigger` BEFORE DELETE ON `user` FOR EACH ROW 
BEGIN
		DELETE FROM topic WHERE topic.author_id = OLD.uid;
		DELETE FROM reply WHERE reply.author_id = OLD.uid;
		DELETE FROM notification WHERE notification.trigger_user_id = OLD.uid;
		DELETE FROM notification WHERE notification.involved_user_id = OLD.uid;
END;
 ;;
delimiter ;

-- ------------------------------------
--  Table strucuture for `node`
-- ------------------------------------
DROP TABLE IF EXISTS `node`;
CREATE TABLE `node` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`name` text,
	`slug` text,
	`thumb` text,
	`intro` text,
	`created_at` text,
	`updated_at` text,
	`plane_id` int(11) DEFAULT NULL,
	`topic_count` int(11) DEFAULT NULL,
	`Ccustom_style` text,
	`limit_reputation` int(11) DEFAULT NULL,
	PRIMARY KEY (`id`)		
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `topic`
-- ----------------------------
DROP TABLE IF EXISTS `topic`;
CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` text,
	`content` text,
	`status` int(11) DEFAULT NULL,
	`hits` int(11) DEFAULT NULL,
	`created_at` datetime DEFAULT NULL,
	`updated_at` datetime DEFAULT NULL,
	`node_id` int(11) DEFAULT NULL,
	`author_id` int(11) DEFAULT NULL,
	`reply_count` int(11) DEFAULT NULL,
	`last_replied_by` text,
	`last_replied_time` datetime DEFAULT NULL,
  `up_vote` int(11) DEFAULT NULL,
  `down_vote` int(11) DEFAULT NULL,
  `last_touched` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
delimiter ;;
CREATE TRIGGER `topic_delete_trigger` BEFORE DELETE ON `topic` FOR EACH ROW 
BEGIN
    DELETE FROM reply WHERE reply.topic_id = OLD.id;
    DELETE FROM notification WHERE notification.involved_topic_id = OLD.id;
END;
 ;;
delimiter ;

-- ----------------------------
--  Table structure for `reply`
-- ----------------------------
DROP TABLE IF EXISTS `reply`;
CREATE TABLE `reply` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`topic_id` int(11) DEFAULT NULL,
	`author_id` int(11) DEFAULT NULL,
	`content` text,
	`created_at` datetime DEFAULT NULL,
	`updated_at` datetime DEFAULT NULL,
	`up_vote` int(11) DEFAULT NULL,
	`down_vote` int(11) DEFAULT NULL,
	`last_touched` datetime DEFAULT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8;

-- -----------------------------------
--  Table structure for `notification`
-- -----------------------------------
DROP TABLE IF EXISTS `notification`;
CREATE TABLE `notification` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`content` text,
	`status` int(11) DEFAULT NULL,
	`involved_type` int(11) DEFAULT NULL,
	`involved_user_id` int(11) DEFAULT NULL,
	`involved_topic_id` int(11) DEFAULT NULL,
	`involved_reply_id` int(11) DEFAULT NULL,
	`trigger_user_id` int(11) DEFAULT NULL,
	`occurrence_time` datetime DEFAULT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=255 DEFAULT CHARSET=utf8;

-- --------------------------
-- Table structure for `vote`
-- --------------------------
DROP TABLE IF EXISTS `vote`;
CREATE TABLE `vote` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) DEFAULT NULL,
  `involved_type` int(11) DEFAULT NULL,
  `involved_user_id` int(11) DEFAULT NULL,
  `involved_topic_id` int(11) DEFAULT NULL,
  `involved_reply_id` int(11) DEFAULT NULL,
  `trigger_user_id` int(11) DEFAULT NULL,
  `occurrence_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

-- ----------------------------------
--  Table strucuture for `collection`
-- ----------------------------------
DROP TABLE IF EXISTS `collection`;
CREATE TABLE `collection` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`owner_user_id` int(11) DEFAULT NULL,
	`involved_type` int(11) DEFAULT NULL,
	`involved_topic_id` int(11) DEFAULT NULL,
	`involved_type_id` int(11) DEFAULT NULL,
	`created_at` datetime DEFAULT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- TODO
-- plane transaction
















