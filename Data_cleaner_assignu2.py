raw_data = [" 80 ", "95", " 70", "100 ", " 60"]
new_clean_data = [int(data.strip()) for data in raw_data]
print(new_clean_data)