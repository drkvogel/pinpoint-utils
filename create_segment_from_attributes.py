#! /usr/bin/env python3

# 1.	Create script to create segment from attributes
# 2.	Create script to create campaign from segments
# 3.	Create script to create the specified set of time-based notifications using the previous two scripts

# get endpoint from env: PINPOINT_APP_ID
# >Set `PINPOINT_APP_ID` to the "Project ID" for the Pinpoint in the `dev-trust-power` AWS account.

# is this in import_dev_secrets.sh? no
# in ./secrets.sh

#     create-segment — AWS CLI 1.16.141 Command Reference (https://docs.aws.amazon.com/cli/latest/reference/pinpoint/create-segment.html)
#     Pinpoint — Boto 3 Docs 1.9.131 documentation (https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html)

# https://docs.python.org/3/library/argparse.html

import boto3
import pprint
# >>> session = awsutils.get_session('eu-west-1')
# >>> client = session.client('pinpoint')
# >>> pprint.pprint(client.describe_instances())

# region-specific Session object
def get_session(region):  
    return boto3.session.Session(region_name=region)

  
def print_endpoint(endpoint):
  client = boto3.client('pinpoint') # assumes region from env?
  response = client.get_endpoint(
      ApplicationId='', # pinpoint app id
      EndpointId='' #?
  )
  pprint.pprint(response)
