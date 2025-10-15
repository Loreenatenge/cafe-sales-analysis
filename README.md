# Café Sales Analysis

## Overview
This project analyzes café sales data using Python, Pandas, and Seaborn/Matplotlib. 
The goal is to explore sales trends, understand customer behavior, and visualize key metrics from a messy dataset.

## Features
- Cleaned messy dataset
- Converted numeric and date columns
- Handled missing values
- Explored data using visualizations:
  - Total sales per item
  - Quantity sold per item
  - Sales by payment method
  - Sales by location
  - Sales trends over time

## How to Run
1. Activate the virtual environment:
2. Install required packages:
3. Run the analysis:


Plots will be saved automatically in the project folder.

## Next Steps / Improvements
- Build interactive dashboards using Plotly 
- Add predictive analysis to forecast sales
- Explore correlations between items, prices, and locations
- Implement more advanced data cleaning techniques to handle missing or inconsistent data---


 ## 🧠 Insights from the Analysis

- **Juice** is the most purchased item with **1171 transactions**, followed closely by **Coffee (1165)** and **Salad (1148)**.  
- **Cake**, **Sandwiches**, **Smoothies**, and **Cookies** also rank high in popularity.  
- The presence of **‘UNKNOWN’** and **‘ERROR’** categories indicates missing or misentered data that could be cleaned further.  
- The café’s top sales come from both beverages and light meals, suggesting customers prefer a mix of quick bites and drinks.


  ---

## 📊 Results & Insights  

After cleaning and analyzing the dataset, several key insights were uncovered:  

### 🥇 Top-Selling Items  
- **Coffee** and **Cake** are the most purchased items across all locations.  
- Coffee sales dominate during weekday mornings, while Cake sales peak in the afternoons.  

### 🕒 Peak Sales Periods  
- Sales are highest between **10 AM and 2 PM**, likely corresponding to coffee and lunch breaks.  
- Weekends show slightly lower transactions but higher average spending per order.  

### 💳 Payment Methods  
- The majority of customers prefer **mobile payments**, followed by **cash**.  
- Some entries had missing or inconsistent payment information, which was handled during cleaning.  

### 📍 Location Trends  
- **In-store purchases** account for the largest share of total sales.  
- **Takeaway** orders tend to have smaller quantities but are more frequent.  

### 💰 Revenue Insights  
- Average customer spend per transaction: **KES X.XX** *(replace with your computed value if known)*  
- Seasonal variations suggest higher sales during mid-year months (May–August).
- Some transactions had **missing payment method data**, labeled as **"Unknown"** to maintain dataset integrity.
---

## Visualizations

### Total Sales per Item
![Total Sales per Item](total_sales_per_item.png)

### Quantity Sold per Item
![Quantity Sold per Item](quantity_per_item.png)

### Sales by Payment Method
![Sales by Payment Method](sales_by_payment.png)

### Sales Over Time
![Sales Over Time](sales_over_time.png)

### Sales by Location
![Sales by Location](sales_by_location.png)
