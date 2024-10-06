pip install geopy

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.io as pio
from geopy.distance import geodesic
from tabulate import tabulate

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/DataAnalysis-challenge/RiyadhAirBnbProcessed_Data.csv")

df.head(3)

print(df.info())

"""# **Clean data**

**Rating column**
"""

# df[df['rating'].isna()]

# df['rating'].fillna("null", inplace=True)
# df['rating'] = df['rating'].replace('null', np.nan)
# # df['rating'] = df['rating'].astype(float, errors='ignore')

"""**City column**"""

df[df['city'] == 'الرياض']

df['city'] = df['city'].replace({'الرياض': 'Riyadh'})

"""**Address column**"""

df[df['address'].isin([
    'الرياض, Riyadh Province, Saudi Arabia',
    'الرياض, منطقة الرياض, Saudi Arabia'
])]

df['address'] = df['address'].replace({
    'الرياض, Riyadh Province, Saudi Arabia': 'Riyadh, Riyadh Province, Saudi Arabia',
    'الرياض, منطقة الرياض, Saudi Arabia': 'Riyadh, Riyadh Province, Saudi Arabia'
})

"""**Mdify preview Amenities**"""

df['previewAmenities'] = df['previewAmenities'].str.replace(r'[\{\}""]', '', regex=True)

# amenities = df['previewAmenities'].str.cat(sep=',').split(',')

# cleaned_amenities = [amenity.strip() for amenity in amenities]

"""---

---

# *Add columns*

**Add neighborhood column**
"""

unique_latitudes = df['lat'].unique()
unique_longitudes = df['lng'].unique()

unique_values_df = pd.DataFrame({
    'Unique Latitudes': unique_latitudes,
    'Unique Longitudes': unique_longitudes
})

print(unique_values_df)

df=df.rename(columns={'lat':'latitude',
                  'lng':'longitude'})

riyadh_neighborhoods = [
    {"name": "Al Olaya", "latitude": 24.7136, "longitude": 46.6753},
    {"name": "Al Malaz", "latitude": 24.6745, "longitude": 46.7133},
    {"name": "Al Murabba", "latitude": 24.6740, "longitude": 46.7145},
    {"name": "Al Sulaymaniyah", "latitude": 24.6868, "longitude": 46.6962},
    {"name": "Al Nasiriyah", "latitude": 24.6618, "longitude": 46.6852},
    {"name": "Al Manar", "latitude": 24.7253, "longitude": 46.8101},
    {"name": "Al Rawdah", "latitude": 24.7520, "longitude": 46.7450},
    {"name": "Hittin", "latitude": 24.7525, "longitude": 46.6270},
    {"name": "Al Yasmin", "latitude": 24.7876, "longitude": 46.6988},
    {"name": "Al Wurud", "latitude": 24.6948, "longitude": 46.6856},
    {"name": "Al Malqa", "latitude": 24.7944, "longitude": 46.6402},
    {"name": "Al Sahafah", "latitude": 24.7998, "longitude": 46.6403},
    {"name": "An Nakheel", "latitude": 24.7406, "longitude": 46.6481},
    {"name": "Al Muruj", "latitude": 24.7486, "longitude": 46.6524},
    {"name": "Al Nafel", "latitude": 24.7838, "longitude": 46.6674},
    {"name": "Al Rabwah", "latitude": 24.6813, "longitude": 46.7463},
    {"name": "Al Qadisiyah", "latitude": 24.7385, "longitude": 46.8602},
    {"name": "Al Khaleej", "latitude": 24.7460, "longitude": 46.8362},
    {"name": "Al Munsiyah", "latitude": 24.7722, "longitude": 46.8220},
    {"name": "Al Hamra", "latitude": 24.7763, "longitude": 46.7762},
    {"name": "Al Izdihar", "latitude": 24.7794, "longitude": 46.7119},
    {"name": "Al Ghadeer", "latitude": 24.7671, "longitude": 46.6405},
    {"name": "Qurtubah", "latitude": 24.7881, "longitude": 46.7554},
    {"name": "Al Fayha", "latitude": 24.6838, "longitude": 46.7782}
]

neighborhood_df = pd.DataFrame(riyadh_neighborhoods)

def find_neighborhood(lat, lon):
    distances = np.sqrt((neighborhood_df['latitude'] - lat)**2 + (neighborhood_df['longitude'] - lon)**2)
    nearest_index = distances.idxmin()
    return neighborhood_df.iloc[nearest_index]['name']

df['neighborhood'] = df.apply(lambda row: find_neighborhood(row['latitude'], row['longitude']), axis=1)

print(df[['latitude', 'longitude', 'neighborhood']].head())

"""**Add city quarte**

موقع تصنيف احياء الرياض :
https://guide.saudigates.net/%D8%AE%D8%B1%D9%8A%D8%B7%D8%A9-%D8%A7%D8%AD%D9%8A%D8%A7%D8%A1-%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6/#:~:text=%D8%AE%D8%B1%D9%8A%D8%B7%D8%A9%20%D8%A7%D8%AD%D9%8A%D8%A7%D8%A1%20%D8%B4%D8%B1%D9%82%20%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6%3A&text=%D8%AD%D9%8A%20%D8%A7%D9%84%D9%8A%D8%B1%D9%85%D9%88%D9%83%20%E2%80%93%20%D8%AD%D9%8A%20%D8%A7%D9%84%D9%85%D8%BA%D8%B2%D8%B1%D8%A7%D8%AA%20%E2%80%93%20%D8%AD%D9%8A,%E2%80%93%20%D8%AD%D9%8A%20%D8%A7%D8%B4%D8%A8%D9%8A%D9%84%D9%8A%D8%A7%20%E2%80%93%20%D8%AD%D9%8A%20%D8%A7%D9%84%D8%B1%D9%88%D8%A7%D8%A8%D9%8A.
"""

city_quarters = {
    "Central Riyadh": [
        "Al Olaya",
        "Al Malaz",
        "Al Murabba",
        "Al Sulaymaniyah",
        "Al Nasiriyah",
        "Al Rabwah"
    ],
    "North Riyadh": [
        "Hittin",
        "Al Yasmin",
        "Al Malqa",
        "Al Sahafah",
        "Al Muruj",
        "Al Nafel",
        "Al Ghadeer",
        "An Nakheel",
        "Al Wurud",
        "Qurtubah"
    ],
    "East Riyadh": [
        "Al Manar",
        "Al Rawdah",
        "Al Khaleej",
        "Al Munsiyah",
        "Al Hamra",
        "Al Qadisiyah",
        "Al Fayha",
        "Al Izdihar"
    ]
}

def get_city_quarter(neighborhood):
    for quarter, neighborhoods in city_quarters.items():
        if neighborhood in neighborhoods:
            return quarter
    return None

df['city_quarter'] = df['neighborhood'].apply(get_city_quarter)

print(df[['neighborhood','city_quarter']].head())

"""**Add landmarks column**"""

landmarks = {
    'Historical Diriyah': (24.7335, 46.5758),
    'Mamlaka Tower': (24.7311, 46.6701),
    'King Fahd National Library': (24.6858, 46.6870),
    'National Museum': (24.6477, 46.7102),
    'Hall of King Abdulaziz': (24.6438, 46.7115),
    'Murabba Palace': (24.6464, 46.7092),
    'Boulevard': (24.7694, 46.6046),
    'King Khalid Airport': (24.9596, 46.7024)
}

def find_landmarks(row, landmarks, threshold=12):
    listing_location = (row['latitude'], row['longitude'])
    nearby_landmarks = []
    distances = {}

    for landmark, loc in landmarks.items():
        distance = geodesic(listing_location, loc).kilometers
        if distance <= threshold:
            nearby_landmarks.append(landmark)
            distances[landmark] = distance

    if nearby_landmarks:
        sorted_landmarks = sorted(distances.items(), key=lambda x: x[1])
        nearby_landmarks = [landmark for landmark, _ in sorted_landmarks[:2]]

    return nearby_landmarks


df['Nearby Landmarks'] = df.apply(find_landmarks, axis=1, landmarks=landmarks)


print(df[['neighborhood', 'city_quarter','Nearby Landmarks']].head())

df.head(3)

"""---

---

# **تحليلات بالجداول ومعامل الارتباط**

**Add tourist attractions**
"""

def calculate_distances(row, landmarks):
    listing_location = (row['latitude'], row['longitude'])
    distances = {landmark: geodesic(listing_location, loc).kilometers for landmark, loc in landmarks.items()}
    return pd.Series(distances)


distances_df = df.apply(calculate_distances, axis=1, landmarks=landmarks)


distances_df['neighborhood'] = df['neighborhood']

distances_df = distances_df[['neighborhood'] + [col for col in distances_df.columns if col != 'neighborhood']]


distances_df = distances_df.drop_duplicates(subset='neighborhood')


distances_df.columns = ['Neighborhood', 'Historical Diriyah', 'Mamlaka Tower',
                         'King Fahd National Library', 'National Museum',
                         'Hall of King Abdulaziz', 'Murabba Palace', 'Boulevard', 'King Khalid Airport']


table = tabulate(distances_df, headers='keys', tablefmt='fancy_grid', showindex=False)
print(table)

"""**Correlate super host status with pricing**"""

average_price_by_host_status = df.groupby('isSuperhost')['TotalPrice'].mean().reset_index()

average_price_table = tabulate(average_price_by_host_status, headers='keys', tablefmt='fancy_grid', showindex=False)

print("Average Price by Super Host Status:")
print(average_price_table)


df['isSuperhost_numeric'] = df['isSuperhost'].astype(int)


correlation = df['isSuperhost_numeric'].corr(df['TotalPrice'])

print(f'Correlation between super host status and price: {correlation:.2f}')

"""مقارنة الأسعار بين الأجزاء المختلفة من المدينة.
دراسة تأثير "city quarter" على تقييمات الضيوف.
"""

quarterly_analysis = df.groupby('city_quarter').agg({
    'TotalPrice': 'mean',
    'rating': 'mean',
    'PricePerDay':'mean'
}).reset_index()

quarterly_table = tabulate(quarterly_analysis, headers='keys', tablefmt='fancy_grid', showindex=False)

print(quarterly_table)

"""**حساب معامل الارتباط بين عدد الأشخاص والسعر في اليوم والسعر الإجمالي**"""

correlation_matrix = df[['persons', 'PricePerDay']].corr()
# 'TotalPrice',

table = tabulate(correlation_matrix, headers='keys', tablefmt='fancy_grid')
print(table)

# persons_total_price_corr = correlation_matrix.loc['persons', 'TotalPrice']
persons_price_per_day_corr = correlation_matrix.loc['persons', 'PricePerDay']

# print(f"Correlation between persons and TotalPrice: {persons_total_price_corr}")
print(f"Correlation between persons and PricePerDay: {persons_price_per_day_corr}")

df.head(3)

"""**ANOVA to test for statistical significance in price differences across regions**

الموقع الجغرافي له تأثير كبير على السعر
"""

from scipy import stats

anova_result = stats.f_oneway(
    df[df['city_quarter'] == 'Central Riyadh']['PricePerDay'],
    df[df['city_quarter'] == 'North Riyadh']['PricePerDay'],
    df[df['city_quarter'] == 'East Riyadh']['PricePerDay']
)

# Display the p-value result
anova_result.pvalue

# Calculate the correlation between 'rating' and 'PricePerDay'
correlation = df['rating'].corr(df['PricePerDay'])
print(f"Correlation between rating and PricePerDay: {correlation}")

"""---

---

# **اجوبه الاسئله**

ما هي العقارات الأكثر طلبًا في سوق Airbnb بالرياض؟

ما هو متوسط سعر الإيجار اليومي لكل نوع من أنواع العقارات في الرياض؟

ما هو تأثير عدد غرف النوم على متوسط سعر الإيجار اليومي في الرياض؟

كيف يؤثر الموقع الجغرافي (الحي) على متوسط أسعار الإيجارات في الرياض؟

ما هو توزيع عقارات Airbnb من حيث المواقع الجغرافية؟

ما هي أكثر الخدمات التي يفضلها الضيوف في الرياض، وكيف تؤثر هذه الخدمات على متوسط تقييم الضيوف للعقارات؟

كيف يرتبط سعر الإيجار اليومي بتقييمات الضيوف في سوق Airbnb بالرياض؟

كيف تؤثر سياسات الإلغاء على سلوك المستأجرين وتقييماتهم في الرياض؟

كيف يتم توزيع أنواع العقارات في أعلى 10 أحياء بالرياض؟

ما هي الأحياء الأعلى تقييمًا في الرياض؟

أكثر أنواع العقارات طلبا


أكثر أنواع العقارات طلبا هي "**Entire rental unit**" (371 قائمة)، تليها "**Private room in rental unit**" (29 قائمة).
"""

most_common_types = df['type'].value_counts()
print("Most common property types:\n", most_common_types)
print(f"The most common property type is: {most_common_types.idxmax()} with {most_common_types.max()} listings.")

property_counts = df['type'].value_counts()

fig = px.bar(most_common_types,
             x=property_counts.index,
             y=property_counts.values,
             labels={'x': 'Property Type', 'y': 'Number of Listings'},
             title='Distribution of Riyadh Airbnb Listings by Property Type',
             color=property_counts.index,
             color_discrete_sequence=px.colors.qualitative.Pastel
             )
fig.update_layout(
            title_font=dict(size=24),
            xaxis_tickangle=-15,
            margin={"r":0,"t":40,"l":40,"b":0},
            width=1200,
            height=600
)
fig.show()

"""**متوسط الاسعار حسب نوع العقار**

(Entire chalet) هي الأغلى بمتوسط سعر يومي يصل إلى 1459 SAR.
"""

df['PricePerDay'] = df['PricePerDay'].astype(int)
avg_price_per_type = df.groupby('type')['PricePerDay'].mean().reset_index()
avg_price_per_type.columns = ['Property Type', 'Average Price (SAR)']
print(avg_price_per_type)

fig_avg_price = px.pie(avg_price_per_type,
                        values='Average Price (SAR)',
                        names='Property Type',
                        title='Average Price by Property Type in Riyadh',
                        color='Property Type',
                        color_discrete_sequence=px.colors.qualitative.Pastel)

fig_avg_price.update_layout(
                      title_font=dict(size=24),
                      margin={"r":10,"t":40,"l":40,"b":10},
                      width=1000,
            height=600
)
fig_avg_price.show()

"""**تأثير عدد الغرف بالسعر**


متوسط سعر الإيجار يرتفع مع زيادة عدد غرف النوم، حيث أن متوسط السعر لعدد غرف نوم 3 هو 866.00 ريال سعودي، بينما لعدد غرف نوم 0 هو 236.00 ريال سعودي.
"""

summary = df[['name', 'bedrooms', 'PricePerDay', 'type', 'rating']]

average_price_per_bedroom = df.groupby('bedrooms')['PricePerDay'].mean().reset_index()
average_price_per_bedroom.columns = ['Number of Bedrooms', 'Average Price Per Day (SAR)']

print(average_price_per_bedroom)

fig = px.scatter(average_price_per_bedroom,
                 x='Number of Bedrooms',
                 y='Average Price Per Day (SAR)',
                 title='Average Price Per Day by Number of Bedrooms',
                 labels={'Number of Bedrooms': 'Number of Bedrooms',
                         'Average Price Per Day (SAR)': 'Average Price Per Day (SAR)'},
                 color='Average Price Per Day (SAR)',
                 color_continuous_scale=px.colors.sequential.Viridis,
                 trendline='ols')

fig.update_xaxes(tickvals=[0, 1, 2, 3])
fig.update_layout(
            title_font=dict(size=24),
            margin={"r":0,"t":40,"l":40,"b":0},
            width=1000,
            height=600
)

fig.show()

"""**تأثير الموقع على السعر حسب الحي**"""

price_by_neighborhood = df.groupby('neighborhood')['PricePerDay'].mean().reset_index()

price_by_neighborhood.columns = ['Neighborhood', 'Average Price Per Day (SAR)']

price_by_neighborhood = price_by_neighborhood.sort_values(by='Average Price Per Day (SAR)', ascending=False)

print(price_by_neighborhood)

fig = px.bar(price_by_neighborhood,
             x='Neighborhood',
             y='Average Price Per Day (SAR)',
             title='Average Price Per Day by Neighborhood in Riyadh',
             labels={'Average Price Per Day (SAR)': 'Average Price Per Day (SAR)', 'Neighborhood': 'Neighborhood'},
             color='Average Price Per Day (SAR)',
             color_continuous_scale=px.colors.sequential.Plasma)

fig.update_layout(
            xaxis_title='Neighborhood',
            yaxis_title='Average Price Per Day (SAR)',
            xaxis_tickangle=-45,
            width=1000,
            height=600,
            margin={"r":0,"t":40,"l":0,"b":0}
)

fig.show()

"""
**توزيع عقارات AirBnb**


"""

point = {
    'lat': 24.797789840045454,
    'lon': 46.65281004315909
}

import plotly.graph_objects as go


landmarks_df = pd.DataFrame(landmarks).T.reset_index()
landmarks_df.columns = ['Name', 'Latitude', 'Longitude']


fig = px.scatter_mapbox(df,
                         lat="latitude",
                         lon="longitude",
                         color="TotalPrice",
                         hover_name="name",
                         hover_data={'rating', 'PricePerDay'},
                         zoom=11,
                         center=point,
                         mapbox_style="open-street-map",
                         title='Geographic Distribution of Airbnb Listings in Riyadh with Prominent Landmarks and Pricing')


fig.add_trace(go.Scattermapbox(
    lat=landmarks_df['Latitude'],
    lon=landmarks_df['Longitude'],
    mode='markers+text',
    marker=dict(size=10, color='red'),
    text=landmarks_df['Name'],
    textposition="top center",
    name='Landmarks'
))


fig.update_layout(
    margin={"r": 0, "t": 60, "l": 0, "b": 0},
    title_font=dict(size=24),
    legend=dict(title_font_size=16, orientation="h", yanchor="bottom", y=1, xanchor="right", x=1.09)
)

fig.show()

"""
**الخدمات والتقييم**"""

df['amenities_list'] = df['previewAmenities'].str.split(',')

cleaned_amenities = [amenity.strip() for amenity in df['previewAmenities'].str.cat(sep=',').split(',')]
amenity_counts = pd.Series(cleaned_amenities).value_counts()

top_amenities = amenity_counts.head(10).reset_index()
top_amenities.columns = ['Amenity', 'Count']

average_ratings = {}

for amenity in top_amenities['Amenity']:
    average_rating = df.loc[df['amenities_list'].apply(lambda x: amenity in x), 'rating'].mean()
    average_ratings[amenity] = average_rating


top_amenities['Average Rating'] = top_amenities['Amenity'].map(average_ratings)


print(top_amenities)

fig = px.bar(top_amenities,
             x='Amenity',
             y='Count',
             title='Impact of Amenities on Guest Ratings',
             labels={'Average Rating': 'Average Rating', 'Amenity': 'Amenities'},
             color='Average Rating',
             color_continuous_scale=px.colors.sequential.Plasma,
             text='Average Rating')

fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

fig.update_layout(
    xaxis_title='Amenities',
    yaxis_title='Count',
    xaxis_tickangle=-45,
    width=1000,
    height=600,
    margin={"r":0, "t":40, "l":0, "b":0}
)

fig.show()

"""**السعر والتقييم**

How is the daily rental price related to guest ratings in the Airbnb market?
"""

average_price_by_rating = df.groupby('rating')['PricePerDay'].mean().reset_index()

print(average_price_by_rating)

fig = px.scatter(df,
                 x='rating',
                 y='PricePerDay',
                 title='Relationship Between Ratings and Price Per Day',
                 labels={'rating': 'Guest Ratings', 'PricePerDay': 'Price Per Day(SAR)'},
                 color='PricePerDay',
                 color_continuous_scale=px.colors.sequential.Viridis,
                 trendline='ols')

fig.update_layout(title_font=dict(size=24),
                  width=1000,
            height=600,
                  margin={"r":0, "t":40, "l":40, "b":0})

fig.show()

"""**تأثير سياسات الإلغاء بالتقييم**

How do cancellation policies affect tenant behavior and ratings?
"""

cancel_policy_summary = df.groupby('cancelPolicy').agg(
    count=('cancelPolicy', 'size'),
    average_rating=('rating', 'mean')
).reset_index()

name_mapping = {
    'CANCEL_FLEXIBLE': 'Flexible Cancellation',
    'CANCEL_MODERATE': 'Moderate Cancellation',
    'CANCEL_STRICT_14_WITH_GRACE_PERIOD': 'Strict Cancellation (14 Days Grace)',
    'CANCEL_BETTER_STRICT_WITH_GRACE_PERIOD': 'Better Strict Cancellation (Grace Period)'
}
cancel_policy_summary['cancelPolicy'] = cancel_policy_summary['cancelPolicy'].map(name_mapping)


cancel_policy_summary

fig = px.bar(
    cancel_policy_summary,
    x='cancelPolicy',
    y='count',
    title='Impact of Cancellation Policies on Tenant Behavior',
    labels={'count': 'Number of Rentals', 'cancelPolicy': 'Cancellation Policy'},
    color='average_rating',
    color_continuous_scale=px.colors.sequential.Plasma,
    text='average_rating')

fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')


fig.update_layout(
    xaxis_title='Cancellation Policy',
    yaxis_title='Number of Rentals',
    width=1000,
            height=600,
    margin={"r":0, "t":40, "l":0, "b":0}
)


fig.show()

"""**أعلى الاحياء تقييم**"""

average_ratings = df.groupby(['neighborhood'], as_index=False)['rating'].mean().sort_values(by='rating', ascending=False)
highest_rating_neighborhood = average_ratings.loc[average_ratings['rating'].idxmax()]

print(average_ratings)
print(f"The neighborhood with the highest average rating is {highest_rating_neighborhood['neighborhood']} with an average rating of {highest_rating_neighborhood['rating']}.")

average_ratings = average_ratings.dropna()
fig = px.bar(average_ratings,
             x='neighborhood',
             y='rating',
             title='Average Ratings by Neighborhood',
             labels={'rating': 'Average Rating', 'neighborhood': 'Neighborhood'},
             color='rating',
             color_continuous_scale=px.colors.sequential.Plasma)

fig.update_layout(
    width=1000,
            height=600,
    margin=dict(t=50, l=25, r=25, b=25))

fig.show()

"""**توزيع العقارات حسب أحياء في الرياض**"""

top_neighborhoods = df['neighborhood'].value_counts().head(10).index
room_type_counts = df[df['neighborhood'].isin(top_neighborhoods)].groupby(['city_quarter','neighborhood','type']).size().reset_index(name='count')

print(room_type_counts)

fig = px.treemap(room_type_counts, path=['city_quarter','neighborhood', 'type'],
                 values='count',
                 title='Distribution of Rental Types by City Quarter and Neighborhood',
                color_discrete_sequence=px.colors.sequential.Viridis)

fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    title_font=dict(size=24),
    font=dict(size=12)
)
fig.show()