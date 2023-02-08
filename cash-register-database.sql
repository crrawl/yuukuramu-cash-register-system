-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 08, 2023 at 01:11 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cash-register-database`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `parrent_id` int(11) DEFAULT NULL,
  `category_id` int(11) NOT NULL,
  `category_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`parrent_id`, `category_id`, `category_name`) VALUES
(NULL, 1, 'Food'),
(NULL, 2, 'Drinks'),
(NULL, 3, 'gadgets'),
(3, 4, 'pc'),
(3, 5, 'phone'),
(NULL, 6, 'books'),
(6, 7, 'hacker_books');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `barcode` varchar(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `count` int(3) NOT NULL DEFAULT 0,
  `weight` float NOT NULL,
  `category` int(10) NOT NULL,
  `price` float NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `barcode`, `name`, `count`, `weight`, `category`, `price`) VALUES
(20, '4510', 'Samsung Galaxy A20e', 1, 0.7, 5, 300.99),
(22, '4521', 'Iphone 12 Pro Max 512GB', 12, 0.7, 5, 1200),
(23, '4523', 'Iphone 12 Pro 512GB', 12, 0.7, 5, 1000),
(24, '4524', 'Iphone 12 512GB', 12, 0.7, 5, 800),
(25, '4525', 'Iphone 12 512GB', 12, 0.7, 5, 800),
(26, '4526', 'Piens Farn Milk 3.2% 1L', 3, 0.7, 5, 0.99),
(27, '4527', 'Apelsīni mazie C4/5 NAVELINA 2.šķ.', 3, 7, 5, 1.3),
(29, '45429', 'Exploits', 1, 0, 4, 4000);

-- --------------------------------------------------------

--
-- Table structure for table `sellers`
--

CREATE TABLE `sellers` (
  `seller_id` int(11) NOT NULL,
  `seller_name` varchar(255) NOT NULL,
  `category` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sellers`
--

INSERT INTO `sellers` (`seller_id`, `seller_name`, `category`) VALUES
(3, 'SIA \"Jarvis Rose\"', 6),
(4, 'SIA \"Baltic Tehnologies\"', 3),
(45, 'Evil Corp', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sellers`
--
ALTER TABLE `sellers`
  ADD PRIMARY KEY (`seller_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `sellers`
--
ALTER TABLE `sellers`
  MODIFY `seller_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
