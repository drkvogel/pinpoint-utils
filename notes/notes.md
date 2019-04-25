
[TPL-127 Create Pinpoint segments & campaigns for time-based push notifications - Jira ](https://trustpower-com.atlassian.net/browse/TPL-127) 
  2019-04-23 13:00:15 linkified!


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

Where JSON_FILE contains;
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

