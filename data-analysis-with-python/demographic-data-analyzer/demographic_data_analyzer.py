import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    total_count = df['race'].count()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    no_of_bach = df[df['education'] == 'Bachelors']['race'].count()
    percentage_bachelors = ((no_of_bach * 100) / total_count).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['race'].count()
    higher_education_above50 = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'].isin(['>50K']))]['race'].count()
    
    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))]['race'].count()
    lower_education_above50 = df[~(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'].isin(['>50K']))]['race'].count()

    # percentage with salary >50K
    higher_education_rich = (higher_education_above50 * 100 / higher_education).round(1)
    lower_education_rich = (lower_education_above50 * 100 / lower_education).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]['race'].count()

    rich_percentage = ((df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')]['race'].count()) * 100 / num_min_workers).round(1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_df = df[df['salary'] == '>50K']['native-country'].value_counts()
    all_country_popul = df['native-country'].value_counts()
    highest_earning_country = (highest_earning_country_df / all_country_popul * 100).idxmax()
    highest_earning_country_percentage = (highest_earning_country_df / all_country_popul * 100).max().round(1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    ind_above50_occp = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts()
    top_IN_occupation = ind_above50_occp.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
