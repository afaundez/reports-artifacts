import os
import sys
import json
from pathlib import Path

output_path = '/tmp/output.txt'
output_content = { 'output': output_path, 'args': sys.argv }
json_object = json.dumps(output_content, indent = 4)
print('=== JSON OBJECT ===')
print(json_object)

with open(output_path, 'w+') as f:
    f.write(json_object)

cmd = f'ls /tmp'
print(f'=== {cmd} ===')
print(os.system(cmd))

cmd = f'cat {output_path}'
print(f'=== {cmd} ===')
print(os.system(cmd))
