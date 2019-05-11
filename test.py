#! /usr/bin/env python3

from typing import Dict, List
import sys
import boto3
import pprint

def get_session(region='eu-west-1'):
  return boto3.session.Session(region_name=region)


def get_client():
  return get_session().client('pinpoint')
  # or: return boto3.client('pinpoint')
    # yes, seems to be the same

# def get_client2(self):
#   return boto3.client('pinpoint')

dry_run = True

def get_secrets():
  # general.git:dev/bin/appconnect noddy method:
  secrets_file = open('./secrets.sh', 'r')
  lines = secrets_file.readlines()
  secrets = {}
  for line in lines:
    if line.find('PINPOINT_APP_ID') != -1:
      secrets['pinpoint_project_id'] = line[line.find('=')+1:].strip()
  secrets_file.close() # or do `with open(file, 'r') as f: x = f.readlines()`
  return secrets

# number_of_days_since_initial_app_install_with_data
# has_data_in_last_24hr.

      # WriteSegmentRequest={
      #   'Dimensions': {
      #       'Attributes': {
      #           'string': {
      #               'AttributeType': 'INCLUSIVE'|'EXCLUSIVE',
      #               'Values': [
      #                   'string',
      #               ]
      #           }
      #       },

def create_segment(segment_name): #, attributes, user_pool=None):
  pp = pprint.PrettyPrinter(indent=4) # ?
  print(f'Creating segment name: {segment_name}')

  writesegmentrequest = {
    'Name': segment_name, # didn't have name before?
    'Dimensions': {
      'Attributes': {
        # 'has_data_in_last_24hr': {
        'something': {
          'AttributeType': 'INCLUSIVE',
          'Values': [
              "foo", "bar", # ?
          ] 
        }
      }
    }
  }
  name = "kb test segment"
  attributes =  {"something": ["foo", "bar"]}
  writesegmentrequest_kb = {
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
    }

  # print('writesegmentrequest: ')
  # pp.pprint(writesegmentrequest)
  # print('writesegmentrequest_kb: ')
  # pp.pprint(writesegmentrequest_kb)
  # exit()
  client = get_client()
  pp.pprint(client)
  pp.pprint('get_secrets()[\'pinpoint_project_id\']: ' + get_secrets()['pinpoint_project_id'])
  print(f'client: {client}')
  # response = get_client().create_segment(
  response = client.create_segment(
    ApplicationId=get_secrets()['pinpoint_project_id'],
    WriteSegmentRequest=writesegmentrequest
  )
  print(f'response: {response}')


def kb_create_segment(application_id: str, name: str, attributes: Dict[str, List[str]]):
  pinpoint = boto3.client("pinpoint")
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
    # mine...
    create_segment('cb test segment')
    # kim's
    # kb_create_segment("134edac7e3b445d69d0a240839b85128", "kb test segment", {"something": ["foo", "bar"]})

# kim's:
# ```py
# #! /usr/bin/env python3

# from typing import Dict, List
# import boto3

# pinpoint = boto3.client("pinpoint")

# def create_segment(application_id: str, name: str, attributes: Dict[str, List[str]]):
#     pinpoint.create_segment(
#         ApplicationId=application_id,
#         WriteSegmentRequest={
#             "Name": name,
#             "Dimensions": {
#                 "Attributes": {
#                     name: {
#                         "AttributeType": "INCLUSIVE",
#                         "Values": values
#                     }
#                     for (name, values) in attributes.items()
#                 }
#             }
#         })


# if __name__ == '__main__':
#     create_segment("134edac7e3b445d69d0a240839b85128", "Kim's Pinpoint Segment", {"something": ["blue", "green"]})
# ```

# cruft

  # pprint(f'client: {client}') # TypeError: 'module' object is not callable

  # # 'has_data_in_last_24hr'
  # values = {
  #   'true'
  # }
  # # values.append('true') # ?
  # has_data_in_last_24hr = {}
  # has_data_in_last_24hr['AttributeType'] = 'INCLUSIVE'
  # has_data_in_last_24hr['Values'] = values
  # attributes = {}
  # attributes['has_data_in_last_24hr'] = has_data_in_last_24hr
  # dimensions = {}
  # dimensions['Attributes'] = attributes
  # writesegmentrequest = {}
  # writesegmentrequest['Dimensions'] = dimensions
  # writesegmentrequest.append(dimensions)
