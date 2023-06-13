from parser import parse

import argparse

# Create the argument parser
parser = argparse.ArgumentParser()

# Add the desired command-line argument
parser.add_argument('-format', type=str, help='Specify the format')

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of the 'format' argument
format_value = args.format

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
