import streamlit
streamlit.title('My Mom\'s new Healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado tost')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruits_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruits_list)
my_fruits_list=my_fruits_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:",list(my_fruits_list.index))

# Display the table on the page
streamlit.dataframe(my_fruits_list)

#Let's put a pick list here so they can pickup the fruit they want to include

#streamlit.multiselect("pick some fruits:",list(my_fruits_list.index),['Avocado','Strawberries'])


#Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruits_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected]

# display the table on the page
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# streamlit.text(fruityvice_response) --this one just show the line as text forma 

#let's normalize little more this response

fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalize) 

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone() - it will fetch one row
# streamlit.text("Hello from Snowflake:") - Header will show like hello from snowflake
# streamlit.text(my_data_row) - 
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
# adding another text for user feedback
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('The user entered ', add_my_fruit)
