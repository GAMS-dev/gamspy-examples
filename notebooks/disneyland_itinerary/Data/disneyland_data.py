import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, time
import pytz
import os
import time as time_module

def fetch_ride_wait_times():
    # URL of the webpage with the Disneyland ride wait times
    url = 'https://wdwpassport.com/wait-times/magic-kingdom'

    # Set the timezone for Orlando
    orlando_tz = pytz.timezone('America/New_York')

    # Get the current time in Orlando
    crawl_time = datetime.now(orlando_tz).strftime('%Y-%m-%d %H:%M')

    # Send a GET request to the website to fetch the HTML content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # List to store the ride names and wait times
        rides_data = []

        # Find all the list items with the ride and wait time information
        rides_list = soup.find_all('li', class_='relative flex items-center justify-between border-b border-gray-200 px-4 py-2 last:border-b-0')

        # Loop through each ride entry and extract the ride name and wait time
        for ride_item in rides_list:
            # Extract the ride name (inside <h3> tag)
            ride_name = ride_item.find('h3', class_='relative z-10 mr-4 text-sm font-medium leading-tight').text.strip()
            
            # Extract the regular wait time (for most rides)
            wait_time_div = ride_item.find('div', class_='inline-flex h-8 w-8 items-center justify-center rounded-full bg-teal-200 font-medium text-teal-800')
            
            # Special case for Tiana's Bayou Adventure wait time format
            special_wait_time_div = ride_item.find('div', class_='ml-1 inline-flex h-8 w-8 items-center justify-center whitespace-nowrap rounded-full bg-teal-200 text-base font-medium text-teal-800')
            
            # Determine which wait time div to use (prefer the special one if it exists)
            if special_wait_time_div:
                wait_time = special_wait_time_div.text.strip()
            elif wait_time_div:
                wait_time = wait_time_div.text.strip()
            else:
                wait_time = 'N/A'  # Handle cases where wait time is missing

            # Append the ride name and wait time to the list
            rides_data.append([ride_name, wait_time])

        # Create a DataFrame from the scraped data
        rides_df = pd.DataFrame(rides_data, columns=['Ride Name', crawl_time])

        # Check if the file already exists
        file_name = 'wait_times.csv'
        if os.path.exists(file_name):
            # Read the existing file
            existing_df = pd.read_csv(file_name)

            # Merge the new data with the existing data based on 'Ride Name'
            merged_df = pd.merge(existing_df, rides_df, on='Ride Name', how='left')

            # Save the updated dataframe
            merged_df.to_csv(file_name, index=False)
            print(f"Updated wait times for {crawl_time}.")
        else:
            # Create a new file with the current data
            rides_df.to_csv(file_name, index=False)
            print(f"Created a new wait times file for {crawl_time}.")
        
        return rides_df

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

if __name__ == '__main__':
    # Define the Orlando timezone
    orlando_tz = pytz.timezone('America/New_York')

    while True:
        # Get the current time in Orlando
        current_time_orlando = datetime.now(orlando_tz).time()
        
        # Define park open and close times
        park_open_time = time(7, 00)  # Park opens at 07:00 AM
        park_close_time = time(0, 30)  # Park closes at 23:30 PM (next day)
        # fetch_ride_wait_times()

        # Check if the current time is within the park's operating hours
        if (park_open_time <= current_time_orlando <= time(23, 59)) or (time(0, 0) <= current_time_orlando <= park_close_time):
        # if (park_open_time <= current_time_orlando <= park_close_time):
            fetch_ride_wait_times()  # Fetch and save wait times
        else:
            print("Park is closed. Skipping fetch.", current_time_orlando)
        
        # Sleep for 5 minutes (300 seconds)
        time_module.sleep(300)