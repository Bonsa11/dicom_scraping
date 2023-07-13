import pandas as pd
import os
import pydicom
import argparse

from maps import data_type_map

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--src", type=str, required=True,
                    help="root folder to start processing from")
parser.add_argument("-d", "--dst", type=str, required=False, default="dicom_tags.csv",
                    help="path to output file, defaults to ./dicom_tags.csv")
parser.add_argument("-R", "--recursive", required=False, action='store_true',
                    help="process recursively from src folder")


def show_dataset(ds: pydicom.dataset, indent: str = '') -> None:
    """print dataset in order, honoring sequences in tags

    :param ds: dataset from DICOM file
    :param indent: whitespace for formatting
    :return: None
    """
    printed_elms = set()
    for elem in ds:
        if elem.VR == "SQ":
            indent += 4 * " "
            if elem.tag not in printed_elms:
                print(indent + str(elem.tag))
                printed_elms.add(elem.tag)
            for item in elem:
                show_dataset(item, indent)
            indent = indent[4:]
        if elem.tag not in printed_elms:
            print(indent + str(elem.tag))
            printed_elms.add(elem.tag)


def print_dataset(file_name) -> None:
    """read in dataset form file and print

    :param file_name: path to DICOM file
    :return: None
    """
    ds = pydicom.dcmread(file_name)
    show_dataset(ds)


def parse_element(elem: pydicom.dataelem.DataElement):
    return None
# TODO


def parse_dicom(filepath: str, dicom_data: dict = {}) -> dict:
    """parses dicom, gets all tags and loads into dictionary

    :param filepath: path to dicom
    :param dicom_data: dict of dicom tags
    :return: updated dictionary
    """
    try:
        ds = pydicom.dcmread(filepath)
        _, filename = os.path.split(filepath)
        for elem in ds:
            dicom_data[f'{filename}.{elem.name}'] = parse_element(elem)
    except Exception as e:
        print(f'failed to process {filename} :: {e}')
    finally:
        return dicom_data


def main():
    """

    :return: None
    """
    args = parser.parse_args()
    data = {}
    if not args.recursive:
        files = [f for f in os.listdir(args.src) if os.path.isfile(os.path.join(args.src, f))]
        print(f'found {len(files)} to process in {args.src}')
        for file in files:
            # data = parse_dicom(os.path.join(args.src, file), data)
            print_dataset(os.path.join(args.src, file))
    else:
        for root, _, filenames in os.walk(args.src):
            for file in filenames[0:5]:
                print(f'parsing DICOMs from root {args.src}')
                # data = parse_dicom(os.path.join(root, file), data)
                print_dataset(os.path.join(root, file))

    df = pd.DataFrame.from_dict(data, orient='index').reset_index()
    df.drop(columns=['index'])
    df.to_csv(args.dst)


if __name__ == '__main__':
    main()
