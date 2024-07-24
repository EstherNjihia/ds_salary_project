import pandas as pd
import glassdoor_scraper as gds

path = "D:/Data_Projects/ds_salary_project/chromedriver"


df  = gds.get_jobs("data scientist", 5, False, path, 15)
