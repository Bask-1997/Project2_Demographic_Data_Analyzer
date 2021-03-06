import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    adult = pd.read_csv('adult.data.csv')
    df = pd.DataFrame(adult)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_unique = df['race'].unique()
    count_race_data = [df[df['race'] == race_unique[0]].count()[0],
    df[df['race'] == race_unique[1]].count()[0],
    df[df['race'] == race_unique[2]].count()[0],
    df[df['race'] == race_unique[3]].count()[0],
    df[df['race'] == race_unique[4]].count()[0]]
    race_count = pd.Series(count_race_data, index= race_unique)


    # What is the average age of men?
    men_age = df.loc[df['sex'] == 'Male']
    average_age_men = men_age['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bachelor_df = df.loc[df['education']=='Bachelors']
    bachelor_count = bachelor_df.count()[0]
    percentage_bachelors = (bachelor_count/df.count()[0])*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    adv_ed_df = df.loc[(df['education'] == 'Bachelors') | 
    (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    adv_more50k_df = adv_ed_df.loc[df['salary'] == '>50K']
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    #Higher education
    higher_education = (adv_ed_df.count()[0]/df.count()[0])*100
    #lower education
    lower_education = ((df.count()[0] - adv_ed_df.count()[0])/df.count()[0])*100
    # percentage with salary >50K
    #Higher_ed_rich
    higher_education_rich = (adv_more50k_df.count()[0]/df.count()[0])*100
    #Lower_ed_rich
    lower_education_rich = ((df.count()[0]-adv_more50k_df.count()[0])/df.count()[0])*100
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[(df['hours-per-week'] == 1) & df['salary'] == '>50K']
    rich_percentage = (num_min_workers.count()[0]/df.count()[0])*100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

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
