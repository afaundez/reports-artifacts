import sys
import json
from pathlib import Path

output_path = '/tmp/output.txt'
output_content = { 'output': output_path, 'args': sys.argv }
json_object = json.dumps(output_content, indent = 4)
print(json_object)

with open(output_path, 'w+') as f:
    f.write(json_object)
