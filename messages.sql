--
-- Table structure for table `messages`
--
DROP TABLE IF EXISTS `messages`;

CREATE TABLE `messages` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `callid` varchar(255) DEFAULT NULL,
  `callerid` varchar(255) DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `replyto` mediumint(9) DEFAULT NULL,
  `archived` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
