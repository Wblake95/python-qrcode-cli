import argparse, qrcode, requests, validators
import datetime
from os import path

date = str(datetime.date.today())

parser = argparse.ArgumentParser()
parser.add_argument("link")
parser.add_argument("-f","--filename", default=date + ".png")
parser.add_argument("-l","--location", default="~/Downloads/")

args = parser.parse_args()
if validators.url(args.link) and path.isdir(path.expanduser(args.location)):
    r = requests.head(args.link, allow_redirects=True)
    if r.status_code == 200:
        img = qrcode.make(args.link)
        img.save(path.expanduser(args.location) + args.filename)
    elif r.status_code == 404:
        print("Link argument is not a valid path:", r.status_code)
else:
    if not validators.url(args.link):
        print("Link argument is not valide url:", args.link)
    else:
        print("Location argument is not valide directory:", args.location)
