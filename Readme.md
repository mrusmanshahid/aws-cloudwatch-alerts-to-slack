# Python script for AWS Lambda to Send Cloudwatch Alerts on Slack

This app delivers cloudwatch alerts to slack using SNS topics subscription.

#### How to deploy?

1. Clone this repository.
2. Compress (.zip) the entire folder.
3. Upload on AWS lambda.
4. Update lambda handler in AWS lambda runtime handler settings to ***lambda.lambda_handler***
5. Deploy lambda
6. Subscribe deployed lambda to cloudwatch alert.
7. We are good! :wave: