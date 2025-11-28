import glob
import json

input_dir = "./portainer/templates"
output_file = "./portainer/templates.json"

templates = glob.glob(f"{input_dir}/*.json")

merged_templates = []

for idx, template in enumerate(templates):
    with open(template, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            data["id"] = idx+1
            merged_templates.append(data)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON file: {file}")

output = {
    "version": "3",
    "templates": merged_templates
}

# Clear output file first
open(output_file, 'w').close()

# Write output contents
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(
        output,
        f,
        indent=4,
        ensure_ascii=False
    )