-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.48 - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             9.5.0.5222
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for bhptaledb
CREATE DATABASE IF NOT EXISTS `bhptaledb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `bhptaledb`;

-- Dumping structure for table bhptaledb.bhptale_roledetails
CREATE TABLE IF NOT EXISTS `bhptale_roledetails` (
  `email` varchar(255) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `fullname` varchar(225) DEFAULT NULL,
  `mobile` bigint(20) NOT NULL,
  `address` varchar(225) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `otp` varchar(255) DEFAULT NULL,
  `otp_time` varchar(255) DEFAULT NULL,
  `verify_link` varchar(255) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  `password` varchar(225) NOT NULL,
  `last_login` varchar(255),
  PRIMARY KEY (`email`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `username` (`username`),
  KEY `bhptale_roledetails_role_id_b599a879_fk_bhptale_userrole_id` (`role_id`),
  CONSTRAINT `bhptale_roledetails_role_id_b599a879_fk_bhptale_userrole_id` FOREIGN KEY (`role_id`) REFERENCES `bhptale_userrole` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table bhptaledb.bhptale_roledetails: ~1 rows (approximately)
/*!40000 ALTER TABLE `bhptale_roledetails` DISABLE KEYS */;
INSERT INTO `bhptale_roledetails` (`email`, `username`, `fullname`, `mobile`, `address`, `gender`, `otp`, `otp_time`, `verify_link`, `active`, `role_id`, `password`, `last_login`) VALUES
	('arunkr8217@gmail.com', 'arun8217', 'Arun Kumar', 8968606280, 'Sector 6 Panchkula', 'Male', '0', '0', '', 1, 3, 'arun8217--', '2019-06-05 10:05:47.689618');
/*!40000 ALTER TABLE `bhptale_roledetails` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
