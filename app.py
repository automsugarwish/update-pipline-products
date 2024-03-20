import requests

def get_product_name(product_id, headers):
    # Define the API endpoint to get product details
    endpoint = f"https://api.na1.insightly.com/v3.1/Product/{product_id}"
    
    # Make the GET request to fetch product details
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        product_data = response.json()
        print(product_data)
        return product_data.get("PRODUCT_NAME")
    else:
        print(f"Error fetching product {product_id}: {response.status_code}")
        return None

def get_product_id(pricebook_entry_id, headers):
    # Define the API endpoint to get product details
    endpoint = f"https://api.na1.insightly.com/v3.1/PricebookEntry/{pricebook_entry_id}"
    
    # Make the GET request to fetch product details
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        product_data = response.json()
        print(product_data)
        return product_data.get("PRODUCT_ID")
    else:
        print(f"Error fetching product {pricebook_entry_id}: {response.status_code}")
        return None

def update_opportunity_custom_fields(opportunity_id, product_names_array, headers):
    # Define the API endpoint to update the opportunity
    endpoint = f"https://api.na1.insightly.com/v3.1/Opportunities/{opportunity_id}"
    
    # Define the payload to update the custom fields
    payload = {
        "OPPORTUNITY_ID": opportunity_id,
        "CUSTOMFIELDS": [
            {
                "FIELD_NAME": "Products__c",
                "FIELD_VALUE": product_names_array
            }
        ]
    }
    
    print(payload)

    # Make the PUT request to update the opportunity
    response = requests.put(endpoint, headers=headers, json=payload)
    
    if response.status_code != 200:
        print(f"Error updating opportunity {opportunity_id}: {response.status_code}")

def get_opportunity_line_items(opportunity_id):
    # Define the API endpoint
    endpoint = f"https://api.na1.insightly.com/v3.1/Opportunities/{opportunity_id}/OpportunityLineItem"
    
    # Set your API key here
    headers = {
        "Authorization": ""
    }
    
    # Make the GET request
    response = requests.get(endpoint, headers=headers)

    product_names_array = []
    
    if response.status_code == 200:
        items = response.json()
        print(items)

        for item in items:
            pricebook_entry_id = item.get("PRICEBOOK_ENTRY_ID")
            print(pricebook_entry_id)
            product_id = get_product_id(pricebook_entry_id, headers)
            print(product_id)
            product_name = get_product_name(product_id, headers)
            print(product_name)

            product_names_array.append(product_name)
            #if product_name:
                #
    else:
        print(f"Error: {response.status_code}")

    update_opportunity_custom_fields(opportunity_id, product_names_array, headers)
    print(product_names_array)

get_opportunity_line_items('38918457')