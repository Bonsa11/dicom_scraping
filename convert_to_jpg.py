import os
import cv2
from pydicom import dcmread
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--src", type=str, required=True,
                    help="root folder to start processing from")
parser.add_argument("-d", "--dst", type=str, required=False, default="dicom_tags.csv",
                    help="path to output file, defaults to ./dicom_tags.csv")
parser.add_argument("-R", "--recursive", required=False, action='store_true',
                    help="process recursively from src folder")


def convert_dicom_to_jpg(filepath: str, destination_folder: str):
    try:
        _, filename = os.path.split(filepath)
        save_path = os.path.join(destination_folder, f'{filename}.tif')
        ds = dcmread(filepath)
        print(f'saving {filepath} to {save_path}')
        cv2.imwrite(save_path, ds.pixel_array)
    except Exception as e:
        print(f'cannot parse {filepath}')


if __name__ == '__main__':
    args = parser.parse_args()
    if not args.recursive:
        files = [f for f in os.listdir(args.src) if os.path.isfile(os.path.join(args.src, f))]
        print(f'found {len(files)} to process in {args.src}')
        for file in files:
            convert_dicom_to_jpg(os.path.join(args.src, file), args.dst)
    else:
        for root, _, filenames in os.walk(args.src):
            for file in filenames:
                convert_dicom_to_jpg(os.path.join(root, file), args.dst)
