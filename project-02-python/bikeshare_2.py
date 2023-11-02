import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTHS = ('january', 'february', 'march', 'april', 'may', 'june')

WEEKDAYS = ('monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday')


def choice(question, options):
    while True:
        answer = input(question).lower().strip()
        if answer == 'exit':
            raise SystemExit
        elif ',' in answer:
            answer = [x.strip().lower() for x in answer.split(',')]
            if list(filter(lambda x: x in options, answer)) == answer:
                break
        elif ',' not in answer:
            if answer in options:
                break

        question = 'Please enter a valid option: '

    return answer


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    print('Please enter exit if you want to exit program.')

    while True:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = choice(
            'Would you like to see data for Chicago, New York City, Washington?\n', CITY_DATA.keys())

        # get user input for month (all, january, february, ... , june)
        month = choice(
            'Which month? January, February, March, April, May, June?\n', MONTHS)

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = choice(
            'Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?\n', WEEKDAYS)

        confirm = choice(
            'You want to see data for {} in {} on {}?\n'.format(city, month, day), ('yes', 'no'))

        if confirm == 'yes':
            break
        else:
            print('Please try again.')

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

    print("=================== Loading data... ===================")
    start_time = time.time()

    # filter by city if applicable
    # check if city is a list or not
    if isinstance(city, list):
        df = pd.concat(map(lambda city: pd.read_csv(
            CITY_DATA[city]), city), sort=True)
        # reorganize DataFrame columns after a city concat
        try:
            df = df.reindex(columns=['Unnamed: 0', 'Start Time', 'End Time',
                                     'Trip Duration', 'Start Station',
                                     'End Station', 'User Type', 'Gender',
                                     'Birth Year'])
        except:
            pass
    else:
        df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    # check if month is a list or not
    if isinstance(month, list):
        df = pd.concat(map(lambda month: df[df['Month'] ==
                           (MONTHS.index(month)+1)], month))
    elif month != 'all':
        df = df[df['Month'] == MONTHS.index(month) + 1]

    # filter by day of week if applicable
    # check if day is a list or not
    if isinstance(day, list):
        df = pd.concat(map(lambda day: df[df['Weekday'] ==
                           (day.title())], day))
    elif day != 'all':
        df = df[df['Day'] == day.title()]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    # display the most common day of week

    # display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # show df
        print(df.to_string())

        # time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
