import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ['chicago', 'new york city', 'washington']
    city = str(input('Enter name of the city you want to examine (chicago, new york city or washington) : ')).lower()
    while True:
        if city not in valid_cities:
            city = str(input('Error, please enter name of the city you want to examine (chicago, new york city or washington) : ')).lower()
        else:
            print('Ok, you selected: ', city)
            break       
            
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = str(input('Specify month to examine (all, january, february, ... , june): ')).lower()
    while True:
        if month not in valid_months:
            month = str(input('Error, please specify correct month to examine or type all: ')).lower()
            break
        else:
            print('Ok, you selected: ', month)
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = str(input('Enter day to examine (all, monday, tuesday, ... sunday): ')).lower()
    while True:
       if day not in valid_days:
        day = str(input('Error, please enter correct day: ')).lower()
        break
       else:
        print('Ok, you selected: ', day)
        break
        

    print('-'*40)
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

     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]
    
    print('The most common month of travel is: ',popular_month)

    # TO DO: display the most common day of week
    df['day of week'] = df['Start Time'].dt.dayofweek
    popular_day_of_week = df['day of week'].mode()[0]
    print('The most common day of week of travel is: ', popular_day_of_week)
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour of travel is: ' , popular_hour)
    
    # Ask user to see raw data until he indicates to stop
    n = 0
    view_data = input('\n Would you like to see the raw data? Enter yes or no:  \n').lower()
    while True:
        if view_data == 'yes':
            print(df.loc[n:n+4])
            n += 5
            continue_data = input('Would you like to continue to see raw data? Enter yes or no please: ').lower()
            if continue_data == 'no':
                break
        else:
            break   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)                

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', popular_start_station) 

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start & End Stations'] = df['Start Station'] + ' and ' + df['End Station']
    popular_comb = df['Start & End Stations'].mode()[0]
    print('The most common combination of start and end stations is: ', popular_comb)
    
   # Ask user to see raw data until he indicates to stop
    n = 0
    view_data = input('\n Would you like to see the raw data? Enter yes or no:  \n').lower()
    while True:
        if view_data == 'yes':
            print(df.loc[n:n+4])
            n += 5
            continue_data = input('Would you like to continue to see raw data? Enter yes or no please: ').lower()
            if continue_data == 'no':
                break
        else:
            break    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Trip Duration'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time is: ', avg_travel_time)
    
    # Ask user to see raw data until he indicates to stop
    n = 0
    view_data = input('\n Would you like to see the raw data? Enter yes or no:  \n').lower()
    while True:
        if view_data == 'yes':
            print(df.loc[n:n+4])
            n += 5
            continue_data = input('Would you like to continue to see raw data? Enter yes or no please: ').lower()
            if continue_data == 'no':
                break
        else:
            break   
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    while True:
        try:
            no_inf = df['Gender'].isna().sum()
            gender = df['Gender'].value_counts()
            print(gender)
            print('Data with no gender assigned: ', no_inf)
            break
        except KeyError:
            print('No data of gender available for this city')
            break          
     
    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:
            earliest_by = df['Birth Year'].min()
            recent_by = df['Birth Year'].max()
            common_by = df['Birth Year'].mode()[0]
            print('The earliest birth year of the users is: ', earliest_by)
            print('The most recent birth year of the users is: ', recent_by)
            print('The most common birth year of the users is: ', common_by)
            break
        except KeyError:
            print('No data of birth year available for this city')
            break
    
   # Ask user to see raw data until he indicates to stop
    n = 0
    view_data = input('Would you like to see the raw data? Enter yes or no: ').lower()
    while True:
        if view_data == 'yes':
            print(df.loc[n:n+4])
            n += 5
            continue_data = input('Would you like to continue to see the raw data? Enter yes or no please: ').lower()
            if continue_data == 'no':
                break
        else:
            break   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
      
        if restart.lower() != 'yes':
            break
  
if __name__ == "__main__":
	main()
                 