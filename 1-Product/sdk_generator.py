import yaml
import jinja2
import os
import re
import requests
import shutil
import subprocess
import json
import copy

def is_remote_url(input_path):
    """Checks if the input path is a remote URL."""
    return input_path.startswith("http://") or input_path.startswith("https://")

def download_openapi_spec(url, filename):
    """Downloads the OpenAPI specification from the given URL."""
    response = requests.get(url)
    response.raise_for_status()

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        f.write(response.text)
    return yaml.safe_load(response.text)

def load_openapi_spec(filepath):
    """Loads and parses the OpenAPI specification from a YAML file."""
    with open(filepath, "r") as f:
        try:
            spec = yaml.safe_load(f)
            return spec
        except yaml.YAMLError as e:
            print(f"Error parsing OpenAPI specification: {e}")
            return None

def sanitize_filename(filename):
    """Sanitizes a string to be a valid filename."""
    return re.sub(r"[^a-zA-Z0-9_\-]", "_", filename)

def generate_sdk(spec, language, output_dir, file_path):
    """Generates the SDK based on the OpenAPI specification."""
    print(f"Entering generate_sdk function for {language}")

    sdk_name = spec["info"]["title"].lower().replace(" ", "_")
    sdk_output_dir = os.path.join(output_dir, f"output-sdk-{language}", sdk_name)
    os.makedirs(sdk_output_dir, exist_ok=True)

    template_dir = os.path.join(os.path.dirname(__file__), "templates")

    # Select the appropriate Jinja template and SDK file name based on language
    if language == "python":
        template_filename = "python_sdk.jinja"
        sdk_file_name = "__init__.py"
    elif language == "node":
        template_filename = "node_sdk.jinja"
        sdk_file_name = "index.js"
    else:
        raise ValueError(f"Unsupported SDK language: {language}")

    template_path = os.path.join(template_dir, template_filename)
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )

    sdk_template = env.get_template(template_filename)
    sdk_file_path = os.path.join(sdk_output_dir, sdk_file_name)

    # Create an instance of ApiClient with the base URL from the spec
    base_url = spec["servers"][0]["url"] if "servers" in spec and spec["servers"] else ""

    # Deep copy the spec to avoid modifying the original spec
    spec_copy = copy.deepcopy(spec)

    # Generate the SDK code
    with open(sdk_file_path, "w") as f:
        if language == "python":
            f.write(sdk_template.render(spec=spec_copy, base_url=base_url, language=language))
        elif language == "node":
            # Convert method names to uppercase for Node.js in the copied spec
            for path, methods in spec_copy['paths'].items():
                methods_copy = methods.copy()
                for method, details in methods_copy.items():
                    if method.lower() != 'parameters':
                        methods[method.upper()] = methods.pop(method)

            f.write(sdk_template.render(spec=spec_copy, base_url=base_url, language=language))

    # Generate README.md
    readme_path = os.path.join(sdk_output_dir, "README.md")
    generate_readme(spec, language, readme_path)

    # Copy the OpenAPI YAML file to the SDK directory
    try:
        shutil.copy(file_path, os.path.join(sdk_output_dir, "openapi.yaml"))
    except Exception as e:
        print(f"Error copying OpenAPI YAML file: {e}")

    # Node.js specific steps
    if language == "node":
        # 1. Create package.json (if needed)
        package_json_path = os.path.join(sdk_output_dir, "package.json")
        if not os.path.exists(package_json_path):
            with open(package_json_path, "w") as f:
                f.write(
                    json.dumps(
                        {
                            "name": sdk_name,
                            "version": "1.0.0",
                            "description": f"Node.js SDK for {sdk_name}",
                            "main": "index.js",
                            "scripts": {
                                "test": "echo \"Error: no test specified\" && exit 1"
                            },
                            "keywords": [],
                            "author": "",
                            "license": "ISC",
                            "dependencies": {
                                "axios": "^1.6.8"
                            },
                        },
                        indent=2,
                    )
                )

        # 2. Install dependencies (using subprocess)
        try:
            subprocess.run(
                ["npm", "install"],
                cwd=sdk_output_dir,
                check=True,
                capture_output=True,
                text=True
            )
            print(f"Node.js dependencies installed successfully in {sdk_output_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing Node.js dependencies: {e}")
            if e.stdout:
                print("stdout:", e.stdout)
            if e.stderr:
                print("stderr:", e.stderr)

    print(f"{language} SDK code generated in: {sdk_file_path}")

def generate_readme(spec, language, output_path):
    """Generates a README.md file for the SDK."""
    sdk_name = spec["info"]["title"]
    description = spec["info"].get("description", "No description provided.")

    # Create a simple overview of the endpoints
    endpoints_overview = ""
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method.lower() != "parameters":
                endpoints_overview += f"- `{method.upper()} {path}`: {details.get('summary', 'No summary')}\n"

    readme_content = f"""
# {language} SDK for {sdk_name}

## Description
{description}

## Endpoints Overview
{endpoints_overview}
"""

    with open(output_path, "w") as f:
        f.write(readme_content.strip())

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.api_key = "special-key"  # Add API key here

    def call_api(self, path, method, params=None):
        url = f"{self.base_url}{path}"
        headers = {
            "Content-Type": "application/json",
            "api_key": self.api_key  # Include API key in headers
        }

        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=params, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=params, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()

        if response.headers["Content-Type"] == "application/json":
            return response.json()
        else:
            return response.text()