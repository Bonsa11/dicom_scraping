# [DICOM Tag Scraping](https://github.com/Bonsa11/dicom_scrapign)
--- 
Return CSV of unique DICOM tags from folder with counts and examples 

### Usage
--- 
Can be run basically on a folder using:
```
$ python3 ./scrape_dicom_tags -s /path/to/src
```

Can be run recursively from a root folder using:
```
$ python3 ./scrape_dicom_tags -R -s /path/to/src
```

For more options:
```
$ python3 ./scrape_dicom_tags --help

usage: [-h] -s SRC [-d DST] [-R]

options:
  -h, --help         show this help message and exit
  -s SRC, --src SRC  root folder to start processing from
  -d DST, --dst DST  path to output file, defaults to ./dicom_tags.csv
  -R, --recursive    process recursively from src folder


```

### Installation
--- 
1. clone the git repo
```
$ git clone https://github.com/Bonsa11/scrape_dicom_tags.git
```

2. cd into the directory
```
$ cd ./scrape_dicom_tags   
```

3. create a virtual environment
```
$ python3 -m venv venv  
```

4. activate your virtual environment
```
$ source ./venv/bin/activate
```

5. install pandas and pydicom
```
(venv)$ pip install pydicom pandas
```

6. run the python module
```
(venv)$ python3 ./scrape_dicom_tags -s /path/to/src
```

