import json
import requests
import os

class EmailSenderMailJet:
    """
    This is the email sender class using the MAILJET implementation
    """

    def send(self,from_mail,to_list,cc_list,bcc_list,subject,text):
        """
        To send mail using Mailjet
        
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
        api_url=os.environ['mailjet_api_url']
        key=os.environ['mailjet_key']
        secret=os.environ['mailjet_secret']
        
        to_address_list = []
        cc_address_list = []
        bcc_address_list = []

        if len(to_list) > 0:
            for to_address in to_list:
                to_address_list.append(
                    {
                        "Email":to_address
                    }
                )
        
        if len(cc_list) > 0:
            for cc_address in cc_list:
                cc_address_list.append(
                    {
                        "Email":cc_address
                    }
                )

        if len(bcc_list) > 0:
            for bcc_address in bcc_list:
                bcc_address_list.append(
                    {
                        "Email":bcc_address
                    }
                )

        mailjet_data = {
            "Messages":[
                {
                    "From":{
                        "Email":from_mail
                    },

                    "To":to_address_list,
                    "Cc":cc_address_list,
                    "Bcc":bcc_address_list,

                    "Subject":subject,
                    "TextPart":text
                }
            ]
        }        

        if not api_url or not key or not secret:
            return 5, 'configuration not complete'
        else:
            response = requests.post(
                api_url,
                auth=(key,secret),
                data=json.dumps(mailjet_data))
                
            if response.ok:
                status = 0
            else:
                status = 1
            message = str(response.content)

            print('MailJet')
                            
            return status, message