-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.33 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for store
CREATE DATABASE IF NOT EXISTS `store` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `store`;

-- Dumping structure for table store.customer
CREATE TABLE IF NOT EXISTS `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `customer_name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table store.invoice
CREATE TABLE IF NOT EXISTS `invoice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cus_id` int(11) NOT NULL,
  `create_date` datetime NOT NULL,
  `pay_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cus_id` (`cus_id`) USING BTREE,
  CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`cus_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table store.invoice_detail
CREATE TABLE IF NOT EXISTS `invoice_detail` (
  `FK_i_id` int(11) NOT NULL,
  `FK_p_id` int(11) NOT NULL,
  `quantity` int(11) unsigned NOT NULL DEFAULT '1',
  `curr_unit_price` double unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`FK_i_id`,`FK_p_id`),
  KEY `FK_invoiceID` (`FK_i_id`) USING BTREE,
  KEY `FK_productID` (`FK_p_id`) USING BTREE,
  CONSTRAINT `FK_invoice_detail_invoice` FOREIGN KEY (`FK_i_id`) REFERENCES `invoice` (`id`),
  CONSTRAINT `FK_invoice_detail_product` FOREIGN KEY (`FK_p_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table store.product
CREATE TABLE IF NOT EXISTS `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `unit_price` double DEFAULT NULL,
  `location` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_update` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

-- Dumping structure for table store.test
CREATE TABLE IF NOT EXISTS `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
