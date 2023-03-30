# Troubleshooting Common SQL Errors with BigQuery

## Task 3. Find the total number of customers who went through checkout

1. What's wrong with the previous query to view 1000 items?
   - We have not specified any columns in the SELECT
   - There is a typo in the dataset name

2. What's wrong with the new previous query to view 1000 items?
   - We are using legacy SQL

3. What is wrong with the previous query?
   - Still no columns defined in SELECT

4. What is wrong with the previous query?
   - The page title is missing from the columns in SELECT
   - Without aggregations, limits, or sorting, this query is not insightful

5. How many columns will the previous query return?
   - 1, a column named hits_page_pageTitle

6. What is wrong with the previous query?
   - The COUNT() function does not de-deduplicate the same fullVisitorId
   - It is missing a GROUP BY clause

7. BQ query 1

## Task 4. List the cities with the most transactions with your ecommerce site

1. Which city had the most distinct visitors? Ignore the value: 'not available in this demo dataset'
   - Mountain View

2. What is wrong with the previous query?
   - You cannot filter aggregated fields in the `WHERE` clause (use `HAVING` instead)
   - You cannot filter on aliased fields within the `WHERE` clause

3. BQ query 2

## Task 5. Find the total number of products in each product category

1. What is wrong with the previous query?
   - No aggregate functions are used
   - Large GROUP BYs really hurt performance (consider filtering first and/or using aggregation functions)

2. What is wrong with the previous query which lists products?
   - The COUNT() function is not the distinct number of products in each category

3. Which category has the most distinct number of products offered?
   - (not set)

4. BQ query 3
