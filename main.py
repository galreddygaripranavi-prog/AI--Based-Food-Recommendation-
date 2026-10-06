import streamlit as st
import pandas as pd

# Load food data
food_data = pd.read_csv("food_data.csv")

# Page title
st.title("🍎 AI-Based Food Recommendation System")

st.write(
    "Get food recommendations and check nutrition information."
)

# Menu
option = st.sidebar.radio(
    "Choose an option",
    [
        "Food Recommendation",
        "Nutrition Analysis"
    ]
)


# --------------------------------
# FOOD RECOMMENDATION
# --------------------------------

if option == "Food Recommendation":

    st.header("🥗 Food Recommendation")

    requirement = st.text_input(
        "What type of food do you want?"
    )

    if st.button("Recommend Food"):

        if requirement == "":
            st.warning(
                "Please enter your requirement."
            )

        else:

            requirement = requirement.lower()

            if "protein" in requirement:

                result = food_data.sort_values(
                    by="protein",
                    ascending=False
                )

            elif "low calorie" in requirement:

                result = food_data.sort_values(
                    by="calories"
                )

            elif "fiber" in requirement:

                result = food_data.sort_values(
                    by="fiber",
                    ascending=False
                )

            elif "carbs" in requirement:

                result = food_data.sort_values(
                    by="carbs",
                    ascending=False
                )

            else:

                result = food_data

            st.subheader("Recommended Foods")

            st.dataframe(
                result.head(5),
                use_container_width=True
            )


# --------------------------------
# NUTRITION ANALYSIS
# --------------------------------

else:

    st.header("🔍 Nutrition Analysis")

    food_name = st.text_input(
        "Enter food name"
    )

    if st.button("Analyze Nutrition"):

        if food_name == "":

            st.warning(
                "Please enter a food name."
            )

        else:

            food = food_data[
                food_data["food"].str.lower()
                == food_name.lower()
            ]

            if food.empty:

                st.error(
                    "Food not found."
                )

            else:

                food = food.iloc[0]

                st.success(
                    "Food found!"
                )

                st.write(
                    "### Nutrition Information"
                )

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Calories",
                    f"{food['calories']} kcal"
                )

                col2.metric(
                    "Protein",
                    f"{food['protein']} g"
                )

                col3.metric(
                    "Carbs",
                    f"{food['carbs']} g"
                )

                col4, col5 = st.columns(2)

                col4.metric(
                    "Fat",
                    f"{food['fat']} g"
                )

                col5.metric(
                    "Fiber",
                    f"{food['fiber']} g"
                )
