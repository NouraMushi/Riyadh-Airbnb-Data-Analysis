# Riyadh Airbnb Data Analysis 🏡📊

## Introduction

This project focuses on analyzing Airbnb rental data in Riyadh, Saudi Arabia. The aim is to gain insights into the market by cleaning the data, adding new columns, and conducting thorough analysis to understand rental prices, guest preferences, and property distribution across neighborhoods.

## Objective 🎯

The goal of this analysis is to explore the factors influencing rental prices, understand guest preferences, and analyze the distribution of property types in different neighborhoods in Riyadh.

## Data Processing Steps 🔍

### 1. Data Cleaning 🧹

- **City Column**: Standardized repeated city names from Arabic to English (e.g., الرياض → Riyadh).
- **Address Column**: Unified various address formats:
  - الرياض، الرياض، السعودية → Riyadh, Riyadh Province, Saudi Arabia.
- **Amenities Column**: Cleaned the `previewAmenities` column by removing unnecessary characters.

### 2. Adding New Columns ➕ 

- **Neighborhood**: Identified the nearest neighborhood based on property coordinates (latitude and longitude).
- **City Quarter**: Categorized properties by their urban quarters (e.g.,Central Riyadh, North Riyadh, East Riyadh).
- **Nearby Landmarks**: Added a column to list prominent landmarks located within a certain distance from each property.

### 3. Data Analysis 📈

- **Distance Analysis**: Calculated distances to landmarks for each neighborhood.
- **Price Analysis by Host Status**: Analyzed average prices for Superhosts vs. Non-Superhosts.
- **City Quarter Analysis**: Explored how prices and ratings vary across different city quarters.
- **Correlation Analysis**: Calculated correlation coefficients to explore the relationships between guest numbers and pricing.

## Results 📊

- **Most Sought-After Properties**: Entire rental units are the most common, with 371 listings.
  
  <img src="https://github.com/user-attachments/assets/b13ddbf1-23a1-4e30-9c06-2f55074a1696" alt="Most Sought-After Properties" width="400">

- **Average Daily Rental Prices**: Prices vary significantly by property type, with Entire chalets averaging 1459 SAR and Private rooms in rental units at approximately 188 SAR.
  
  <img src="https://github.com/user-attachments/assets/bd60d403-2baf-4e1f-be05-3044cbdebced" alt="Average Daily Rental Prices" width="400">

- **Impact of Number of Bedrooms**: As the number of bedrooms increases, the average daily price rises, with two-bedroom properties averaging 775 SAR and three-bedroom properties averaging 866 SAR.
  
  <img src="https://github.com/user-attachments/assets/34391125-2a2d-4a79-9444-f11d6039d5a6" alt="Impact of Number of Bedrooms" width="400">

- **Geographical Location Impact**: Significant price differences across neighborhoods, with Qurtubah having the highest average daily price of 351 SAR.
  
  <img src="https://github.com/user-attachments/assets/f1f6e941-ed68-454e-9f21-cedcb49ef7ff" alt="Geographical Location Impact" width="400">

- **Preferred Amenities**: Air conditioning and Wi-Fi are strongly linked to higher guest ratings, with average ratings of 5.00 and 4.98, respectively.
  
  <img src="https://github.com/user-attachments/assets/9e572c91-57eb-4fb3-9016-990974e01ba6" alt="Preferred Amenities" width="400">

- **Cancellation Policies**: Flexible cancellation policies are the most common and have an average rating of 4.95.
  
  <img src="https://github.com/user-attachments/assets/5395842e-91a5-493a-addd-6775b621170e" alt="Cancellation Policies" width="400">

## Conclusion 🏆

This analysis reveals that location, amenities, property types, and cancellation policies shape guest satisfaction and pricing in Riyadh. High-rated neighborhoods like Al Manar and properties near landmarks command higher prices. Essential amenities like air conditioning and Wi-Fi boost ratings, and stricter cancellation policies lead to better reviews. Overall, strategic choices drive Airbnb success in Riyadh.


