import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. How many people of each race are represented in this dataset? 
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = ((df['education'] == 'Bachelors').mean() * 100).round(1)

    # 4. What percentage of people with advanced education make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = ((df[advanced_education]['salary'] == '>50K').mean() * 100).round(1)

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = ~advanced_education
    lower_education_rich = ((df[lower_education]['salary'] == '>50K').mean() * 100).round(1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = ((num_min_workers['salary'] == '>50K').mean() * 100).round(1)

    # 8. What country has the highest percentage of people that earn >50K?
    countries_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    countries_total = df['native-country'].value_counts()
    highest_earning_country_percentage = (countries_count / countries_total * 100).max().round(1)
    highest_earning_country = (countries_count / countries_total).idxmax()

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print("Min work time:", min_work_hours, "hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
