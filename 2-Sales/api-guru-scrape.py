import yaml
import requests
import csv
import time
import datetime
import os  # Import the 'os' module

def extract_openapi_info(yaml_url, provider_name):
    # ... (same as before)
    try:
        response = requests.get(yaml_url)
        response.raise_for_status()

        data = yaml.safe_load(response.content)

        server_description = data.get('servers', [{}])[0].get('description') if data.get('servers') else None
        contact_info = data.get('info', {}).get('contact', {})
        contact_email = contact_info.get('email')
        contact_name = contact_info.get('name')
        contact_url = contact_info.get('url')
        x_origin = data.get('info', {}).get('x-origin', [{}])[0]
        x_origin_url = x_origin.get('url')
        x_provider_name = data.get('info', {}).get('x-providerName')

        extracted_data = {
            'x-provider-name': x_provider_name,
            'server-description': server_description,
            'contact-email': contact_email,
            'contact-name': contact_name,
            'contact-url': contact_url,
            'x-origin-url': x_origin_url,
            'api-guru-yaml-link': yaml_url,
            'provider-name': provider_name,  # Add provider name for tracking
        }

        return extracted_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching YAML for {provider_name} ({yaml_url}): {e}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML for {provider_name} ({yaml_url}): {e}")
        return None
    except KeyError as e:
        print(f"Missing key in YAML data for {provider_name} ({yaml_url}): {e}")
        return None
    except ValueError as e:
        print(f"Value error in YAML data for {provider_name} ({yaml_url}): {e}")
        return None
    

def save_to_csv(data_list, csv_filename):
    if not data_list:
        print("No data to save.")
        return

    fieldnames = ['provider-name', 'x-provider-name', 'server-description', 'contact-email', 'contact-name', 'contact-url', 'x-origin-url', 'api-guru-yaml-link']

    try:
        # Check if the file exists to decide whether to write headers
        write_header = not os.path.exists(csv_filename)

        with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if write_header:
                writer.writeheader()
            writer.writerows(data_list)
        print(f"Data successfully appended to {csv_filename}")

    except (IOError, OSError) as e:
        print(f"Error writing to CSV file: {e}")

if __name__ == "__main__":
    list_url = "https://api.apis.guru/v2/list.json"
    csv_filename = "openapi_info.csv"

    try:
        response = requests.get(list_url)
        response.raise_for_status()
        api_list = response.json()

        extracted_data_list = []
        processed_count = 0
        
        for provider_name, api_data in api_list.items():
            for version, version_data in api_data['versions'].items():
                yaml_url = version_data.get("swaggerYamlUrl") # Note: Some APIs might use "openapi.yaml" instead of "swagger.yaml"
                if yaml_url:
                    info = extract_openapi_info(yaml_url, provider_name)
                    if info:
                        extracted_data_list.append(info)
                    processed_count += 1

                    # Save and print update for every 50 APIs processed
                    if processed_count % 50 == 0:
                        print(f"Processed {processed_count} APIs...")
                        save_to_csv(extracted_data_list, csv_filename)
                        extracted_data_list = []  # Clear the list after saving
                else:
                    print(f"No YAML URL found for {provider_name} version {version}")

            # Optional: Add a small delay to avoid overloading the server
            time.sleep(0.5)

        # Save any remaining data that hasn't been saved yet
        if extracted_data_list:
            save_to_csv(extracted_data_list, csv_filename)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching API list: {e}")

    print(f"Processed a total of {processed_count} APIs.")