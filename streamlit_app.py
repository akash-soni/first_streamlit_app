import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Buttermeal oatmeal')
streamlit.text('Kale, Spinach & Rocket smoothie')
streamlit.text('hard boiled, free-range eggs')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick up some fruits:",list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# streamlit.text("The fruit load list contains:")
# streamlit.text(my_data_row)
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


# Add second input
second_fruit_choice = streamlit.text_input('What fruit would you like to add?','')
streamlit.write('Thanks for adding ', second_fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")