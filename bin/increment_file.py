import os
import re

def get_next_filename(template):
  """
  Given a filename template, returns the next filename in the sequence.
  The template should contain a placeholder for the number, e.g., 'file_{}.txt'.
  """
  # Extract the directory and filename from the template
  directory, filename_template = os.path.split(template)
  
  # Create a regex pattern to match the filenames
  pattern = re.escape(filename_template).replace(r'\{\}', r'(\d+)')
  
  # List all files in the directory
  files = os.listdir(directory)
  
  # Find all matching files and extract their numbers
  numbers = []
  for file in files:
    match = re.match(pattern, file)
    if match:
      numbers.append(int(match.group(1)))
  
  # Determine the next number in the sequence
  if numbers:
    next_number = max(numbers) + 1
  else:
    next_number = 1
  
  # Generate the next filename
  next_filename = filename_template.format(next_number)
  
  return os.path.join(directory, next_filename)

def get_latest_filename(template):
  """
  Given a filename template, returns the latest filename in the sequence.
  The template should contain a placeholder for the number, e.g., 'file_{}.txt'.
  """
  # Extract the directory and filename from the template
  directory, filename_template = os.path.split(template)
  
  # Create a regex pattern to match the filenames
  pattern = re.escape(filename_template).replace(r'\{\}', r'(\d+)')
  
  # List all files in the directory
  files = os.listdir(directory)
  
  # Find all matching files and extract their numbers
  numbers = []
  for file in files:
    match = re.match(pattern, file)
    if match:
      numbers.append(int(match.group(1)))
  
  # Determine the latest number in the sequence
  if numbers:
    latest_number = max(numbers)
    latest_filename = filename_template.format(latest_number)
    return os.path.join(directory, latest_filename)
  else:
    return None
# Example usage
if __name__ == "__main__":
  template = "/home/ken/repos/iotaspencer.me/files/file_{}.txt"
  print(get_next_filename(template))
  
