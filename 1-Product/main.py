from sdk_generator import generate_sdk, load_openapi_spec
import os

# Configuration
OUTPUT_DIR = "output_sdk"

def main():
    """
    Generates an SDK from a local OpenAPI YAML specification.
    """

    # Get input file path from user
    file_path = input("Enter the full path to the local OpenAPI YAML file: ")

    # Load from local file
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    # Check if it's a YAML file (optional, but good practice)
    if not file_path.lower().endswith((".yaml", ".yml")):
        print("Warning: The specified file does not have a .yaml or .yml extension.")

    try:
        spec = load_openapi_spec(file_path)
        print(f"Loaded OpenAPI spec from {file_path}")
    except Exception as e:
        print(f"Error loading OpenAPI spec: {e}")
        return

    # SDK type selection
    sdk_types = ["python", "node"]
    print("Available SDK types:")
    for i, sdk_type in enumerate(sdk_types):
        print(f"{i+1}. {sdk_type}")

    while True:
        try:
            choice = int(input(f"Select SDK type (1 or 2): "))
            if choice == 1 or choice == 2:
                language = sdk_types[choice - 1]
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if spec:
        print(f"Generating {language} SDK...")
        generate_sdk(spec, language, OUTPUT_DIR, file_path)
        print(f"SDK generated in '{OUTPUT_DIR}' directory.")
    else:
        print("Failed to load OpenAPI spec. Check for errors above.")

if __name__ == "__main__":
    main()