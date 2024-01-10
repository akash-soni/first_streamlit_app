import streamlit
import pandas
streamlit.title('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Buttermeal oatmeal')
streamlit.text('Kale, Spinach & Rocket smoothie')
streamlit.text('hard boiled, free-range eggs')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
