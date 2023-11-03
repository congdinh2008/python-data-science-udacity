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
    """
    Asks user to specify a city, month, and day to analyze.

    Args:
        question - question to ask user
        options - list of options to check user input

    Returns:
        answer - user input
    """
    while True:
        answer = input(question).lower().strip()
        if answer == 'exit':
            raise SystemExit
        # check if answer contains all
        elif 'all' in answer:
            # if answer contains all, return all options
            # list all options in a string
            options = ', '.join(options)
            answer = options.split(', ')
            break
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
            'Would you like to see data for Chicago, New York City, Washington or "all" to apply no city filter?\n', CITY_DATA.keys())

        # get user input for month (all, january, february, ... , june)
        month = choice(
            'Which month? January, February, March, April, May, June or "all" to apply no month filter?\n', MONTHS)

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = choice(
            'Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or "all" to apply no day filter?\n', WEEKDAYS)

        confirm = choice(
            'You want to see data for {} in {} on {}?\nEnter [y]yes or [n]no:\n'.format(city, month, day), ('y', 'n'))

        if confirm == 'y':
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
    else:
        df = df[df['Month'] == MONTHS.index(month) + 1]

    # filter by day of week if applicable
    # check if day is a list or not
    if isinstance(day, list):
        df = pd.concat(map(lambda day: df[df['Weekday'] ==
                           (day.title())], day))
    else:
        df = df[df['Weekday'] == day.title()]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        None
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mostCommonMonth = df['Month'].mode()[0]
    print('Most common month: {}'.format(MONTHS[mostCommonMonth-1]).title())

    # display the most common day of week
    mostCommonDay = df['Weekday'].mode()[0]
    print('Most common day of week: {}'.format(mostCommonDay))

    # display the most common start hour
    mostCommonHour = df['Start Hour'].mode()[0]
    print('Most common start hour: {}'.format(mostCommonHour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        None
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mostCommonStartStation = str(df['Start Station'].mode()[0])
    print('Most common start station: {}'.format(mostCommonStartStation))

    # display most commonly used end station
    mostCommonEndStation = str(df['End Station'].mode()[0])
    print('Most common end station: {}'.format(mostCommonEndStation))

    # display most frequent combination of start station and end station trip
    mostCommonCombination = df.groupby(
        ['Start Station', 'End Station']).size().idxmax()
    print('Most common combination of start station and end station trip: {}'.format(
        mostCommonCombination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        None
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totalTravelTime = df['Trip Duration'].sum()
    # Format seconds to days, hours, minutes, and seconds
    totalTravelTime = (str(int(totalTravelTime//86400)) +
                       'd ' +
                       str(int((totalTravelTime % 86400)//3600)) +
                       'h ' +
                       str(int(((totalTravelTime % 86400) % 3600)//60)) +
                       'm ' +
                       str(int(((totalTravelTime % 86400) % 3600) % 60)) +
                       's')

    # Print total travel time
    print('Total travel time: {}'.format(totalTravelTime))

    # display mean travel time
    meanTravelTime = df['Trip Duration'].mean()
    # Format seconds to days, hours, minutes, and seconds
    meanTravelTime = (str(int(meanTravelTime//60)) + 'm ' +
                      str(int(meanTravelTime % 60)) + 's')
    # Print mean travel time
    print('Mean travel time: {}'.format(meanTravelTime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """
    Displays statistics on bikeshare users.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        city - Name of the city to analyze
    Returns:
        None
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    stats = {}

    # Display counts of user types
    countOfUserTypes = df['User Type'].value_counts().to_string()
    print('Count of user types: {}'.format(countOfUserTypes))

    # Display counts of gender
    if 'Gender' in df.columns:
        countOfGender = df['Gender'].value_counts().to_string()
        print('Count of user gender: {}'.format(countOfGender))
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the {} city.'.format(
            city.title()))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliestYearOfBirth = int(df['Birth Year'].min())
        print('Earliest year of birth: {}'.format(earliestYearOfBirth))

        mostRecentYearOfBirth = int(df['Birth Year'].max())
        print('Most recent year of birth: {}'.format(mostRecentYearOfBirth))

        mostCommonYearOfBirth = int(df['Birth Year'].mode()[0])
        print('Most common year of birth: {}'.format(mostCommonYearOfBirth))
    else:
        print('Birth year stats cannot be calculated because Birth Year does not appear in the {} city.'.format(
            city.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Create a menu to allow the user to choose menu the below options to filter the data
        # 1. Display raw data
        # 2. Time stats
        # 3. Station stats
        # 4. Trip duration stats
        # 5. User stats
        # 6. Restart
        # 7. Exit

        while True:
            menu = choice(
                '\nPlease choose one of the options below:\n'
                '1. Display raw data\n'
                '2. Time stats\n'
                '3. Station stats\n'
                '4. Trip duration stats\n'
                '5. User stats\n'
                '6. Restart\n'
                '7. Exit\n', ('1', '2', '3', '4', '5', '6', '7'))
            if menu == '1':
                numberOfRow = input('How many rows do you want to display?\n')
                print(df.head(int(numberOfRow)).to_string())
            elif menu == '2':
                time_stats(df)
            elif menu == '3':
                station_stats(df)
            elif menu == '4':
                trip_duration_stats(df)
            elif menu == '5':
                user_stats(df, city)
            elif menu == '6':
                break
            elif menu == '7':
                raise SystemExit
            else:
                print('Please enter a valid option.')

        restart = input(
            '\nWould you like to restart? Enter [y]yes or [n]no.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
    main()
