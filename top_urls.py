import sys
from queue import PriorityQueue

def get_top_urls(n = 10):
    # Check the args
    if (args := len(sys.argv)) > 2:
        print(f"Too many arguments, got {args - 1} expected 1")
        sys.exit(2)
    elif args < 2:
        print("Specify the file path")
        sys.exit(2)

    file_path = sys.argv[1]

    top_n_urls = PriorityQueue()
    
    # Open and read the file    
    with open(file_path, 'r') as f:
        for line in f:
            try:
                url, value = line.rsplit(maxsplit=1)
                value = int(value)
                # If the queue has space, add the url
                if top_n_urls.qsize() < n:
                    top_n_urls.put((value, url))
                else:
                    # If value is larger than the smallest item, replace it with value
                    if top_n_urls.queue[0][0] < value:
                        top_n_urls.get()
                        top_n_urls.put((value, url))
            except ValueError:
                continue
    
    # Reverse and print the result PriorityQueue supports minheap only
    result = []
    while not top_n_urls.empty():
        value, url = top_n_urls.get()
        result.append(url)

    print('\n'.join(reversed(result)))

if __name__ == "__main__":
    get_top_urls()