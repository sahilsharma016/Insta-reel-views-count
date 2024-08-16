import login
from login import driver,time
import pandas as pd
import csv
from selenium.webdriver.support import expected_conditions as EC
from login import By


# Read the Excel file
df = pd.read_excel("modified_excel_file.xlsx")

# import time

# # Group DataFrame by 'account_link'
# grouped = df.groupby('account_link')

# for account_link, group_df in grouped:
#     print("Processing account:", account_link)
#     for index, row in group_df.iterrows():
#         reel_link = row['reel_link']

#         driver.get(reel_link)
#         time_of_upload = login.WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//time[@class='x1p4m5qa']")))
        
#         # Check if the value is within the specified ranges
#         if (time_of_upload.text.endswith("hours ago") and int(time_of_upload.text.split()[0]) in range(1, 25)) \
#                 or (time_of_upload.text.endswith("days ago") and int(time_of_upload.text.split()[0]) in range(1, 6)):
#             print("Opened reel link:", reel_link)
#             # Process further if needed
#         else:
#             print("Time of upload is not within the specified ranges. Breaking for account:", account_link)
#             break  # Breaks the loop for the current account_link
#     time.sleep(3)  # You might want to add a delay between processing different accounts
# import time

# # Group DataFrame by 'account_link'
# grouped = df.groupby('account_link')

# for account_link, group_df in grouped:
#     print("Processing account:", account_link)
#     total_views = 0  # Initialize total views for this account_link
#     for index, row in group_df.iterrows():
#         reel_link = row['reel_link']
#         driver.get(reel_link)
#         time_of_upload = login.WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//time[@class='x1p4m5qa']")))
        
#         # Check if the value is within the specified ranges
#         if (time_of_upload.text.endswith("hours ago") and int(time_of_upload.text.split()[0]) in range(1, 25)) \
#                 or (time_of_upload.text.endswith("days ago") and int(time_of_upload.text.split()[0]) in range(1, 6)):
#             print("Opened reel link:", reel_link)
#             # Process further if needed
#             total_views += row['views']
#         else:
#             print("Time of upload is not within the specified ranges. Breaking for account:", account_link)
#             break  # Breaks the loop for the current account_link
#     print("Total views for", account_link, ":", total_views)
#     time.sleep(3)  # You might want to add a delay between processing different accounts

import pandas as pd
import time

# Load the existing Excel file if it exists, otherwise create an empty DataFrame
try:
    existing_data = pd.read_excel('modified_excel_file.xlsx')
except FileNotFoundError:
    existing_data = pd.DataFrame(columns=['account_link', 'total_views'])

# Group DataFrame by 'account_link'
grouped = df.groupby('account_link')

for account_link, group_df in grouped:
    print("Processing account:", account_link)
    total_views = 0  # Initialize total views for this account_link
    for index, row in group_df.iterrows():
        try:
            reel_link = row['reel_link']
            driver.get(reel_link)
            time_of_upload = login.WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//time[@class='x1p4m5qa']")))
            
            # Check if the value is within the specified ranges
            if (time_of_upload.text.endswith("hours ago") and int(time_of_upload.text.split()[0]) in range(1, 25)) \
                    or (time_of_upload.text.endswith("days ago") and int(time_of_upload.text.split()[0]) in range(1, 6)):
                print("Opened reel link:", reel_link)
                # Process further if needed
                total_views += row['views']
            else:
                print("Time of upload is not within the specified ranges. Breaking for account:", account_link)
                break  # Breaks the loop for the current account_link
        except Exception as e:
            print(f"An error occurred while processing reel link {reel_link}: {str(e)}")
            total_views = 'Error'  # Mark total_views as 'Error' in case of an error
            break  # Breaks the loop for the current account_link
        
    

# Save the updated DataFrame to an Excel file
existing_data.to_excel('total_views.xlsx', index=False)
