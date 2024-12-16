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
  
  ![1](https://github.com/user-attachments/assets/bb1d7466-d35f-49c5-be5a-8d451f85fd51)

- **Average Daily Rental Prices**: Prices vary significantly by property type, with Entire chalets averaging 1459 SAR and Private rooms in rental units at approximately 188 SAR.
  
  ![2](https://github.com/user-attachments/assets/9910dc7a-f26c-4283-b9de-f9b97371c49a)
  
- **Impact of Number of Bedrooms**: As the number of bedrooms increases, the average daily price rises, with two-bedroom properties averaging 775 SAR and three-bedroom properties averaging 866 SAR.
  
  ![3](https://github.com/user-attachments/assets/f03b97c9-4605-435d-a79c-a33d06bd90e2)

- **Geographical Location Impact**: Significant price differences across neighborhoods, with Qurtubah having the highest average daily price of 351 SAR.
  
  ![4](https://github.com/user-attachments/assets/021a7d84-cc83-467c-9214-e60dd964d78d)

- **Preferred Amenities**: Air conditioning and Wi-Fi are strongly linked to higher guest ratings, with average ratings of 5.00 and 4.98, respectively.
  
  ![5](https://github.com/user-attachments/assets/275dcd20-1d27-4fca-80c3-f217a15bbba7)

- **Cancellation Policies**: Flexible cancellation policies are the most common and have an average rating of 4.95.

  ![6](https://github.com/user-attachments/assets/bfefae43-e39d-429f-81b1-291ffbfcf9d8)
  
## Conclusion 🏆

This analysis reveals that location, amenities, property types, and cancellation policies shape guest satisfaction and pricing in Riyadh. High-rated neighborhoods like Al Manar and properties near landmarks command higher prices. Essential amenities like air conditioning and Wi-Fi boost ratings, and stricter cancellation policies lead to better reviews. Overall, strategic choices drive Airbnb success in Riyadh.


