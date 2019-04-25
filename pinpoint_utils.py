
# 2019-04-23 16:52:15
# for teh grokking

# tpl_campaign list segments
# tpl_campaign delete segment <segment_id>  {probably need to define rules here}
# tpl_campaign create segment segment_name=“<string>” attributes=attr_x=ABC and attr_y=XYZ [user-pool=FOOBAR_ENV]

# tpl_campaign list campaigns [user-pool=FOOBAR_ENV]
# tpl_campaign delete campaign <campaign_id> [user-pool=FOOBAR_ENV]
#             {probably need to define rules here}
# tpl_campaign create campaign
#              segment=<segment_id>
#              campaign_name=<string> 
#              title=“Hum bug”
#              message_body=“go figure”
#              launch=<date_time_to_send_message, epoch_or_standard_format, SendIn_N_minutes>
#              user-pool=FOOBAR_ENV

import boto3
import pprint

# boto3.resource or ?

# awsutils? not in tp-api, not [aws-utils · PyPI ](https://pypi.org/project/aws-utils/)
# from this: [Automating AWS EC2 Management with Python and Boto3 ](https://stackabuse.com/automating-aws-ec2-management-with-python-and-boto3/)
# >>> session = awsutils.get_session('eu-west-1')
# >>> client = session.client('pinpoint')
# >>> pprint.pprint(client.describe_instances())

# 19/04/23 15:53:49 cjb-tp-macbook:~/Projects/trust-power-api/lambdas/notification-service/scripts/pinpoint ±(feature/TPL-127-wip-pinpoint-segs-and-campaigns) ✗ 
# bpython uses python3 by default
# ❯ bpython
# bpython version 0.18 on top of Python 3.7.2 /usr/local/opt/python/bin/python3.7
# >>> import boto3
# >>> boto3.session.Session()
# Session(region_name='eu-west-1')

# 19/04/23 15:06:16 cjb-tp-macbook:~/Projects/trust-power-api/lambdas/notification-service/scripts/pinpoint ±(feature/TPL-127-wip-pinpoint-segs-and-campaigns) ✗ 
# ❯ cat ~/.aws/*
# config:
# [default]
# output = json
# region = eu-west-1
# credentials:
# [default]
# aws_access_key_id = ...
# aws_secret_access_key = ...

# region-specific Session object
# is this necessary? when can do `boto3.client('pinpoint')`
# and when defaults to value in ~/.aws/credentials, e.g. `region = eu-west-1`
def get_session(region='eu-west-1'):  
  return boto3.session.Session(region_name=region)


def get_secrets():
  # argparse? via jb?
  # appconnect noddy method? general.git:dev/bin/appconnect gitignored?
  secrets_file = open('./secrets.sh', 'r')
  lines = secrets_file.readlines()
  secrets = {}
  for line in lines:
    if line.find('PINPOINT_PROJECT_ID') != -1:
      secrets['pinpoint_project_id'] = line[line.find('=')+1:].strip()
  secrets_file.close() # or do `with open(file, 'r') as f: x = f.readlines()`
  return secrets


# 19/04/23 16:59:01 cjb-tp-macbook:~/Projects/trust-power-api/lambdas/notification-service/scripts/pinpoint ±(feature/TPL-127-wip-pinpoint-segs-and-campaigns) ✗ 
# ❯ bpython
# bpython version 0.18 on top of Python 3.7.2 /usr/local/opt/python/bin/python3.7
# >>> import pinpoint_utils
# >>> pinpoint_utils.get_client()
# <botocore.client.Pinpoint object at 0x110452d68>
def get_client():
  return get_session().client('pinpoint')
  # or: return boto3.client('pinpoint')

# def get_client2():
#   return boto3.client('pinpoint')
#   # return get_session().client('pinpoint')


def print_endpoint(endpoint_id, pinpoint_id=get_secrets()['pinpoint_project_id']):
  # client = boto3.client('pinpoint') # assumes region from env?
  # if pinpoint_id == None: # smell
  #   pinpoint_id = get_secrets()['pinpoint_project_id']
  #   print('defaulted pinpoint_id to ' + get_secrets()['pinpoint_project_id'])
  print('pinpoint_id: ' + pinpoint_id)
  client = get_client()
  response = client.get_endpoint( # "only accepts keyword arguments"
      ApplicationId=pinpoint_id,   # pinpoint app id - doesn't change?
      EndpointId=endpoint_id       #? have to create by running app?
  )
  pprint.pprint(response)


# get_segments(**kwargs)
# Used to get information about your segments.
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_segment
def list_segments():
  segs = get_client().get_segments(
    ApplicationId=get_secrets()['pinpoint_project_id'],
    # PageSize='10',
    # Token='string' # ?? Invalid Token Received # for pagination
  )
  pprint.pprint(segs)


def delete_segment():
  pass


def create_segment():
  pass

# response = client.get_campaigns(
#     ApplicationId='string',
#     PageSize='string',
#     Token='string'
# )
def list_campaigns():
  camps = get_client().get_campaigns(
    ApplicationId=get_secrets()['pinpoint_project_id'],
    # PageSize='10',
    # Token='string' # ?? Invalid Token Received # for pagination
  )
  pprint.pprint(camps)


def delete_campaign():
  pass


def create_campaign():
  pass

