import time
import pandas as pd
import numpy as np


CITY_DATA = { 'Chicago': 'chicago.csv',
			'New York City': 'new_york_city.csv',
			'Washington': 'washington.csv' }
# Dictionary to assist function "load_data"
month_index = { 1: 'January',
				2: 'February',
				3: 'March',
				4: 'April',
				5: 'May',
				6: 'June'}
# Begin filtering data
def get_filters():
	print('Hello! Let\'s explore some US bikeshare data!\n')
	print('But first we have to filter the data before you can see anything.')
	print('First, we need to know which city we want to look at.')
	print('Please try to answer as properly as possible.')
	while True:
	# get user input for city
		while True:
			try:
				city_input = input('\nWhich city would you like to explore: Chicago, Washington, or New York City? \n')
				if city_input.lower() == 'chi-town' or city_input.lower() == 'chicago' or city_input.lower() == 'chitown':
					city = 'Chicago'
					print('Ahhh the windy city, good choice!')
					break
				elif city_input.lower() == 'washington' or city_input.lower() == 'dc' or city_input == 'The Nation\'s Capital' or city_input.lower() == 'washington dc':
					city = 'Washington'
					print('A nice choice if it wasn\'t for the current guy living in the White House.')
					break
				elif city_input.lower() == 'new york city' or city_input.lower() == 'nyc' or city_input.lower() == 'new york':
					city = 'New York City'
					print('Time to get into that Empire State of Mind.')
					break
				else:
					print('As much as we should go to "{}", we can\'t.'.format(city_input))
			finally:
				print('\n...Reviewing your choices...\n')


		# get user input for month (all, january, february, ... , june)
		print('Now we have to know which month from January to June, or all.')
		while True:
			try:
				print('January, February, March, April, May, June, or "All"')
				month_input = input('Which month do you want to check out?\n')
				if month_input.lower() == 'january' or month_input.lower() == 'jan':
					month = 'January'
					break
				elif month_input.lower() == 'february' or month_input.lower() == 'feb':
					month = 'February'
					break
				elif month_input.lower() == 'march' or month_input.lower() == 'mar':
					month = 'March'
					break
				elif month_input.lower() == 'april' or month_input.lower() == 'apr':
					month = 'April'
					break
				elif month_input.lower() == 'may':
					month = 'May'
					break
				elif month_input.lower() == 'june' or month_input.lower() == 'jun':
					month = 'June'
					break
				elif month_input.lower() == 'all':
					print('You really want all of it?! Okay...your choice.')
					month = 'All Months'
					break
				else:
					print('"{}" is an invalid month. Let\'s try this again.\n'.format(month_input))
			finally:
				print('\n...Reviewing your choices...\n')


		# get user input for day of week (all, monday, tuesday, ... sunday)
		print('Which day of the week do you wanna view?')
		while True:
			try:
				day_input = input('Select from Sun, Mon, Tues, Wed, Thurs, Fri, Sat, or the whole week:\n')
				if day_input.lower() == 'sunday' or day_input.lower() == 'sun':
					day = 'Sunday'
					break
				elif day_input.lower() == 'monday' or day_input.lower() == 'mon':
					print('I hate Mondays')
					day = 'Monday'
					break
				elif day_input.lower() == 'tuesday' or day_input.lower() == 'tues':
					day = 'Tuesday'
					break
				elif day_input.lower() == 'wednesday' or day_input.lower() == 'wed':
					print('HUMP DAY!!!')
					day = 'Wednesday'
					break
				elif day_input.lower() == 'thursday' or day_input.lower() == 'thurs':
					day = 'Thursday'
					break
				elif day_input.lower() == 'friday' or day_input.lower() == 'fri':
					day = 'Friday'
					break
				elif day_input.lower() == 'saturday' or day_input.lower() == 'sat':
					day = 'Saturday'
					break
				elif day_input.lower() == 'all' or day_input.lower() == 'the whole week':
					print('You seriously want the whole week?!')
					day = 'The Whole Week'
					break
				else:
					print('{} is not even close to being a day of the week. Try again.'.format(day_input))
			finally:
				print('\n...Reviewing your choices...\n')

		print('~'*80)
		print('Just to recap. Your choices are as follows: {0}, {1}, and {2}'.format(city, month, day))
		recap = input('Are you sure about these choices? Enter yes or no.\n')
		if recap.lower() == 'yes' or recap.lower() == 'y' or recap == '':
			print('Choices confirmed\n')
			print('~'*80)
			break
	return city, month, day

# Create dataframe from user input
def load_data(city, month, day):
	df = pd.read_csv(CITY_DATA[city])
	# convert to datetime
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	df['End Time'] = pd.to_datetime(df['End Time'])
	# get the month and day
	df['month'] = df['Start Time'].dt.month
	df['day'] = df['Start Time'].dt.day_name()
	# filter by month
	if month != 'All Months':
		months = ['January', 'February', 'March', 'April', 'May', 'June'] #Here in the months list, January is index 0
		month = months.index(month) + 1 #then its index gets updated by +1 to match the df['month']
		df = df[df['month'] == month]
	# filter by day
	if day != 'The Whole Week':
		df = df[df['day'] == day.title()]

	return df

# Displays user statistics
def user_stats(city, df):
	# stats of user type
	print('\n***We will now display User Statistics***\n')
	ans = input('Do you wanna see statistics about "User Type"? Enter yes or no.\n')
	if ans.lower() == 'yes' or ans.lower() == 'y':
		start_time = time.time()
		user = df.groupby(['User Type']).size()
		print('The counts for regular Customers vs Subscribers bike users:\n', user)
		print("\nThis took %s seconds to execute." % (time.time() - start_time))
		print('~'*80)
	# This gives additional stats for the cities Chicago and NYC
	# Statistics in gender and birthyear
	if city == 'New York City' or city == 'Chicago':
		print('BONUS: Since you selected {} as the city, here are some additional statistics.\n'.format(city))
		ans = input('Do you wanna see statistics about "Gender"? Enter yes or no.\n')
		if ans.lower() == 'yes' or ans.lower() == 'y':
			start_time = time.time()
			gender = df.groupby(['Gender']).size()
			print('The counts for Male vs Female bike users:\n',gender)
			print("\nThis took %s seconds to execute." % (time.time() - start_time))
			print('~'*80)
		
		ans = input('Do you wanna see statistics about "Birth Year & Age"? Enter yes or no.\n')
		if ans.lower() == 'yes' or ans.lower() == 'y':
			start_time = time.time()
			df['Age'] = 2020 - df['Birth Year']
			avg_age = df['Age'].mean()
			print('The average age of bikers in {} is {:.5f} years-old.'.format(city, avg_age))
			print('\nThe oldest rider, thus far, is {} years-old.'.format(int(df['Age'].max()))) # the oldest goes over 120!?
			print('\nThe youngest rider, thus far, is {} years-old.'.format(int(df['Age'].min()))) # apparently one of the bike users is 4 yrs old?
			print('\nThe most common age that use the bikes: \n', df['Age'].value_counts().head(1))
			print("\nThis took %s seconds to execute." % (time.time() - start_time))
			print('~'*80)
	return

# calculates time related stats
def time_stats(df):
	print('\n***We will now display Time-related Statistics***\n')
	ans = input('Do you wanna see statistics about "Start Time or End Time"? Enter yes or no.\n')
	if ans.lower() == 'yes' or ans.lower() == 'y':
		start_time = time.time()
		#find most common month
		common_month = df['month'].mode()[0]
		if common_month in month_index:
			print('\nThe most common month is', month_index[common_month])
		#find most common day
		common_day = df['day'].mode()[0]
		print('\nThe most common day is', common_day)
		# find common start of the trip
		df['hour'] = df['Start Time'].dt.hour
		common_hour = df['hour'].mode()[0]
		print('\nThe most common start hour for a trip is', common_hour)
		print("\nThis took %s seconds to execute." % (time.time() - start_time))
		print('~'*80)
	return

# calculates stats using the trip duration column
def trip_duration_stats(df):
	# make sure no trip duration are in floats
	df[("Trip Duration")] = df["Trip Duration"].fillna(0.0).astype(int)
	print('\n***We will now display Trip Duration Statistics***\n')
	ans = input('Do you wanna see statistics about "Trip Duration"? Enter yes or no.\n')
	if ans.lower() == 'yes' or ans.lower() == 'y':
		start_time = time.time()
		# finds total time duration
		total_time = df['Trip Duration'].sum()
		print('The total amount of travel time is', total_time,'seconds')
		print('OR', total_time/60, 'minutes')
		print('OR', total_time/3600, 'hours')
		print()
		# finds average trip time
		mean_time = df['Trip Duration'].mean()
		print('The average for travel time is', mean_time,'seconds')
		print('OR', mean_time/60, 'minutes')
		print("\nThis took %s seconds to execute." % (time.time() - start_time))
		print('~'*80)
	return

# finds station related statistics
def station_stats(df):
	print('\n***We will now display Station Statistics***\n')
	ans = input('Do you wanna see the most common "Start Station"? Enter yes or no.\n')
	if ans.lower() == 'yes' or ans.lower() == 'y':
		start_time = time.time()
		# finds common start station
		common_start = df.groupby(['Start Station']).size().sort_values(ascending=False).index[0]
		print('The most common Start Station is', common_start)
		print("\nThis took %s seconds to execute." % (time.time() - start_time))
		print('~'*80)
	ans = input('Do you wanna see the most common "End Station"? Enter yes or no.\n')
	if ans.lower() == 'yes' or ans.lower() == 'y':
		start_time = time.time()
		#finds common end station
		common_end = df.groupby(['End Station']).size().sort_values(ascending=False).index[0]
		print('The most common Start Station is', common_end)
		print("\nThis took %s seconds to execute." % (time.time() - start_time))
		print('~'*80)
	ans = input('Do you wanna see the most common "Start -> End" trip? Enter yes or no.\n')
	if ans.lower() == 'yes' or ans.lower() == 'y':
		# finds common trip
		start_time = time.time()
		t1 = df['Start Station'].copy()
		t2 = df['End Station'].copy()
		df['trip'] = t1.str.cat(t2, sep=" to ")
		common_trip = df.groupby(['trip']).size().sort_values(ascending=False).index[0]
		print('The most common "Start -> End" trip is from', common_trip)
		print("\nThis took %s seconds to execute." % (time.time() - start_time))
		print('~'*80)
	return

# helps with printing 5 rows at a time
def print_df(df2):
	count = 0
	print('\n***We will now print out a few rows of raw data***')
	d = df2.to_dict('records') #turns each row in dataframe into a dictionary which is then put into a large list containing these dictionaries
	while True:
		start_time = time.time()
		ans = input('\nEnter yes(y) or press the enter key to scroll through raw data. Otherwise, enter no(n): ')
		if ans.lower() == 'yes' or ans.lower() == 'y' or ans == '':
			print('\nPrinting rows...')
			#I am sure there is a better way to execute this but this will do for now
			print(d[count])
			print(d[count+1])
			print(d[count+2])
			print(d[count+3])
			print(d[count+4])
			count += 5
		elif ans.lower() == 'no' or ans.lower() == 'n':
			print("\nYou looked at raw data for %s seconds." % (time.time() - start_time))
			print('~'*80)
			break
		else:
			print('INVALID INPUT')


def main():
	while True:
		city, month, day = get_filters()
		df = load_data(city, month, day) # df2 is to help print out rows 5 at a time and is the original dataframes without additional columns
		df2 = df.copy()
		df2 = df2.rename(columns={'Unnamed: 0':'ID'}) #rename one of the columns to a better name
		df2.pop('day') # removes the filters created from get_filters()
		df2.pop('month') #removed

		time_stats(df)
		station_stats(df)
		trip_duration_stats(df)
		user_stats(city, df)
		print_df(df2)

		print('~'*80)
		print('Just to recap. You looked at stats with these filters: {0}, {1}, and {2}'.format(city, month, day))
		restart = input('\nWould you like to restart? Enter yes or no.\n')
		if restart.lower() == 'no' or restart.lower() == 'n':
			print('Thank you. Come again!')
			break

if __name__ == "__main__":

	main()
