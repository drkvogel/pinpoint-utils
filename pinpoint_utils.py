
# 2019-04-23 16:52:15
# for teh grokking

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html

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

# region-specific Session object
# is this necessary? when can do `boto3.client('pinpoint')`
# and when defaults to value in ~/.aws/credentials, e.g. `region = eu-west-1`
# >>> sess = boto3.session.Session()
# >>> sess
# Session(region_name='eu-west-1')
def get_session(region='eu-west-1'):
  return boto3.session.Session(region_name=region)


def get_client():
  return get_session().client('pinpoint')
  # or: return boto3.client('pinpoint')
    # yes, seems to be the same

# def get_client2():
#   return boto3.client('pinpoint')


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
    # Token='string' # for pagination
  )
  pprint.pprint(segs)


# tpl_campaign delete segment <segment_id>  {probably need to define rules here}
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_segment
def delete_segment(segment_id):
  get_client().delete_segment(
    ApplicationId=get_secrets()['pinpoint_project_id'],
    SegmentId=segment_id
  )


# tpl_campaign create segment segment_name=“<string>” attributes=attr_x=ABC and attr_y=XYZ [user-pool=FOOBAR_ENV]
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_segment
def create_segment(segment_name, attributes, user_pool=None):
  response = get_client().create_segment(
    # lots of stuff
  )


# tpl_campaign list campaigns [user-pool=FOOBAR_ENV]
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_campaigns
def list_campaigns(user_pool=None):
  camps = get_client().get_campaigns(
    ApplicationId=get_secrets()['pinpoint_project_id'],
    # PageSize='10',
    # Token='string' # for pagination
  )
  pprint.pprint(camps)


# tpl_campaign delete campaign <campaign_id> [user-pool=FOOBAR_ENV]
#             {probably need to define rules here}
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_campaign
def delete_campaign(campaign_id, user_pool=None):
  # TODO are you sure?
  get_client().delete_campaign(
      ApplicationId=get_secrets()['pinpoint_project_id'],
      CampaignId=campaign_id
  )


# tpl_campaign create campaign
#              segment=<segment_id>
#              campaign_name=<string> 
#              title=“Hum bug”
#              message_body=“go figure”
#              launch=<date_time_to_send_message, epoch_or_standard_format, SendIn_N_minutes>
#              user-pool=FOOBAR_ENV
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_campaign
def create_campaign(segment, campaign_name, title, message_body, launch, user_pool):
  response = get_client().create_campaign(
    # huge amount of stuff
  )
  # parse response