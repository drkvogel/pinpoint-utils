#! /usr/bin/env python3

from typing import Dict, List
import boto3

pinpoint = boto3.client("pinpoint")

def create_segment(application_id: str, name: str, attributes: Dict[str, List[str]]):
    pinpoint.create_segment(
        ApplicationId=application_id,
        WriteSegmentRequest={
            "Name": name,
            "Dimensions": {
                "Attributes": {
                    name: {
                        "AttributeType": "INCLUSIVE",
                        "Values": values
                    }
                    for (name, values) in attributes.items()
                }
            }
        })


if __name__ == '__main__':
    create_segment("134edac7e3b445d69d0a240839b85128", "Kim's Pinpoint Segment", {"something": ["blue", "green"]})
