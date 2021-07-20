import sys
import json
from pathlib import Path

output_path = '/tmp/output.txt'
Path(output_path).touch()
output_paths = { 'output': output_path, 'args': sys.argv }
print(json.dumps(output_paths, indent = 4))
