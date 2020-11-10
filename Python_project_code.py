import pandas as pd
import time
import numpy as np

#here's the dictionary with the keys (cities) and values(csv's files)
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#list of months
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

#list of days
days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

#dataframe = None
df = None
start_loc = 0
#defining the function get_filters that will get city, month and day
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("\nWhat city can I get data for you?: ").lower()
        if city not in CITY_DATA:
            print('\nYour answer is invalid. Please write Chicago, New Work or Washington')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input ("\nPlease enter a month from Jan-Jun you wish to perform analysis for: ").lower()
        if month not in months :
            print ("\nYour answer is invalid. Please write a month from Jan-June")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nPlease enter the day you wish to perform analysis for: ").lower()
        if day not in days:
            print ("\nYour answer is invalid. Please write a day dude, don't make me waste my time")
            continue
        else:
            break

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load the file of the city the user chose
    city_file = CITY_DATA[city]

    #Convert the data into pandas and read the csv
    df = pd.read_csv(city_file)

    #Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Get the month
    df['month'] = df['Start Time'].dt.month

    #get the day
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    print('the city you entered is "{}" and the file Im going to read is: {}'.format(city, city_file))
    print('\n')
    print('-'*40)
    print('\n')

    return df

#this function will tell me which month, day and hour are the most frequent by clients
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('\nMost Common Month:', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day_of_the_week = df['day_of_week'].mode()[0]
    print('\nMost Common Day of the Week:', popular_day_of_the_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#this function will tell me, which are the most frequent stations
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station: ', most_used_start_station)

    # TO DO: display most commonly used end station
    most_used_end_station =  df['End Station'].mode()[0]
    print('\nMost Popular End Station: ', most_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined'] =  df['Start Station'] + 'to' + ['End Station']
    combined_stations = df['Combined'].mode()[0]
    print('\nMost frequent used station between Start and Eng Stations: ', combined_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#this function will let me know, which are the
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nthe amount of total travel are {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean of the travles are: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df.groupby('User Type')['User Type'].count()
    print('\nThe total number of users are: {}'.format(user_type_count))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df.groupby('Gender')['Gender'].count()
        print('\ntotal travel time: ', gender_count)
    else:
        print('\nThere are no columns about gender')

    # TO DO: Display earliest, most recent, and most common year of birth

    #earliest year from the database
    try:
        earliest_year = df['Birth Year'].min()
        print('The earliest year from the database {} is {}'.format(city, earliest_date))
    except:
        print('There is no data available for the input you put')

    #most recent year
    try:
        recent_year = df['Birth Year'].max()
        print('The most recent year from the database {} is {}'.format(city, recent_year))
    except:
        print('There is no data available for the input you put')

    #most common year
    try:
        common_year = df['Birth Year'].mode()[0]
        print('The earliest year from the database {} is {}'.format(city, common_year))
    except:
        print('There is no data available for the input you put')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Ask the user if he wants to display the first five rows of data."""

    user_choice = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?:").lower()
    if user_choice in ('yes', 'y'):
        i = 0
        while True:
            print(df.iloc[i:i + 5])
            i += 5
            next_rows = input('Would you like to see more data? Please enter yes or no: ').lower()
            if next_rows not in ('yes', 'y'):
                break

#Main fuction to display the inputs and results to end users
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
