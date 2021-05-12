from slack_webhook import Slack
import json

webhook = "place_your_slack_webhook_here"

def post_message_to_slack(json_msg):
    slack = Slack(url=webhook)
    slack.post(text='Cloud Watch Alert',
               as_user= True,
               username="Cloud Watch Alerts",
               attachments=[{
                   "fallback": json_msg,
                   "message": json_msg,
                   "color": "danger",
                   "fields": [
                       {
                           "title": "Metric",
                           "value": json_msg['Trigger']['MetricName'],
                           "short": False
                       },
                       {
                           "title": "Status",
                           "value": json_msg['NewStateValue'],
                           "short": True
                       },
                       {
                           "title": "State Change Time",
                           "value": json_msg['StateChangeTime'],
                           "short": True
                       },
                       {
                           "title": "Instance",
                           "value": json_msg['Trigger']['Dimensions'][0]['value'],
                           "short": True
                       },
                       {
                           "title": "Alarm Name",
                           "value": json_msg['AlarmName'],
                           "short": False
                       },
                       {
                           "title": "Reason",
                           "value": json_msg['NewStateReason'],
                           "short": False
                       },
                   ]
               }]
               )

def lambda_handler(event, context):
    sns = event['Records'][0]['body']
    json_msg = json.loads(json.loads(sns)['Message'])
    post_message_to_slack(json_msg)