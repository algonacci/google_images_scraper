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

# Description
A simple tools to scrape data from Google Images for computer vision task

# How to run Google image scraping

- clone this repo
- `pip install numpy, imutils, opencv-python, argparse, requests`
- copy all the js_code.js
- open and search the google images, scroll down as much as you want
- press F12
- paste in the console log, press enter
- it will download urls.txt which contains all image url
- move the urls.txt to the project directory
- open terminal and run this command
- `python image-downloader2.py -u urls.txt -o dataset`
- press enter and wait till 10 minutes
