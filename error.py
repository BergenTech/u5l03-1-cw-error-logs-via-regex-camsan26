# chatgpt link: https://chat.openai.com/share/759bce15-9ccc-4720-9c44-3954e75c26ea
import json, csv, re
file_path = "logs.json"
with open(file_path,'r') as file:
    data = json.load(file)
    pattern = r'ERROR'
    matching = []
    for i in data:
        match = re.search(pattern,i['level'],re.IGNORECASE)
        # print(match)
        matching.append(i)
    # print(matching)
with open('logs.csv','w',newline='') as CSV_file:
    fieldnames = ['timestamp','level','message']
    writer = csv.DictWriter(CSV_file,fieldnames=fieldnames)
    writer.writeheader()
    for i in data:
        writer.writerow(i['timestamp'],i['level'],i['message'])
    