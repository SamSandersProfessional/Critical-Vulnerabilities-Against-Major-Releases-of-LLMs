import requests
import json
import re
import time
import nvdlib

# Initialise the APIClient. The API key allows the program to export 50 queries per 30 seconds instead of 5.
client = nvdlib.searchCVE(pubStartDate = '2026-01-01 00:00', pubEndDate = '2026-03-28 00:00', cvssV3Severity='CRITICAL', key='*************', delay=0.6)

for eachCVE in client:
    print(eachCVE.published)      # Output the query
print("end")                      # Tells the program the query completed.
