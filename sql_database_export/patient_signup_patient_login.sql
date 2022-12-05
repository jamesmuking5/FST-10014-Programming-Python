-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: patient_signup
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patient_login`
--

DROP TABLE IF EXISTS `patient_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_login` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `patient_ic` varchar(50) NOT NULL,
  `patient_password` varchar(50) DEFAULT NULL,
  `full_name` varchar(50) DEFAULT NULL,
  `blood_pressure` varchar(50) DEFAULT 'Empty. To fill.',
  `spo2` varchar(50) DEFAULT 'Empty. To fill.',
  `heart_rate` varchar(50) DEFAULT 'Empty. To fill.',
  `temperature` varchar(50) DEFAULT 'Empty. To fill.',
  `current_diseases` varchar(150) DEFAULT 'Empty. To fill.',
  `medical_history` varchar(800) DEFAULT 'Empty. To fill.',
  `patient_weight` varchar(50) DEFAULT NULL,
  `patient_height` varchar(50) DEFAULT NULL,
  `bmi` varchar(50) DEFAULT NULL,
  `allergies` varchar(150) DEFAULT NULL,
  `patient_contact` varchar(50) DEFAULT NULL,
  `patient_emergency` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`patient_id`,`patient_ic`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Relevant patient details\n';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_login`
--

LOCK TABLES `patient_login` WRITE;
/*!40000 ALTER TABLE `patient_login` DISABLE KEYS */;
INSERT INTO `patient_login` VALUES (1,'user123','user123','Ricardo Milos','102/85','100','85','36.5','Hyoertension, Diabetes','Caeserean G2P2','89','180','25','Nuts','0197771236','0128766612');
/*!40000 ALTER TABLE `patient_login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-06  3:19:30
