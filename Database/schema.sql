CREATE DATABASE  IF NOT EXISTS `sieteYmedio` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sieteYmedio`;
-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: sieteYmedio
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

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
-- Table structure for table `cards`
--

DROP TABLE IF EXISTS `cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cards` (
  `card_id` int NOT NULL AUTO_INCREMENT,
  `deck_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `priority` int NOT NULL,
  `real_value` float NOT NULL,
  `value` int NOT NULL,
  PRIMARY KEY (`card_id`),
  KEY `deck_id` (`deck_id`),
  CONSTRAINT `cards_ibfk_1` FOREIGN KEY (`deck_id`) REFERENCES `decks` (`deck_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards`
--

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;
INSERT INTO `cards` VALUES (1,1,'As de Oros',4,1,1),(2,1,'Dos de Oros',4,2,2),(3,1,'Tres de Oros',4,3,3),(4,1,'Cuatro de Oros',4,4,4),(5,1,'Cinco de Oros',4,5,5),(6,1,'Seis de Oros',4,6,6),(7,1,'Siete de Oros',4,0.5,7),(8,1,'Ocho de Oros',4,0.5,8),(9,1,'Nueve de Oros',4,0.5,9),(10,1,'Sota de Oros',4,0.5,10),(11,1,'Caballo de Oros',4,0.5,11),(12,1,'Rey de Oros',4,0.5,12),(13,1,'As de Copas',3,1,1),(14,1,'Dos de Copas',3,2,2),(15,1,'Tres de Copas',3,3,3),(16,1,'Cuatro de Copas',3,4,4),(17,1,'Cinco de Copas',3,5,5),(18,1,'Seis de Copas',3,6,6),(19,1,'Siete de Copas',3,0.5,7),(20,1,'Ocho de Copas',3,0.5,8),(21,1,'Nueve de Copas',3,0.5,9),(22,1,'Sota de Copas',3,0.5,10),(23,1,'Caballo de Copas',3,0.5,11),(24,1,'Rey de Copas',3,0.5,12),(25,1,'As de Espadas',2,1,1),(26,1,'Dos de Espadas',2,2,2),(27,1,'Tres de Espadas',2,3,3),(28,1,'Cuatro de Espadas',2,4,4),(29,1,'Cinco de Espadas',2,5,5),(30,1,'Seis de Espadas',2,6,6),(31,1,'Siete de Espadas',2,0.5,7),(32,1,'Ocho de Espadas',2,0.5,8),(33,1,'Nueve de Espadas',2,0.5,9),(34,1,'Sota de Espadas',2,0.5,10),(35,1,'Caballo de Espadas',2,0.5,11),(36,1,'Rey de Espadas',2,0.5,12),(37,1,'As de Bastos',1,1,1),(38,1,'Dos de Bastos',1,2,2),(39,1,'Tres de Bastos',1,3,3),(40,1,'Cuatro de Bastos',1,4,4),(41,1,'Cinco de Bastos',1,5,5),(42,1,'Seis de Bastos',1,6,6),(43,1,'Siete de Bastos',1,0.5,7),(44,1,'Ocho de Bastos',1,0.5,8),(45,1,'Nueve de Bastos',1,0.5,9),(46,1,'Sota de Bastos',1,0.5,10),(47,1,'Caballo de Bastos',1,0.5,11),(48,1,'Rey de Bastos',1,0.5,12),(49,2,'Ace of Diamonds',4,1,1),(50,2,'Two of Diamonds',4,2,2),(51,2,'Three of Diamonds',4,3,3),(52,2,'Four of Diamonds',4,4,4),(53,2,'Five of Diamonds',4,5,5),(54,2,'Six of Diamonds',4,6,6),(55,2,'Seven of Diamonds',4,7,7),(56,2,'Eight of Diamonds',4,0.5,8),(57,2,'Nine of Diamonds',4,0.5,9),(58,2,'Ten of Diamonds',4,0.5,10),(59,2,'Jack of Diamonds',4,0.5,11),(60,2,'Queen of Diamonds',4,0.5,12),(61,2,'King of Diamonds',4,0.5,13),(62,2,'Ace of Hearts',3,1,1),(63,2,'Two of Hearts',3,2,2),(64,2,'Three of Hearts',3,3,3),(65,2,'Four of Hearts',3,4,4),(66,2,'Five of Hearts',3,5,5),(67,2,'Six of Hearts',3,6,6),(68,2,'Seven of Hearts',3,7,7),(69,2,'Eight of Hearts',3,0.5,8),(70,2,'Nine of Hearts',3,0.5,9),(71,2,'Ten of Hearts',3,0.5,10),(72,2,'Jack of Hearts',3,0.5,11),(73,2,'Queen of Hearts',3,0.5,12),(74,2,'King of Hearts',3,0.5,13),(75,2,'Ace of Spades',2,1,1),(76,2,'Two of Spades',2,2,2),(77,2,'Three of Spades',2,3,3),(78,2,'Four of Spades',2,4,4),(79,2,'Five of Spades',2,5,5),(80,2,'Six of Spades',2,6,6),(81,2,'Seven of Spades',2,7,7),(82,2,'Eight of Spades',2,0.5,8),(83,2,'Nine of Spades',2,0.5,9),(84,2,'Ten of Spades',2,0.5,10),(85,2,'Jack of Spades',2,0.5,11),(86,2,'Queen of Spades',2,0.5,12),(87,2,'King of Spades',2,0.5,13),(88,2,'Ace of Clubs',1,1,1),(89,2,'Two of Clubs',1,2,2),(90,2,'Three of Clubs',1,3,3),(91,2,'Four of Clubs',1,4,4),(92,2,'Five of Clubs',1,5,5),(93,2,'Six of Clubs',1,6,6),(94,2,'Seven of Clubs',1,7,7),(95,2,'Eight of Clubs',1,0.5,8),(96,2,'Nine of Clubs',1,0.5,9),(97,2,'Ten of Clubs',1,0.5,10),(98,2,'Jack of Clubs',1,0.5,11),(99,2,'Queen of Clubs',1,0.5,12),(100,2,'King of clubs',1,0.5,13);
/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `decks`
--

DROP TABLE IF EXISTS `decks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `decks` (
  `deck_id` int NOT NULL AUTO_INCREMENT,
  `deck_name` varchar(45) NOT NULL,
  PRIMARY KEY (`deck_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `decks`
--

LOCK TABLES `decks` WRITE;
/*!40000 ALTER TABLE `decks` DISABLE KEYS */;
INSERT INTO `decks` VALUES (1,'Spanish Deck'),(2,'Poker Deck');
/*!40000 ALTER TABLE `decks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_players`
--

DROP TABLE IF EXISTS `game_players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_players` (
  `game_id` int NOT NULL,
  `player_id` int NOT NULL,
  KEY `game_id` (`game_id`),
  KEY `player_id` (`player_id`),
  CONSTRAINT `game_players_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`),
  CONSTRAINT `game_players_ibfk_2` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_players`
--

LOCK TABLES `game_players` WRITE;
/*!40000 ALTER TABLE `game_players` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `game_id` int NOT NULL AUTO_INCREMENT,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `deck_id` int NOT NULL,
  PRIMARY KEY (`game_id`),
  KEY `deck_id` (`deck_id`),
  CONSTRAINT `games_ibfk_1` FOREIGN KEY (`deck_id`) REFERENCES `decks` (`deck_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_rounds`
--

DROP TABLE IF EXISTS `player_rounds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_rounds` (
  `round_id` int NOT NULL AUTO_INCREMENT,
  `round_number` int NOT NULL,
  `player_id` int NOT NULL,
  `start_points` int NOT NULL,
  `end_points` int NOT NULL,
  `player_bet` int NOT NULL,
  `is_bank` tinyint NOT NULL,
  PRIMARY KEY (`round_id`),
  KEY `player_id` (`player_id`),
  CONSTRAINT `player_rounds_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_rounds`
--

LOCK TABLES `player_rounds` WRITE;
/*!40000 ALTER TABLE `player_rounds` DISABLE KEYS */;
/*!40000 ALTER TABLE `player_rounds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `player_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `risk_level` int NOT NULL,
  `is_ai` tinyint(1) NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rounds`
--

DROP TABLE IF EXISTS `rounds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rounds` (
  `round_id` int NOT NULL AUTO_INCREMENT,
  `game_id` int NOT NULL,
  `round_number` int NOT NULL,
  PRIMARY KEY (`round_id`),
  KEY `game_id` (`game_id`),
  CONSTRAINT `rounds_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rounds`
--

LOCK TABLES `rounds` WRITE;
/*!40000 ALTER TABLE `rounds` DISABLE KEYS */;
/*!40000 ALTER TABLE `rounds` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-10 18:25:15
