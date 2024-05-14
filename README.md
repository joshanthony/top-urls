How to run:
- Install Python 3 on your local machine
- cd into the directory and run `python3 top_urls.py file.txt`
- file.txt can be any file in the required format, example file.text provided

Example output:
```
http://api.tech.com/item/16
http://api.tech.com/item/15
http://api.tech.com/item/14
http://api.tech.com/item/13
http://api.tech.com/item/12
http://api.tech.com/item/10
http://api.tech.com/item/9
http://api.tech.com/item/8
http://api.tech.com/item/7
http://api.tech.com/item/6
```

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
