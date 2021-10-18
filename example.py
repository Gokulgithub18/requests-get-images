import json
import os
from src.download_file import download_file

# Downloads a number of image files from Firebase Storage

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
            output_file_path=os.path.join(os.getcwd(), config["DOWNLOAD_DIR"], file)
        )