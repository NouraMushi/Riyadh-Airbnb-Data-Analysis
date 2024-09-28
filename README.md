# Riyadh-Airbnb-Data-Analysis 🏡📊

## Introduction

This project focuses on analyzing Airbnb rental data in Riyadh, Saudi Arabia. The aim is to understand the market by cleaning the data, adding new columns, and analyzing the information to gain valuable insights into rentals and guest preferences.

## Objective 🎯

The goal of this analysis is to explore the factors influencing rental prices, understand guest preferences, and analyze the distribution of property types across different neighborhoods.

## Data Processing Steps 🔍

### 1. Data Cleaning 🧹

- **City Column**: Replaced repeated values from Arabic to English (e.g., الرياض → Riyadh).
- **Address Column**: Unified similar address formats:
  - الرياض، الرياض، السعودية → Riyadh، Riyadh Province، Saudi Arabia
- **Amenities Column**: Removed unnecessary characters from the `previewAmenities` column.

### 2. Adding New Columns ➕ 

- **Neighborhood**: Identifies the nearest neighborhood based on the property's latitude and longitude.
- **City Quarter**: Categorizes the property by its urban quarter (e.g., Central Riyadh, North Riyadh).
- **Nearby Landmarks**: Added a column to list landmarks within a specified distance from the property.

### 3. Data Analysis 📈

- **Distance Analysis**: Calculated distances to nearby landmarks for each neighborhood.
- **Average Price Analysis**: Analyzed average prices based on host status (Superhosts and Non-Superhosts).
- **City Quarter Analysis**: Examined how prices and ratings vary across different city quarters.
- **Correlation Analysis**: Calculated the correlation coefficient to identify relationships between the number of guests and pricing.

## Results 📊

- **Most Sought-After Properties**: The most common property type is the Entire rental unit, with 371 listings.
  
  <img src="https://github.com/user-attachments/assets/b13ddbf1-23a1-4e30-9c06-2f55074a1696" alt="Most Sought-After Properties" width="400">

- **Average Daily Rental Prices**: Vary significantly across property types, with the Entire chalet averaging 1459 SAR and the Private room in rental unit at approximately 188 SAR.
  
  <img src="https://github.com/user-attachments/assets/bd60d403-2baf-4e1f-be05-3044cbdebced" alt="Average Daily Rental Prices" width="400">

- **Impact of Number of Bedrooms**: As the number of bedrooms increases, the average daily price also tends to increase significantly (775 SAR for two bedrooms, 866 SAR for three bedrooms).
  
  <img src="https://github.com/user-attachments/assets/34391125-2a2d-4a79-9444-f11d6039d5a6" alt="Impact of Number of Bedrooms" width="400">

- **Geographical Location's Impact**: Notable price variances across different neighborhoods, with Qurtubah having the highest average price of 351 SAR.
  
  <img src="https://github.com/user-attachments/assets/f1f6e941-ed68-454e-9f21-cedcb49ef7ff" alt="Geographical Location's Impact" width="400">

- **Preferred Amenities**: Air conditioning and Wifi are linked to high average ratings of 5.00 and 4.98, respectively.
  
  <img src="https://github.com/user-attachments/assets/9e572c91-57eb-4fb3-9016-990974e01ba6" alt="Preferred Amenities" width="400">

- **Cancellation Policies**: Flexible Cancellation policies are the most common, with an average rating of 4.95.
  
  <img src="https://github.com/user-attachments/assets/5395842e-91a5-493a-addd-6775b621170e" alt="Cancellation Policies" width="400">

## Conclusion 🏆

The analysis revealed that location, property type, and amenities play a significant role in determining prices and guest preferences. Higher-rated properties tend to command higher rental prices, highlighting the importance of providing quality services.
