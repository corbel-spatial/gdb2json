import os
import xml.etree.ElementTree as ET  # noqa

import xmltodict


def parse(gdb_path: str):
    if not gdb_path.endswith(".gdb"):
        raise FileNotFoundError(gdb_path)

    dataset = dict()
    with open(os.path.join(os.path.abspath(gdb_path), "a00000004.gdbtable"), "rb") as f:
        gdbtable = f.read()

        for root_name in [
            "DEFeatureClassInfo",
            "DEFeatureDataset",
            "DERasterDataset",
            "DEWorkspace",
            "ESRI_ItemInformation",
            "metadata",
            "typens:DEFeatureDataset",
            "typens:DETableInfo",
        ]:
            start_pos = 0
            while True:
                start_pos = gdbtable.find(
                    bytes(f"<{root_name} ", "utf-8"), start_pos
                )
                end_pos = gdbtable.find(
                    bytes(f"</{root_name}>", "utf-8"), start_pos
                )
                if start_pos == -1 or end_pos == -1:  # no matches
                    break
                end_pos = end_pos + len(f"</{root_name}>")
                match = gdbtable[start_pos:end_pos].decode("utf-8")
                start_pos = end_pos

                xml_dict = xmltodict.parse(match)
                if root_name not in dataset:
                    dataset[root_name] = list()
                dataset[root_name].append(xml_dict)
    return dataset
