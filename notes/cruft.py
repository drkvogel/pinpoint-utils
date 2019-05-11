

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

import sys
import boto3
import pprint

# stuff to run always here such as class/def
# def main():
#     pass


if __name__ == "__main__":
  print('__name__ == "__main__"')
  # stuff only to run when not called via 'import' here
  # main()
  # utils = PinpointUtils()
  pass

# >>> from pinpoint_utils import PinpointUtils
# >>> utils = PinpointUtils()

class PinpointUtils():

  # region-specific Session object
  # is this necessary? when can do `boto3.client('pinpoint')`
  # and when defaults to value in ~/.aws/credentials, e.g. `region = eu-west-1`
  # >>> sess = boto3.session.Session()
  # >>> sess
  # Session(region_name='eu-west-1')
  def get_session(region='eu-west-1'):
    return boto3.session.Session(region_name=region)

  def get_client(self):
    return get_session().client('pinpoint')
    # or: return boto3.client('pinpoint')
      # yes, seems to be the same

  # def get_client2(self):
  #   return boto3.client('pinpoint')

  dry_run = True

  def get_secrets(self):
    # general.git:dev/bin/appconnect noddy method:
    secrets_file = open('./secrets.sh', 'r')
    lines = secrets_file.readlines()
    secrets = {}
    for line in lines:
      if line.find('PINPOINT_APP_ID') != -1:
        secrets['pinpoint_project_id'] = line[line.find('=')+1:].strip()
    secrets_file.close() # or do `with open(file, 'r') as f: x = f.readlines()`
    return secrets


  # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_user_endpoints
  def print_endpoints(self):
    print('pinpoint_id: ' + pinpoint_id)
    client = get_client()
    response = client.get_user_endpoints( # "only accepts keyword arguments"
        ApplicationId=pinpoint_id,   # pinpoint app id - doesn't change?
        EndpointId=endpoint_id       #? have to create by running app?
    )
    pprint.pprint(response)


  def print_endpoint(self, endpoint_id):
    # client = boto3.client('pinpoint') # assumes region from env?
    # if pinpoint_id == None: # smell
    client = self.get_client()
    pinpoint_id = self.get_secrets()['pinpoint_project_id']
    #   print('defaulted pinpoint_id to ' + get_secrets()['pinpoint_project_id'])
    print('pinpoint_id: ' + pinpoint_id)
    are_you_sure()
    print('TODO')
    sys.exit()
    response = client.get_endpoint( # "only accepts keyword arguments"
        ApplicationId=pinpoint_id,   # pinpoint app id - doesn't change?
        EndpointId=endpoint_id       #? have to create by running app?
    )
    pprint.pprint(response)


  # get_segments(**kwargs)
  # Used to get information about your segments.
  # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_segment
  def list_segments(self):
    segs = get_client().get_segments(
      ApplicationId=get_secrets()['pinpoint_project_id'],
      # PageSize='10',
      # Token='string' # for pagination
    )
    pprint.pprint(segs)


  # tpl_campaign delete segment <segment_id>  {probably need to define rules here}
  # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_segment
  def delete_segment(self, segment_id):
    print(f'Deleting segment id: {segment_id}')
    are_you_sure()
    print('TODO')
    sys.exit()
    if not dry_run:
      get_client().delete_segment(
        ApplicationId=get_secrets()['pinpoint_project_id'],
        SegmentId=segment_id
      )


  # tpl_campaign create segment segment_name=“<string>” attributes=attr_x=ABC and attr_y=XYZ [user-pool=FOOBAR_ENV]
  # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_segment
  def create_segment(self, segment_name, attributes, user_pool=None):
    print('TODO')
    sys.exit()
    print(f'Creating segment name: {segment_name}')
    if not dry_run:
      response = get_client().create_segment(
        ApplicationId=get_secrets()['pinpoint_project_id'],
        WriteSegmentRequest=request
        # lots of stuff
      )

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
    # name = "kb test segment"
    # attributes =  {"something": ["foo", "bar"]}
    # writesegmentrequest_kb = {
    #       "Name": name,
    #       "Dimensions": {
    #           "Attributes": {
    #               name: {
    #                   "AttributeType": "INCLUSIVE",
    #                   "Values": values
    #               }
    #               for (name, values) in attributes.items()
    #           }
    #       }
    #   }

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

  # tpl_campaign list campaigns [user-pool=FOOBAR_ENV]
  # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_campaigns
  def list_campaigns(self, user_pool=None):
    print('list campaigns')
    print('TODO')
    sys.exit()
    camps = get_client().get_campaigns(
      ApplicationId=get_secrets()['pinpoint_project_id'],
      # PageSize='10',
      # Token='string' # for pagination
    )
    pprint.pprint(camps)

  def are_you_sure(self):
    if not input("Are you sure? (y/n): ").lower().strip()[:1] == "y": 
      print('Quitting.')
      sys.exit(1)

  # tpl_campaign delete campaign <campaign_id> [user-pool=FOOBAR_ENV]
  #             {probably need to define rules here}
  # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_campaign
  def delete_campaign(self, campaign_id, user_pool=None):
    # TODO are you sure?
    print(f'Deleting campaign id: {campaign_id}')
    # if not input("Are you sure? (y/n): ").lower().strip()[:1] == "y": sys.exit(1)
    are_you_sure()
    print('TODO')
    sys.exit()
    if not dry_run:
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
  def create_campaign(self, segment, campaign_name, title, message_body, launch, user_pool):
    print(f'Creating campaign for segment: {segment}, name: {campaign_name}')
    are_you_sure()
    print('TODO')
    sys.exit()
    if not dry_run:
      response = get_client().create_campaign(
        # 
      )
      # parse response


# cruft

  # def print_endpoint(self, endpoint_id, pinpoint_id=get_secrets()['pinpoint_project_id']):
    # get_secrets() is run on import when in the args like this
