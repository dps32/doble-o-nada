-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
-- Temporary view structure for view `player_initial_card_statistics`
--

DROP TABLE IF EXISTS `player_initial_card_statistics`;
/*!50001 DROP VIEW IF EXISTS `player_initial_card_statistics`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `player_initial_card_statistics` AS SELECT 
 1 AS `player_id`,
 1 AS `player_name`,
 1 AS `suit`,
 1 AS `initial_card_name`,
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!50001 VIEW `player_initial_card_statistic` AS select `p`.`player_id` AS `player_id`,`p`.`name` AS `player_name`,substring_index(`c`.`name`,' ',-(1)) AS `suit`,`c`.`name` AS `most_repeated_card`,count(0) AS `times_repeated`,count(distinct `r`.`game_id`) AS `total_games` from ((((`players` `p` join `player_rounds` `pr` on((`p`.`player_id` = `pr`.`player_id`))) join `rounds` `r` on((`pr`.`round_id` = `r`.`round_id`))) join `games` `g` on((`r`.`game_id` = `g`.`game_id`))) join `cards` `c` on((`pr`.`first_card_in_hand` = `c`.`card_id`))) where (`r`.`round_number` = 0) group by `p`.`player_id`,`c`.`card_id` having (`total_games` >= 3) order by `p`.`player_id`,`times_repeated` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `player_initial_card_statistics`
--

/*!50001 DROP VIEW IF EXISTS `player_initial_card_statistics`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`adminsql`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `player_initial_card_statistics` AS select `pr`.`player_id` AS `player_id`,`p`.`name` AS `player_name`,`c`.`priority` AS `suit`,`c`.`name` AS `initial_card_name`,count(0) AS `times_repeated`,count(distinct `r`.`game_id`) AS `total_games` from ((((`player_rounds` `pr` join `rounds` `r` on((`pr`.`round_id` = `r`.`round_id`))) join `games` `g` on((`r`.`game_id` = `g`.`game_id`))) join `players` `p` on((`pr`.`player_id` = `p`.`player_id`))) join `cards` `c` on((`pr`.`first_card_in_hand` = `c`.`card_id`))) where (`r`.`round_number` = 1) group by `pr`.`player_id`,`c`.`card_id` having (`total_games` > 3) order by `pr`.`player_id`,`times_repeated` desc */;
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
/*!50001 VIEW `players_ranking` AS select `p`.`player_id` AS `player_id`,`p`.`name` AS `player_name`,sum((`pr`.`end_points` - `pr`.`start_points`)) AS `total_gains`,count(distinct `r`.`game_id`) AS `total_games`,`p`.`time` AS `total_minutes_played` from ((`players` `p` join `player_rounds` `pr` on((`p`.`player_id` = `pr`.`player_id`))) join `rounds` `r` on((`pr`.`round_id` = `r`.`round_id`))) group by `p`.`player_id` order by `total_gains` desc,`total_games` desc */;
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

-- Dump completed on 2025-01-18 19:25:29
