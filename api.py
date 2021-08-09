from flask import Flask, jsonify, request
from service import EmailService
from dotenv import load_dotenv

# load environment variables
load_dotenv()

app=Flask(__name__)

@app.route('/emailservice/sendmail',methods=['POST'])
def send_mail():
    """
    Endpoint to send mail

    params:
        -from_email
        -to
        -cc
        -bcc
        -subject
        -text
    """
    data=request.json

    if "from_email" not in data or "subject" not in data or "text" not in data or ("to" not in data and "cc" not in data and "bcc" not in data):
        return jsonify({"error": "missing parameters in request!"}), 400

    else:
        from_mail=data['from_email']

        to_list = None
        cc_list = None
        bcc_list = None
        subject = None
        text = None

        if "to" in data:
            to_list=data['to']
        
        if "cc" in data:
            cc_list=data['cc']

        if "bcc" in data:
            bcc_list=data['bcc']

        if "subject" in data:
            subject=data['subject']

        if "text" in data:
            text=data['text']

        
        status, message = EmailService().send_email(from_mail,to_list,cc_list,bcc_list,subject,text)

    return jsonify({'status':status,'message':message})

if __name__=='__main__':
    app.run()