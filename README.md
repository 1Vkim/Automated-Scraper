## Price Update and Email Notification Script

This script monitors the price of a product and sends an email notification if the price drops below a desired threshold.

## Requirements

- Python 3.x
- requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- schedule library (`pip install schedule`)
- replit library (`pip install replit`)

### Usage

1. Set up your email credentials as environment variables (`mailPassword` and `mailUsername`).
2. Update the product URL and desired price in the `priceUpdate` function.
3. Run the script.

### Explanation

1. `priceUpdate` function scrapes the product pricing from a specified URL and updates it in the database.
2. The script schedules this function to run daily at midnight to check for price updates.
3. If the current price is lower than the desired price, it triggers the `sendMail` function to send an email notification.

Ensure you have the necessary permissions and configurations set up for sending emails via SMTP.

For detailed usage and customization, refer to the code comments and modify as needed.
