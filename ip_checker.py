import requests
import json
import csv
import time
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('ABUSEIPDB_API_KEY')

if not api_key:
    print("[-] Error: API Key not found. Please check your .env file.")
    exit()

url = 'https://api.abuseipdb.com/api/v2/check'
headers = {
    'Accept': 'application/json',
    'Key': api_key
}

csv_file = open('malicious_ips.csv', mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['IP Address', 'Abuse Score (%)', 'Country', 'ISP', 'Total Reports'])

print("[*] Starting IP reputation scan...\n")

try:
    with open('ips.txt', 'r') as file:
        ips = file.readlines()
except FileNotFoundError:
    print("[-] Error: 'ips.txt' file not found.")
    exit()

for ip in ips:
    ip = ip.strip() 
    if not ip:
        continue 
        
    print(f"[*] Checking IP: {ip}")
    querystring = {'ipAddress': ip, 'maxAgeInDays': '90'}
    
    response = requests.get(url=url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = json.loads(response.text)['data']
        
        abuse_score = data['abuseConfidenceScore']
        country = data['countryCode']
        isp = data['isp']
        total_reports = data['totalReports']
        
        csv_writer.writerow([ip, abuse_score, country, isp, total_reports])
        
        time.sleep(1)
    else:
        print(f"[-] Error checking {ip} - Status Code: {response.status_code}")

csv_file.close()
print("\n[+] Scan completed successfully! Results saved in 'malicious_ips.csv'.")