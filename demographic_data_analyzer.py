import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv", header=None, skipinitialspace=True)

    df.columns = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week",
        "native-country", "salary"
    ]

    # Convert numeric columns to numbers
    numeric_columns = [
        "age", "fnlwgt", "education-num",
        "capital-gain", "capital-loss", "hours-per-week"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Number of each race
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    # Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # Advanced education
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    lower_education = ~higher_education

    # Percentage of advanced education earners >50K
    higher_education_rich = round(
        (df.loc[higher_education, "salary"] == ">50K").mean() * 100, 1
    )

    # Percentage of non-advanced education earners >50K
    lower_education_rich = round(
        (df.loc[lower_education, "salary"] == ">50K").mean() * 100, 1
    )

    # Minimum hours worked
    min_work_hours = df["hours-per-week"].min()

    # People working minimum hours
    num_min_workers = df["hours-per-week"] == min_work_hours

    rich_percentage = round(
        (df.loc[num_min_workers, "salary"] == ">50K").mean() * 100, 1
    )

    # Country with highest percentage earning >50K
    country_data = df.groupby("native-country")["salary"].apply(
        lambda x: (x == ">50K").mean() * 100
    )

    highest_earning_country = country_data.idxmax()
    highest_earning_country_percentage = round(
        country_data.max(), 1
    )

    # Most popular occupation in India earning >50K
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: "
            f"{higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: "
            f"{lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: "
            f"{rich_percentage}%"
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            f"Highest percentage of rich people in country: "
            f"{highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }