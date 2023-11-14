import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
# urllib is for control flow changes and URLError for error massage handling

streamlit.title('My Mom\'s new Healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado tost')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas
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

# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)
# import requests

# New way to display with try expect with nested if else
"""streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please enter a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalize)
except URError as e:
  stramlit.error()"""

#  we will move several lines of code into a little group of code called a function.

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalize

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please enter a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(this_fruit_choice)
    streamlit.dataframe(back_from_function)
except URError as e:
  stramlit.error()

  
  


# streamlit.text(fruityvice_response) --this one just show the line as text forma 

#let's normalize little more this response

#fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalize) 

# import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
 # my_data_row = my_cur.fetchone() - it will fetch one row
 # streamlit.text("Hello from Snowflake:") - Header will show like hello from snowflake
 # streamlit.text(my_data_row) - '''


streamlit.header("The fruit load list contains:")

# Snowflake related function
def get_fruit_load_least():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
# Add a button to load a fruit
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
  
# Allow the end user to add a fruit to the list

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values('" + new_fruit + "')")
      return "Thanks for adding new Friuit:" + new_fruit


add_my_fruit = streamlit.text_input('View our fruit list - Add your favorites!')
if streamlit.button('Get Fruit load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

#back_from_function = get_fruityvice_data(add_my_fruit)
  #streamlit.text(back_from_function)


      

  

# add_my_fruit = streamlit.text_input('What fruit would you like to add?')


#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)
# adding another text for user feedback
#streamlit.write('Thanks for adding:', add_my_fruit)

#for test this line 
# my_cur.execute("insert into fruit_load_list values('for streamlit')")

#streamlit.stop()'''
