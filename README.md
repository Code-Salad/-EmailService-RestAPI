# EmailService-RestAPI

RESTful API that accepts the necessary information and sends emails. If one of the services goes down, it can quickly failover to a another provider without affecting your customers.

Email service currently supported are:
- MailJet
- AWS SES
- Mandrill

Endpoint URL
-----------
```
/emailservice/sendemail
```
It is a REST API. It is accessible through HTTP POST requests, expecting a JSON object as input. And it will return an object as output too.


Sample input json:
```
{
    'from':'test_from@mail.com',
    'to':['test_to1@mail.com, test_to2@mail.com'],
    'cc':'test_cc@mail.com',
    'bcc':['test_bcc1@mail.com', 'test_bcc2@mail.com'],
    'subject':'test subject',
    'text':'This is the test text as the email content. Again, this is the test text as the email content.'
}
```

Error Codes
-----------
status code | message
----------- | -------
0           | success
1           | from email address invalid
2           | to/cc/bcc email address invalid
3           | subject and text both are empty
4           | all email sender failed
5           | email provider configuration not complete
