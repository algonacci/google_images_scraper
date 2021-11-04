from imutils import paths
import argparse
import requests
import cv2
import os
import numpy as np

# Adapted from https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/
# fixes the following issues with the original:
# 1 - files are always saved as .jpg even if they are not in JPEG format
#     This version uses open CV to write the image files so they are really always JPG
# 2 - failed files leave gaps in numbering
# 3 - numbering always starts from zero

# how to use 'python image-downloader2.py -u urls.txt -o my-bottle-dataset'

# link edit: 
# 1. https://gist.github.com/davesnowdon/2016d4e9f069ff1788ede4f2902bd198#file-image-downloader2-py
# 2. https://github.com/tomahim/py-image-dataset-generator


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
                help="path to file containing image URLs")
ap.add_argument("-o", "--output", required=True,
                help="path to output directory of images")
ap.add_argument("-s", "--start", required=False,
                help="First number to start at",
                default=0)
ap.add_argument("-v", "--verbose", required=False,
                help="Print information as we go",
                action="store_true", default=False)


# grab the list of URLs from the input file, then initialize the
def read_url_list(filename):
    return open(filename).read().strip().split("\n")


# generator to read URLs and return data
def read_urls(urls, is_verbose=False):
    for url in urls:
        try:
            # try to download the image
            if is_verbose:
                print("Downloading {}".format(url))
            r = requests.get(url, timeout=60)
            yield ((url, r.content))
        except requests.exceptions.RequestException as e:
            print("Error downloading {} : {}".format(url, e))


# test if files are image data that OpenCV can read
def return_images(file_contents, is_verbose=False):
    for url, data in file_contents:
        try:
            # convert to numpy array that OpenCV can read
            nparr = np.fromstring(data, np.uint8)
            # attempt to decode data as image
            img_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if img_cv is None:
                if is_verbose:
                    print("Skipping {} - not an image".format(url))
            else:
                # return the image
                yield ((url, img_cv))
        except Exception as err:
            if is_verbose:
                print("Error parsing {} : {}".format(url, err))


def write_images(images, output_dir, start=0, is_verbose=False):
    file_num = start
    for url, image in images:
        p = os.path.sep.join([output_dir, "{}.jpg".format(str(file_num).zfill(8))])
        cv2.imwrite(p, image)
        file_num += 1
        if is_verbose:
            print("{} <- {}".format(p, url))


if __name__ == "__main__":
    args = vars(ap.parse_args())
    output_dir = args["output"]
    is_verbose = args["verbose"]
    start = int(args["start"])

    urls = read_url_list(args["urls"])
    url_data = read_urls(urls, is_verbose)
    images = return_images(url_data, is_verbose)
    write_images(images, output_dir, start, is_verbose)