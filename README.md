<div align="center">
  <h1>
    <img
      src="https://raw.githubusercontent.com/algonacci/Free-CDN/main/Chara.png"
      width="100px"
    /><br />Google Images Scraper
  </h1>
</div>
<p align="center">
  <a href="https://twitter.com/algonacci" target="_blank"
    ><img
      alt=""
      src="https://img.shields.io/badge/Twitter-1DA1F2?style=normal&logo=twitter&logoColor=white"
      style="vertical-align: center"
  /></a>
  <a href="https://id.linkedin.com/in/ericjuliantooo" target="_blank"
    ><img
      alt=""
      src="https://img.shields.io/badge/LinkedIn-0077B5?style=normal&logo=linkedin&logoColor=white"
      style="vertical-align: center"
  /></a>
</p>

## Description
A simple tools to scrape data from Google Images for computer vision task

## Installation
```bash
# Python version 3.7.9 or newer
$ git clone https://github.com/algonacci/google_images_scraper.git
$ pip install -r requirements.txt
```

## Usage
- Make a folder named `dataset` in the project directory
- Copy all inside the `js_code.js`
- Search for a keyword in Google Images, and scroll down as much as you want
- Press `F12` in your keyboard
- Paste in the console log, then hit enter
- It will download `urls.txt` which contains all the scraped image's urls
- Copy that `urls.txt` into the project directory
- Open terminal and run `python image-downloader2.py -u urls.txt -o dataset`
- Hit enter and wait till all images are scraped

## License
[MIT LICENSE](./LICENSE)

© Developed by [algonacci](https://github.com/algonacci)
