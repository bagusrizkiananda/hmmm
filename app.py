import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Title
st.title('Netflix Titles Dashboard')

# Show raw data if requested
if st.checkbox('Show Raw Dataset'):
    st.write(df)

# Show basic statistics
st.subheader('Dataset Overview')
st.write(f'Total data: {df.shape[0]} rows, {df.shape[1]} columns')
st.write('Missing values per column:')
st.write(df.isnull().sum())

# Filter by Type
types = df['type'].unique()
selected_type = st.selectbox('Select Content Type', types)
filtered_df = df[df['type'] == selected_type]

st.write(f'Total {selected_type}: {filtered_df.shape[0]}')
st.write(filtered_df.head(10))

# Year Distribution
st.subheader(f'{selected_type} Release Year Distribution')
fig, ax = plt.subplots()
filtered_df['release_year'].value_counts().sort_index().plot(kind='bar', figsize=(15, 5), ax=ax)
plt.xlabel('Release Year')
plt.ylabel('Count')
st.pyplot(fig)

# Country Distribution
st.subheader(f'Top 10 Countries Producing {selected_type}')
fig2, ax2 = plt.subplots()
filtered_df['country'].value_counts().head(10).plot(kind='barh', ax=ax2)
plt.xlabel('Count')
plt.ylabel('Country')
st.pyplot(fig2)

st.caption('Made with ❤️ using Streamlit')
