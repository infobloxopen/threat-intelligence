"""
Small script to validate the CSV files containing
indicators
"""
import csv
import logging
from pathlib import Path
import re
import sys

import validators


logger = logging.getLogger(__name__)


CLASSIFICATIONS = [
    "classification",
    "ddga",
    "legitimate",
    "malicious",
    "malvertising",
    "malware",
    "nameserver",
    "other",
    "parked",
    "phishing",
    "propaganda",
    "redirect",
    "scam",
    "smishing",
    "spam",
    "suspended",
    "suspicious",
    "unavailable",
]
FIELDNAMES = ["type", "indicator", "classification", "source", "notes", "references", "telfhash"]


def check_telfash(telfash: str):
    if not re.search('^t1[0-9a-f]{70}$', telfash):
        raise validators.ValidationFailure(
            f"Invalid telfash - {telfash} - should start with t1 followed by 70 hexadecimal characters"
        )


VALIDATION_FUNCS = {
    "domain": validators.domain,
    "ip": validators.ipv4,
    "ipv4": validators.ipv4,
    "email": validators.email,
    "url": validators.url,
    "sha256": validators.sha256,
    "telfhash": check_telfash,
}


def check_references(references: str) -> bool:
    """
    Checks all the references are valid URL's.
    """
    if not references:  # empty references column allowed
        return True
    try:
        validators.url(references)
        return True
    except validators.ValidationFailure as err:
        logger.warning("Invalid reference - '%s' - '%s'", references, err)
        return False


def validate_csv(file_path: Path):
    """
    Performs various checks on the CSV file containing indicators.
    """
    valid_csv = True
    with file_path.open() as open_file:
        open_file.readline()  # skip header
        reader = csv.DictReader(
            f=open_file, quoting=csv.QUOTE_ALL, fieldnames=FIELDNAMES
        )
        for line in reader:
            indicator_type = line["type"]
            indicator_value = line["indicator"]
            validation_func = VALIDATION_FUNCS.get(indicator_type)
            if not validation_func:
                logger.warning("Incorrect type - '%s'", line)
                valid_csv = False
            else:
                try:
                    validation_func(indicator_value)
                except validators.ValidationFailure as err:
                    logger.warning("Invalid indicator - '%s' - '%s'", line, err)
                    valid_csv = False

            if not check_references(line["references"]):
                valid_csv = False

            classification = line["classification"]
            if classification not in CLASSIFICATIONS:
                logger.warning("Invalid classification '%s' - %s", classification, line)
                valid_csv = False

    return valid_csv


def main():
    """
    Checks all the CSV files in the repo containing indicators.
    """
    csv_files = sorted(Path().rglob("*_iocs.csv"))
    success = True
    for csv_file in csv_files:
        if not validate_csv(csv_file):
            logger.warning("Issue with %s. See logs.", csv_file)
            success = False

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
