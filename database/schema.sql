CREATE DATABASE  IF NOT EXISTS `sieteymedio` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sieteymedio`;
-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: dobleonada.mysql.database.azure.com    Database: sieteymedio
-- ------------------------------------------------------
-- Server version	8.0.39-azure

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
-- Temporary view structure for view `average_bet_per_game`
--

DROP TABLE IF EXISTS `average_bet_per_game`;
/*!50001 DROP VIEW IF EXISTS `average_bet_per_game`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `average_bet_per_game` AS SELECT 
 1 AS `game_id`,
 1 AS `average_bet`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `average_first_round_bet`
--

DROP TABLE IF EXISTS `average_first_round_bet`;
/*!50001 DROP VIEW IF EXISTS `average_first_round_bet`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `average_first_round_bet` AS SELECT 
 1 AS `Game ID`,
 1 AS `Average Bet (First Round)`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `average_last_round_bet`
--

DROP TABLE IF EXISTS `average_last_round_bet`;
/*!50001 DROP VIEW IF EXISTS `average_last_round_bet`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `average_last_round_bet` AS SELECT 
 1 AS `Game ID`,
 1 AS `Average Bet (Last Round)`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `bank_users_per_game`
--

DROP TABLE IF EXISTS `bank_users_per_game`;
/*!50001 DROP VIEW IF EXISTS `bank_users_per_game`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `bank_users_per_game` AS SELECT 
 1 AS `game_id`,
 1 AS `bank_users_count`*/;
SET character_set_client = @saved_cs_client;

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
INSERT INTO `cards` VALUES (1,1,'As de Oros',4,1,1),(2,1,'Dos de Oros',4,2,2),(3,1,'Tres de Oros',4,3,3),(4,1,'Cuatro de Oros',4,4,4),(5,1,'Cinco de Oros',4,5,5),(6,1,'Seis de Oros',4,6,6),(7,1,'Siete de Oros',4,7,7),(8,1,'Ocho de Oros',4,0.5,8),(9,1,'Nueve de Oros',4,0.5,9),(10,1,'Sota de Oros',4,0.5,10),(11,1,'Caballo de Oros',4,0.5,11),(12,1,'Rey de Oros',4,0.5,12),(13,1,'As de Copas',3,1,1),(14,1,'Dos de Copas',3,2,2),(15,1,'Tres de Copas',3,3,3),(16,1,'Cuatro de Copas',3,4,4),(17,1,'Cinco de Copas',3,5,5),(18,1,'Seis de Copas',3,6,6),(19,1,'Siete de Copas',3,7,7),(20,1,'Ocho de Copas',3,0.5,8),(21,1,'Nueve de Copas',3,0.5,9),(22,1,'Sota de Copas',3,0.5,10),(23,1,'Caballo de Copas',3,0.5,11),(24,1,'Rey de Copas',3,0.5,12),(25,1,'As de Espadas',2,1,1),(26,1,'Dos de Espadas',2,2,2),(27,1,'Tres de Espadas',2,3,3),(28,1,'Cuatro de Espadas',2,4,4),(29,1,'Cinco de Espadas',2,5,5),(30,1,'Seis de Espadas',2,6,6),(31,1,'Siete de Espadas',2,7,7),(32,1,'Ocho de Espadas',2,0.5,8),(33,1,'Nueve de Espadas',2,0.5,9),(34,1,'Sota de Espadas',2,0.5,10),(35,1,'Caballo de Espadas',2,0.5,11),(36,1,'Rey de Espadas',2,0.5,12),(37,1,'As de Bastos',1,1,1),(38,1,'Dos de Bastos',1,2,2),(39,1,'Tres de Bastos',1,3,3),(40,1,'Cuatro de Bastos',1,4,4),(41,1,'Cinco de Bastos',1,5,5),(42,1,'Seis de Bastos',1,6,6),(43,1,'Siete de Bastos',1,7,7),(44,1,'Ocho de Bastos',1,0.5,8),(45,1,'Nueve de Bastos',1,0.5,9),(46,1,'Sota de Bastos',1,0.5,10),(47,1,'Caballo de Bastos',1,0.5,11),(48,1,'Rey de Bastos',1,0.5,12),(49,2,'Ace of Diamonds',4,1,1),(50,2,'Two of Diamonds',4,2,2),(51,2,'Three of Diamonds',4,3,3),(52,2,'Four of Diamonds',4,4,4),(53,2,'Five of Diamonds',4,5,5),(54,2,'Six of Diamonds',4,6,6),(55,2,'Seven of Diamonds',4,7,7),(56,2,'Eight of Diamonds',4,0.5,8),(57,2,'Nine of Diamonds',4,0.5,9),(58,2,'Ten of Diamonds',4,0.5,10),(59,2,'Jack of Diamonds',4,0.5,11),(60,2,'Queen of Diamonds',4,0.5,12),(61,2,'King of Diamonds',4,0.5,13),(62,2,'Ace of Hearts',3,1,1),(63,2,'Two of Hearts',3,2,2),(64,2,'Three of Hearts',3,3,3),(65,2,'Four of Hearts',3,4,4),(66,2,'Five of Hearts',3,5,5),(67,2,'Six of Hearts',3,6,6),(68,2,'Seven of Hearts',3,7,7),(69,2,'Eight of Hearts',3,0.5,8),(70,2,'Nine of Hearts',3,0.5,9),(71,2,'Ten of Hearts',3,0.5,10),(72,2,'Jack of Hearts',3,0.5,11),(73,2,'Queen of Hearts',3,0.5,12),(74,2,'King of Hearts',3,0.5,13),(75,2,'Ace of Spades',2,1,1),(76,2,'Two of Spades',2,2,2),(77,2,'Three of Spades',2,3,3),(78,2,'Four of Spades',2,4,4),(79,2,'Five of Spades',2,5,5),(80,2,'Six of Spades',2,6,6),(81,2,'Seven of Spades',2,7,7),(82,2,'Eight of Spades',2,0.5,8),(83,2,'Nine of Spades',2,0.5,9),(84,2,'Ten of Spades',2,0.5,10),(85,2,'Jack of Spades',2,0.5,11),(86,2,'Queen of Spades',2,0.5,12),(87,2,'King of Spades',2,0.5,13),(88,2,'Ace of Clubs',1,1,1),(89,2,'Two of Clubs',1,2,2),(90,2,'Three of Clubs',1,3,3),(91,2,'Four of Clubs',1,4,4),(92,2,'Five of Clubs',1,5,5),(93,2,'Six of Clubs',1,6,6),(94,2,'Seven of Clubs',1,7,7),(95,2,'Eight of Clubs',1,0.5,8),(96,2,'Nine of Clubs',1,0.5,9),(97,2,'Ten of Clubs',1,0.5,10),(98,2,'Jack of Clubs',1,0.5,11),(99,2,'Queen of Clubs',1,0.5,12),(100,2,'King of clubs',1,0.5,13);
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
  PRIMARY KEY (`game_id`,`player_id`),
  KEY `player_id` (`player_id`),
  CONSTRAINT `game_players_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE,
  CONSTRAINT `game_players_ibfk_2` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`) ON DELETE CASCADE
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
  `start_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `end_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `deck_id` int NOT NULL,
  PRIMARY KEY (`game_id`),
  KEY `deck_id` (`deck_id`),
  CONSTRAINT `games_ibfk_1` FOREIGN KEY (`deck_id`) REFERENCES `decks` (`deck_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;

/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `highest_bet_per_game`
--

DROP TABLE IF EXISTS `highest_bet_per_game`;
/*!50001 DROP VIEW IF EXISTS `highest_bet_per_game`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `highest_bet_per_game` AS SELECT 
 1 AS `game_id`,
 1 AS `player_id`,
 1 AS `highest_bet`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `lowest_bet_per_game`
--

DROP TABLE IF EXISTS `lowest_bet_per_game`;
/*!50001 DROP VIEW IF EXISTS `lowest_bet_per_game`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `lowest_bet_per_game` AS SELECT 
 1 AS `game_id`,
 1 AS `player_id`,
 1 AS `lowest_bet`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `player_initial_card_statistic`
--

DROP TABLE IF EXISTS `player_initial_card_statistic`;
/*!50001 DROP VIEW IF EXISTS `player_initial_card_statistic`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `player_initial_card_statistic` AS SELECT 
 1 AS `player_id`,
 1 AS `player_name`,
 1 AS `suit`,
 1 AS `most_repeated_card`,
 1 AS `times_repeated`,
 1 AS `total_games`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `player_rounds`
--

DROP TABLE IF EXISTS `player_rounds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_rounds` (
  `id` int NOT NULL AUTO_INCREMENT,
  `round_id` int NOT NULL,
  `is_bank` tinyint NOT NULL,
  `player_id` int NOT NULL,
  `start_points` int NOT NULL,
  `end_points` int NOT NULL,
  `player_bet` int NOT NULL,
  `first_card_in_hand` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `player_id` (`player_id`),
  KEY `fk_first_card` (`first_card_in_hand`),
  KEY `fk_player_rounds_round_id` (`round_id`),
  CONSTRAINT `fk_first_card` FOREIGN KEY (`first_card_in_hand`) REFERENCES `cards` (`card_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_player_rounds_round_id` FOREIGN KEY (`round_id`) REFERENCES `rounds` (`round_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `player_rounds_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_rounds`
--

LOCK TABLES `player_rounds` WRITE;
/*!40000 ALTER TABLE `player_rounds` DISABLE KEYS */;

UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `player_id` int NOT NULL AUTO_INCREMENT,
  `dni` varchar(20) NOT NULL,
  `name` varchar(45) NOT NULL,
  `risk_level` int NOT NULL,
  `is_ai` tinyint(1) NOT NULL,
  `points` int NOT NULL DEFAULT '0',
  `time` int NOT NULL DEFAULT '0',
  `deleted` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;

/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `players_ranking`
--

DROP TABLE IF EXISTS `players_ranking`;
/*!50001 DROP VIEW IF EXISTS `players_ranking`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `players_ranking` AS SELECT 
 1 AS `player_id`,
 1 AS `player_name`,
 1 AS `total_gains`,
 1 AS `total_games`,
 1 AS `total_minutes_played`*/;
SET character_set_client = @saved_cs_client;

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
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rounds`
--

LOCK TABLES `rounds` WRITE;
/*!40000 ALTER TABLE `rounds` DISABLE KEYS */;

/*!40000 ALTER TABLE `rounds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `average_bet_per_game`
--

/*!50001 DROP VIEW IF EXISTS `average_bet_per_game`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`adminsql`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `average_bet_per_game` AS select `r`.`game_id` AS `game_id`,avg(`pr`.`player_bet`) AS `average_bet` from (`player_rounds` `pr` join `rounds` `r` on((`pr`.`round_id` = `r`.`round_id`))) group by `r`.`game_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `average_first_round_bet`
--

/*!50001 DROP VIEW IF EXISTS `average_first_round_bet`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`adminsql`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `average_first_round_bet` AS select `r`.`game_id` AS `Game ID`,avg(`pr`.`player_bet`) AS `Average Bet (First Round)` from (`rounds` `r` join `player_rounds` `pr` on((`r`.`round_id` = `pr`.`round_id`))) where (`r`.`round_number` = 1) group by `r`.`game_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `average_last_round_bet`
--

/*!50001 DROP VIEW IF EXISTS `average_last_round_bet`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`adminsql`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `average_last_round_bet` AS select `r`.`game_id` AS `Game ID`,avg(`pr`.`player_bet`) AS `Average Bet (Last Round)` from (`rounds` `r` join `player_rounds` `pr` on((`r`.`round_id` = `pr`.`round_id`))) where (`r`.`round_number` = (select max(`r2`.`round_number`) from `rounds` `r2` where (`r2`.`game_id` = `r`.`game_id`))) group by `r`.`game_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `bank_users_per_game`
--

/*!50001 DROP VIEW IF EXISTS `bank_users_per_game`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`adminsql`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `bank_users_per_game` AS select `r`.`game_id` AS `game_id`,count(distinct `pr`.`player_id`) AS `bank_users_count` from (`player_rounds` `pr` join `rounds` `r` on((`pr`.`round_id` = `r`.`round_id`))) where (`pr`.`is_bank` = 1) group by `r`.`game_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `highest_bet_per_game`
--

/*!50001 DROP VIEW IF EXISTS `highest_bet_per_game`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`adminsql`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `highest_bet_per_game` AS select `r`.`game_id` AS `game_id`,`pr`.`player_id` AS `player_id`,max(`pr`.`player_bet`) AS `highest_bet` from (`player_rounds` `pr` join `rounds` `r` on((`pr`.`round_id` = `r`.`round_id`))) group by `r`.`game_id`,`pr`.`player_id` having (`highest_bet` = (select max(`pr2`.`player_bet`) from (`player_rounds` `pr2` join `rounds` `r2` on((`pr2`.`round_id` = `r2`.`round_id`))) where (`r2`.`game_id` = `r`.`game_id`))) order by `highest_bet` desc,`pr`.`player_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `lowest_bet_per_game`
--

/*!50001 DROP VIEW IF EXISTS `lowest_bet_per_game`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`adminsql`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `lowest_bet_per_game` AS select `r`.`game_id` AS `game_id`,`pr`.`player_id` AS `player_id`,min(`pr`.`player_bet`) AS `lowest_bet` from (`player_rounds` `pr` join `rounds` `r` on((`pr`.`round_id` = `r`.`round_id`))) group by `r`.`game_id`,`pr`.`player_id` having (`lowest_bet` = (select min(`pr2`.`player_bet`) from (`player_rounds` `pr2` join `rounds` `r2` on((`pr2`.`round_id` = `r2`.`round_id`))) where (`r2`.`game_id` = `r`.`game_id`))) order by `lowest_bet`,`pr`.`player_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `player_initial_card_statistic`
--

/*!50001 DROP VIEW IF EXISTS `player_initial_card_statistic`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`adminsql`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `player_initial_card_statistic` AS select `p`.`player_id` AS `player_id`,`p`.`name` AS `player_name`,substring_index(`c`.`name`,' ',-(1)) AS `suit`,`c`.`name` AS `most_repeated_card`,count(0) AS `times_repeated`,count(distinct `r`.`game_id`) AS `total_games` from ((((`players` `p` join `player_rounds` `pr` on((`p`.`player_id` = `pr`.`player_id`))) join `rounds` `r` on((`pr`.`round_id` = `r`.`round_id`))) join `games` `g` on((`r`.`game_id` = `g`.`game_id`))) join `cards` `c` on((`pr`.`first_card_in_hand` = `c`.`card_id`))) where ((`r`.`round_number` = 0) and (`p`.`deleted` = 0)) group by `p`.`player_id`,`c`.`card_id` having (`total_games` >= 3) order by `p`.`player_id`,`times_repeated` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `players_ranking`
--

/*!50001 DROP VIEW IF EXISTS `players_ranking`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`adminsql`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `players_ranking` AS select `p`.`player_id` AS `player_id`,`p`.`name` AS `player_name`,`p`.`points` AS `total_gains`,count(distinct `r`.`game_id`) AS `total_games`,`p`.`time` AS `total_minutes_played` from (((`players` `p` join `player_rounds` `pr` on((`p`.`player_id` = `pr`.`player_id`))) join `rounds` `r` on((`pr`.`round_id` = `r`.`round_id`))) join `games` `g` on((`r`.`game_id` = `g`.`game_id`))) where (`p`.`deleted` = 0) group by `p`.`player_id` order by `total_gains` desc,`total_games` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-20 16:43:26
