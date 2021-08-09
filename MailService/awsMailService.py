import boto3
import os

class EmailSenderAWS:
    """
    This is the email sender class using the AWS SES implementation
    """
         
    def send(self, from_email, to_list, cc_list, bcc_list, subject, text):
        """
        To send mail using AWS SES
        
        params:
            -from_mail
            -to_list
            -cc_list(optional)
            -bcc_list(optional)
            -subject
            -text
        
        return 0 if the sending sucess
        return 1 if the sending failed
        return 5 if the configuration is not complete
        """
        key = os.environ['AWSAccessKeyId']
        secret = os.environ['AWSSecretKey']
                
        if not key or not secret:
            return 5, 'configuration not complete'
        else:
            data={}
            data['ToAddresses']=to_list
            data['CcAddresses'] =cc_list
            data['BccAddresses']=bcc_list

            AWS_REGION = "us-east-2"
            client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id=key, aws_secret_access_key=secret)


            try:
                response = client.send_email(
                    Destination=data,
                    Message={
                        'Body': {
                            'Text': {
                                'Data': text
                            },
                        },
                        'Subject': {
                            'Data': subject
                        },
                    },
                    Source=from_email
                )
            except Exception as e:
                status=1
                # message=e.response['Error']['Message']
                message=str(e)
                
            else:
                status = 0            
                message = response['MessageId']

            print('AWS')
          
            return status, message