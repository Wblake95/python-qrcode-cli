import argparse, qrcode, requests, validators
from datetime import date
from os import path

Date = str(date.today())

parser = argparse.ArgumentParser()
parser.add_argument("link")
# :param link: Enter link for the qrcode
parser.add_argument("-f","--filename", default=date + ".png")
# :param filename: Enter filename for the qrcode
parser.add_argument("-l","--location", default="~/Downloads/")
# :param location: Enter directory for the qrcode

args = parser.parse_args()
if validators.url(args.link) and path.isdir(path.expanduser(args.location)):
    r = requests.head(args.link, allow_redirects=True)
    if r.status_code == 200:
        # if url is true, make qr code
        img = qrcode.make(args.link)
        img.save(path.expanduser(args.location) + args.filename)
    elif r.status_code == 404:
        # if url is an error, print warning
        print("Link argument is not a valid path:", r.status_code)
else:
    # print for errors in link or directory
    if not validators.url(args.link):
        print("Link argument is not valide url:", args.link)
    else:
        print("Location argument is not valide directory:", args.location)
