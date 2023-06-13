from parser import parse

# Main function
def main():
    url = "https://alerts.in.ua"
    alert_class = 'active'
    items = parse(url)

    regions_parsed_arr = []

    for item in items:
        region = item['data-oblast']
        is_alert = alert_class in item['class']
        dictionary = {'region': region, 'alert': is_alert}
        if(not (dictionary in regions_parsed_arr)):
            regions_parsed_arr.append(dictionary)

    for item in regions_parsed_arr:
        print(item)
            

if __name__ == "__main__":
    main()
