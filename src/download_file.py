import requests

def download_file(url: str, output_file_path: str):
    """  
    Sets up a request to stream data from the provided URL, writing it to the specified output file
    
    args:
        - url (str) : the location of the file being downloaded
        - output_file_path (str) : the name you want to give the downloaded file
    """
    with requests.get(url, stream=True) as file_request:
        file_request.raise_for_status()
        with open(output_file_path, "wb") as output_file:
            for chunk in file_request.iter_content(chunk_size=1000):
                output_file.write(chunk)
