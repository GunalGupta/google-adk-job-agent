import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from google.adk.tools import ToolContext

def send_email(subject: str, html_content: str, to_email: str, tool_context: ToolContext) -> str:
    """Sends an email using the Brevo API."""
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = "YOUR_BREVO_API_KEY" 
    
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    sender = {"name": "Job Summary Agent", "email": "testmail@gunalgupta.tech"}
    to = [{"email": to_email, "name": "Recipient"}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        html_content=html_content,
        sender=sender,
        subject=subject
    )
    
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return "Email sent successfully."
    except ApiException as e:
        return f"Failed to send email: {str(e)}"