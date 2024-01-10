import streamlit
import pandas
streamlit.title('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Buttermeal oatmeal')
streamlit.text('Kale, Spinach & Rocket smoothie')
streamlit.text('hard boiled, free-range eggs')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick up some fruits:",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
