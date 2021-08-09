import requests
import json
import os


class EmailSenderMandrill:
    """
    This is the email sender class using the MANDRILL implementation
    """

    def send(self, from_email, to_list, cc_list, bcc_list, subject, text):
        """
        To send mail using Mandrill

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
        api_url = os.environ["mandrill_api_url"]
        key = os.environ["mandrill_key"]

        if not api_url or not key:
            return 5, "configuration not complete"
        else:

            to_address_list = []

            if len(to_list) > 0:
                for to_address in to_list:
                    to_address_list.append({"email": to_address, "type": "to"})

            if len(cc_list) > 0:
                for cc_address in cc_list:
                    to_address_list.append({"email": cc_address, "type": "cc"})

            if len(bcc_list) > 0:
                for bcc_address in bcc_list:
                    to_address_list.append({"email": bcc_address, "type": "bcc"})

            mandrill_data = {
                "key": key,
                "message": {
                    "text": text,
                    "subject": subject,
                    "from_email": from_email,
                    "to": to_address_list,
                },
            }

            response = requests.post(api_url, data=json.dumps(mandrill_data))

            if response.ok:
                status = 0
            else:
                status = 1

            message = str(response.content)

            print("Mandrill")

            return status, message
