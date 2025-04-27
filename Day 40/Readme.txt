1. data_manager.py:
This file likely contains the DataManager class. It is responsible for interacting with data, such as fetching destination data and updating destination codes in Google Sheets or a database. Here's a breakdown of what might be in this file:

Key functions and their purposes:
get_destination_data():

Fetches destination data from a Google Sheet or other database. This data includes information like the city name, its IATA code (airport code), and the lowest price of flights for that destination.

update_destination_codes():

Updates the IATA codes in the destination data sheet. If the sheet doesn't contain the correct codes, this function ensures they get updated by calling external APIs like FlightSearch to find the IATA codes.

get_customer_emails():

Retrieves customer emails from the sheet or database. These are the people who will receive notifications about flight deals.

2. flight_search.py:
This file contains the FlightSearch class, which interacts with a flight API to check flight availability and prices. Here's an overview of what it does:

Key functions and their purposes:
get_destination_code(city_name):

Takes a city name (e.g., "London") as input and returns the IATA code for the airport (e.g., "LON") by querying a flight API or database.

check_flights(origin, destination, from_time, to_time, is_direct=True):

Searches for available flights based on the given parameters:

origin: The origin airport (e.g., London).

destination: The destination airport (e.g., New York).

from_time: The start date to search for flights.

to_time: The end date to search for flights.

is_direct: Boolean flag to indicate whether the flight should be direct or can include stopovers.

This function interacts with the flight API to fetch flight details based on the parameters.

3. flight_data.py:
This file contains utility functions for processing flight data, such as finding the cheapest flight from the list of available flights. It could have the following functions:

Key functions and their purposes:
find_cheapest_flight(flights):

Takes a list of flight objects (whether direct or indirect) and finds the flight with the lowest price.

This function processes the list of flights and returns the one with the cheapest fare, making it easy to send notifications for the best deal.

4. notification_manager.py:
This file is responsible for sending notifications to users (via email, WhatsApp, or SMS). It would likely contain the NotificationManager class, which handles all the different communication channels.

Key functions and their purposes:
send_sms(message_body):

Sends an SMS to a phone number with the content of message_body. It might use an SMS API like Twilio to send the messages.

send_whatsapp(message_body):

Similar to send_sms(), but sends the message via WhatsApp. Again, this likely uses the Twilio WhatsApp API or another service.

send_emails(email_list, email_body):

Sends emails to a list of email addresses. The email_body contains the flight deal message, and it is sent to everyone in the email_list.

File Interactions and Flow:
Now that we've looked at the individual files, let's discuss how these files interact with each other:

Main Script (the one you shared in the beginning):

Starts by initializing instances of DataManager, FlightSearch, and NotificationManager.

It then fetches destination data from the DataManager using get_destination_data().

For each destination, it uses FlightSearch to find available flights.

The flights are processed using the find_cheapest_flight function from flight_data.py.

If a flight deal is found that is lower than the current lowest price for that destination, it triggers notifications via WhatsApp and email using the methods from NotificationManager.

DataManager:

Handles retrieving and updating data from Google Sheets (or another data source). It’s mainly responsible for managing the destination data and customer emails.

FlightSearch:

Interacts with flight APIs to search for available flights. It handles both direct and indirect flight searches.

FlightData:

This file focuses on processing the flight data returned by the FlightSearch. It extracts the cheapest flight from the list of flights, which is then used to trigger notifications.

NotificationManager:

Once a cheap flight is found, NotificationManager is responsible for sending notifications to customers via email, SMS, or WhatsApp.

