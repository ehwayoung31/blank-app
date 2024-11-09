import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("movies_2024.csv")

# Streamlit app
def main():
    st.title("Budget vs Revenue Analysis")
    st.write("This app visualizes the relationship between budget and revenue of movies.")

    # Display the first few rows of the dataset
    st.write("### Movie Dataset Preview")
    st.write(df.head())

    # Check if 'budget' and 'revenue' columns exist in the dataset
    if 'budget' in df.columns and 'revenue' in df.columns:
        # Scatter plot of budget vs revenue
        st.write("### Budget vs Revenue Scatter Plot")
        fig, ax = plt.subplots()
        ax.scatter(df['budget'], df['revenue'], alpha=0.5)
        ax.set_xlabel('Budget')
        ax.set_ylabel('Revenue')
        ax.set_title('Budget vs Revenue')
        st.pyplot(fig)
    else:
        st.error("The dataset does not contain the required 'budget' and 'revenue' columns.")

if __name__ == "__main__":
    main()
