import json
import os
import requests

def download_file(url: str, output_file: str):
    """  
    Sets up a request to stream data from the provided URL, and write it to a specified file in chunks
    
    args:
        - url (str) : the location of the file being downloaded
        - output_file (str) : the name you want to give the downloaded file
    """
    with requests.get(url, stream=True) as file_request:
        file_request.raise_for_status()
        with open(output_file, "wb") as file:
            for chunk in file_request.iter_content(chunk_size=1000):  # chunk size is configurable
                file.write(chunk)

if __name__=="__main__":
    with open(os.path.join(os.getcwd(), "config.json")) as config_file:
        config = json.load(config_file)
    
    file_list = [
        "E-ChuNsOIEc.jpg",
        "_kG6AnmQp_o.jpg",
        "SKRH9tkztMg.jpg",
        "sLXC_oNOdbA.jpg",
        "WGLnUbCEFcc.jpg",
    ]
    for file in file_list:
        download_file(
            url=config["BASE_URL"].format(file_name=file), 
            output_file=os.path.join(os.getcwd(), config["DOWNLOAD_DIR"], file)
        )