import pandas as pd
import dataframe_image as dfi
import os
import json

def json_to_table_image(json_file_path, output_image_path, **kwargs):
    """
    Converts a JSON file to a styled table image (PNG) with left-aligned
    cells and blue column headers with white font. Ensures left alignment
    by directly setting cell properties.

    Args:
        json_file_path (str): Path to the JSON file.
        output_image_path (str): Path to save the output PNG image.
        **kwargs: Additional keyword arguments to customize table styling 
                  (passed to dfi.export). See dataframe_image documentation
                  for available options (e.g., table_conversion, max_rows, 
                  max_cols, etc.).
    """

    try:
        # Read JSON into a pandas DataFrame
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        if isinstance(data, list):
            df = pd.DataFrame(data)
        elif isinstance(data, dict):
            df = pd.DataFrame([data])
        else:
            raise ValueError("Unsupported JSON format. Expecting a list of dictionaries or a single dictionary.")

        # Left-align all cells using set_properties
        styled_df = df.style.set_properties(**{'text-align': 'left'}).set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'left'), ('background-color', 'blue'), ('color', 'white')]},
            {'selector': 'tr:nth-of-type(odd)', 'props': [('background-color', '#f2f2f2')]},
        ])

        # Export styled DataFrame to PNG image (no title set)
        dfi.export(styled_df, output_image_path, **kwargs)

        print(f"Table image saved to: {output_image_path}")

    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {json_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define the marketing folder and JSON file names
marketing_folder = "marketing"
json_files = {
    "api-events": "api-events.json",
    "blog-schedule": "blog-schedule.json",
    "video-schedule": "video-schedule.json"
}

# Process each JSON file
for table_name, json_file_name in json_files.items():
    json_file_relative_path = os.path.join(marketing_folder, json_file_name)
    output_png = os.path.join(marketing_folder, f"{table_name}_table.png")

    # Get the absolute path of the JSON file
    json_file_absolute_path = os.path.abspath(json_file_relative_path)

    json_to_table_image(
        json_file_absolute_path,
        output_png,
        table_conversion='matplotlib',
        max_rows=15,
        max_cols=8
    )