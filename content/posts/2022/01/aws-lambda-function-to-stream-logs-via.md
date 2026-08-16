---
title: "AWS Lambda: Function to stream logs via SQS"
date: "2022-01-01T22:55:00.007Z"
updated: "2022-01-21T11:00:19.644Z"
legacy_url: "/2022/01/aws-lambda-function-to-stream-logs-via.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-8398212528823179026"
author: "df"
labels:
  - "logstash"
  - "lambda"
  - "sqs"
  - "siem"
  - "aws"
---

<h2>Summary</h2><p>As part of logging and monitoring strategy it is quite important to emit data from AWS services to another service or system or aggregation layer. <a href="https://aws.amazon.com/sqs/" target="_blank">AWS SQS </a>(Amazon Simple Queue Service) is a great tool to communicate between such micro-services with real-time &amp; between software components at any volume.</p><p>Aim of this article is a snippet to stream logs via SQS to an external service (like logstash or siem tools) using Lambda Function</p><h2>Pre-Reqs</h2><p></p><ul><li>Permission to pull data from specific SQS queue</li></ul><p></p><h2>Steps</h2><p></p><ul><li>Ensure lambda function can reach the SQS queue</li><li>Below is a snippet of code to push the data in real-time</li></ul>
<pre><code class="python">
import gzip
import json
import base64
import boto3
import time

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    account = boto3.client('sts').get_caller_identity()['Account']

    queue_url = "https://sqs.eu-west-1.amazonaws.com/12345567928/my-app-{}.fifo".format(account)
    cw_data = event['awslogs']['data']
    compressed_payload = base64.b64decode(cw_data)
    uncompressed_payload = gzip.decompress(compressed_payload)
    payload = json.loads(uncompressed_payload)
    log_events = payload['logEvents']
    log_group = payload['logGroup']
    log_stream = payload['logStream']
    event=    {}
    for log_event in log_events:
        event['AccountID']=account
        event['LogGroup']=log_group
        event['LogStream']=log_stream
        event['Log']=log_event
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageGroupId="my_logging",
            MessageDeduplicationId="%.20f" % time.time(),
            MessageBody=json.dumps(event)
        )
</code>
</pre>
<ul><li>Now pull data using logstash or similar service</li></ul>
<pre><code>
input {
      sqs {
         queue =&gt; "MYQUEUENAME-SQS"
         access_key_id =&gt; "ABCDEFGHIJK"
         secret_access_key =&gt; "WW1123ABCDEFGHIJK"
         region =&gt; "us-west-1"
         proxy_uri =&gt; "https://10.20.30.40:1234"
         id_field =&gt; "sqs_message_id"
         sent_timestamp_field =&gt; "sqs_sent_timestamp"
         add_field =&gt; { "[my][queue]" =&gt; "my-app-queue" }
      }
}

filter {

}

output {
    elasticsearch {
        hosts =&gt; "my_elastic_hostname"
        data_stream =&gt; "true"
    }
}
</code>
</pre>
<div>Please provide your feedback</div><div class="separator"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEheL67AeEQesFCnQbjYtAFsA_hfuGQpsfYx80UwSM0Z_o2I2aIIG18CEmR1S_1jxWpVJ9Eci65Ub5_AjlHH6nRi_QeWnBIuM9bWOBpUNvY8udWYix7bF34G5hKONL4hU6JRrqxWZFK498iRVX_Kn5YoTcYCpRKmfn-gSkcwJh2hvq_CGR8Phlz_RPGL=s1499"><img border="0" data-original-height="894" data-original-width="1499" height="239" src="https://blogger.googleusercontent.com/img/a/AVvXsEheL67AeEQesFCnQbjYtAFsA_hfuGQpsfYx80UwSM0Z_o2I2aIIG18CEmR1S_1jxWpVJ9Eci65Ub5_AjlHH6nRi_QeWnBIuM9bWOBpUNvY8udWYix7bF34G5hKONL4hU6JRrqxWZFK498iRVX_Kn5YoTcYCpRKmfn-gSkcwJh2hvq_CGR8Phlz_RPGL=w400-h239" width="400" /></a></div><br /><div><br /></div><p></p>
