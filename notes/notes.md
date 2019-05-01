
[TPL-127 Create Pinpoint segments & campaigns for time-based push notifications - Jira ](https://trustpower-com.atlassian.net/browse/TPL-127) 
  

1.	Create script to create segment from attributes
2.	Create script to create campaign from segments
3.	Create script to create the specified set of time-based notifications using the previous two scripts


Get List of endpoints for specific user (First get user-id from cognito):
```
aws pinpoint get-user-endpoints --application-id <appid> --region us-east-1 --user-id <userid>
```
Get details of specific endpoint:
```
aws pinpoint get-endpoint --application-id <appid> --region us-east-1 --endpoint-id ID_XXX (edited)
```

The *Attributes* portion within the JSON returned by the above command has been empty (bug). I’ve used the following command to update the Attributes manually, without this you will not see the key=value pair appear within pinpoint console (to help create segments/campaigns).
```
aws pinpoint update-endpoint --application-id ${APPLICATION_ID} --region us-east-1  --endpoint-id ${ep_id} --endpoint-request file://${JSON_FILE}
```

Where `JSON_FILE` contains, e.g.:

```json
{
  "Attributes": {
    "appBuild" : ["978", "1049"],
    "MVP_Alpha_CohortID" : ["2"],
    "Device" : ["Installed"]
  }
}
```

```java
  static final String NUMBER_OF_DAYS_SINCE_INITIAL_APP_INSTALL_WITH_DATA_ATTRIBUTE_NAME = System.getenv().getOrDefault("NUMBER_OF_DAYS_SINCE_INITIAL_APP_INSTALL_WITH_DATA_ATTRIBUTE_NAME", "number_of_days_since_initial_app_install_with_data");
  static final String HAS_DATA_IN_LAST_24_HR_ATTRIBUTE_NAME = System.getenv().getOrDefault("HAS_DATA_IN_LAST_24_HR_ATTRIBUTE_NAME", "has_data_in_last_24hr");
```

```py
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

# 19/04/23 16:59:01 cjb-tp-macbook:~/Projects/trust-power-api/lambdas/notification-service/scripts/pinpoint ±(feature/TPL-127-wip-pinpoint-segs-and-campaigns) ✗ 
# ❯ bpython
# bpython version 0.18 on top of Python 3.7.2 /usr/local/opt/python/bin/python3.7
# >>> import pinpoint_utils
# >>> pinpoint_utils.get_client()
# <botocore.client.Pinpoint object at 0x110452d68>

>>> import boto3
>>> c = boto3.client('pinpoint')
>>> c
<botocore.client.Pinpoint object at 0x112693978>
>>> sess = boto3.session.Session()
>>> sess
Session(region_name='eu-west-1')
>>> c2 = sess.client('pinpoint')
>>> c2
<botocore.client.Pinpoint object at 0x11297a5c0>
>>> 
```

## done

2019-04-23 13:00:15 linkified!
