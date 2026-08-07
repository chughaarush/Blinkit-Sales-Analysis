
USE blinkit_sales;
# First 10 rows of table
-- SELECT * FROM blinkit 
-- LIMIT 10;

# Total sales
-- SELECT SUM(Sales) AS Total_Sales
-- FROM blinkit;

#Average sales
-- SELECT AVG(Sales) AS Average_Sales
-- FROM blinkit;

# Highest sales
-- SELECT MAX(Sales) AS Highest_Sale
-- FROM blinkit;

# Lowest sales
-- SELECT MIN(Sales) AS Lowest_Sale
-- FROM blinkit;

#total sales acc to item type
-- SELECT `Item Type`, SUM(Sales) AS Total_Sales
-- FROM blinkit
-- GROUP BY `Item Type`
-- ORDER BY Total_Sales DESC;

#Avg sales by item type
-- SELECT `Item Type`, AVG(Sales) AS avg_Sales
-- FROM blinkit
-- GROUP BY `Item Type`
-- ORDER BY avg_Sales DESC;

#avg rating of each item type
-- SELECT `Item Type`, AVG(Rating) as avg_rating
-- FROM blinkit
-- GROUP BY `Item Type`
-- ORDER BY avg_rating

#total sales in relative to outlet size
-- SELECT `Outlet Size`,
--        SUM(Sales) AS Total_Sales
-- FROM blinkit
-- GROUP BY `Outlet Size`
-- ORDER BY Total_Sales DESC;

#Product count relative to outlet size
-- SELECT `Outlet Size`,
--        COUNT(*) AS Product_Count
-- FROM blinkit
-- GROUP BY `Outlet Size`
-- ORDER BY Product_Count DESC;

#sales acc to outlet location type 
-- SELECT `Outlet Location Type`,
--        SUM(Sales) AS Total_Sales
-- FROM blinkit
-- GROUP BY `Outlet Location Type`
-- ORDER BY Total_Sales DESC;

#total sales acc to item fat content
-- SELECT `Item Fat Content`,
-- SUN(Sales) AS Total_Sales
-- FROM blinkit
-- GROUP BY `Item Fat Content`
-- ORDER BY Total_Sales DESC;

#sales by item fat content
-- SELECT `Item Fat Content`,
--        SUM(Sales) AS Total_Sales
-- FROM blinkit
-- GROUP BY `Item Fat Content`
-- ORDER BY Total_Sales DESC;

#top 10 highest selling products
-- SELECT `Item Identifier`,
--        Sales
-- FROM blinkit
-- ORDER BY Sales DESC
-- LIMIT 10;

#top 10 highest rated products
-- SELECT `Item Identifier`,
--        Rating
-- FROM blinkit
-- ORDER BY Rating DESC
-- LIMIT 10;

#Item Types having Average Rating greater than 4
-- SELECT `Item Type`, AVG(Rating)
-- FROM blinkit
-- GROUP BY `Item Type`
-- HAVING AVG(Rating) > 4
-- ORDER BY AVG(Rating) DESC;

# Outlet Sizes having Total Sales greater than 100000
-- SELECT `Outlet Size`, SUM(Sales) AS total_sales 
-- FROM blinkit 
-- GROUP BY `Outlet Size`
-- HAVING total_sales > 100000
-- ORDER BY SUM(Sales) DESC

# Show only Low Fat and Regular products
-- SELECT *
-- FROM blinkit
-- WHERE `Item Fat Content` IN ('Low Fat','Regular');

# show where item starts with FD
-- SELECT *
-- FROM blinkit
-- WHERE `Item Identifier` LIKE 'FD%';

#categorize sales
-- SELECT
--     `Item Identifier`,
--     Sales,
--     CASE
--         WHEN Sales > 200 THEN 'High Sales'
--         WHEN Sales >= 100 THEN 'Medium Sales'
--         ELSE 'Low Sales'
--     END AS Sales_Category
-- FROM blinkit;


# Categorize Ratings
-- SELECT 
-- `Item Identifier`,
-- `Rating`,
-- CASE
--         WHEN Rating >= 4 THEN 'Excellent'
--         WHEN Rating >= 3 THEN 'Good'
--         ELSE 'Poor'
--     END AS Rating_Category
-- FROM blinkit;


# Products having Sales greater than the average Sales
-- SELECT * FROM blinkit
-- WHERE Sales>
-- ( SELECT AVG(Sales)
-- FROM blinkit
-- );


# High-selling Low Fat products
-- SELECT *
-- FROM blinkit
-- WHERE `Item Fat Content` = 'Low Fat'
-- AND Sales > 200;

#Top 5 highest-rated products
-- SELECT
--     `Item Identifier`,
--     Rating
-- FROM blinkit
-- ORDER BY Rating DESC
-- LIMIT 5;