#!/usr/bin/env python3

# SPDX-FileCopyrightText: GARDENA GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse
import logging
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MAIN")


def check_and_log(expr, log_message):
    if not expr:
        logger.error(log_message)
        sys.exit(1)


def discover_files(directory_or_files: List[Path]):
    for d in directory_or_files:
        if d.is_dir():
            for dirpath, _dirnames, filenames in os.walk(d):
                for filename in filenames:
                    file_path = Path(dirpath, filename)
                    assert file_path.is_file()
                    if file_path.suffix == ".xml":
                        yield file_path
        elif d.is_file():
            yield d


def check_file(file_path: Path):
    logger.info(f"Checking {file_path}")
    obj = get_object_spec_node(file_path)

    # Checks
    check_urn(obj)


def get_object_spec_node(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    check_and_log(root.tag == "LWM2M", "Root tag not found")
    obj = root.find("Object")
    return obj


def check_urn(obj):
    obj_id = obj.find("ObjectID").text
    obj_version = obj.find("ObjectVersion")

    if obj_version is not None:
        obj_version = obj_version.text

    obj_urn = obj.find("ObjectURN").text
    obj_urn_parts = obj_urn.split(":")
    check_and_log(
        len(obj_urn_parts) == 5 or len(obj_urn_parts) == 6,
        f"URN consist of {obj_urn_parts} parts. 5 or 6 expected.",
    )

    check_and_log(
        obj_urn_parts[4] == obj_id,
        f"Object ID in URN is wrong. ID: {obj_id}. URN: {obj_urn}",
    )
    if len(obj_urn_parts) == 6:
        check_and_log(
            obj_urn_parts[5] == obj_version,
            f"Object version in URN is wrong. Version: {obj_version}. URN: {obj_urn}",
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", help="directories or files to check", nargs="*")
    args = parser.parse_args()
    paths = [Path(p) for p in args.paths]
    files = discover_files(paths)
    for file in files:
        check_file(file)


if __name__ == "__main__":
    main()
