import login
from login import driver, WebDriverWait, By
import pandas as pd
import csv
from selenium.webdriver.support import expected_conditions as EC

# Read the Excel file
df = pd.read_excel("modified_excel_file.xlsx")

# Group DataFrame by 'account_link'
grouped = df.groupby('account_link')

# List to store data for new CSV file
new_data = []

with open('view_counts.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
        
    for account_link, group_df in grouped:
        print("Processing account:", account_link)
        total_sum = 0  # Initialize total sum for this account_link
        for index, row in group_df.iterrows():
            try:
                reel_link = row['reel_link']
                driver.get(reel_link)
                time_of_upload = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//time[@class='x1p4m5qa']")))
                
                # Check if the value is within the specified ranges
                if (time_of_upload.text.endswith("hours ago") and int(time_of_upload.text.split()[0]) in range(1, 25)) \
                        or (time_of_upload.text.endswith("days ago") and int(time_of_upload.text.split()[0]) in range(1, 6)) or (time_of_upload.text.endswith("minutes ago") and int(time_of_upload.text.split()[0]) in range(1, 60)) :
                    print("Opened reel link:", reel_link)
                    # Process further if needed
                    total_sum += row['views']
                    
                else:
                    print("Time of upload is not within the specified ranges. Breaking for account:", account_link)
                    break  # Breaks the loop for the current account_link
                
            except Exception as e:
                print(f"An error occurred while processing reel link {reel_link}: {str(e)}")
                total_sum = 'Error'  # Mark total_sum as 'Error' in case of an error
                break  # Breaks the loop for the current account_link
        csv_writer.writerow([account_link, total_sum])
