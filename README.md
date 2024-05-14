How to run:
- Install Python 3 on your local machine
- cd into the directory and run `python3 top_urls.py file.txt`
- Provide any file instead of file.txt

Assumptions
- We only need to store the top 10 results
- The example file format does not change
- Skip/ignore invalid values
- Accept absolute or relative paths
- It doesn't need a GUI

How to test:
- Use Python built in unittest
- Use unittest.mock to mock the file read
- Compre expected output using assertEqual
