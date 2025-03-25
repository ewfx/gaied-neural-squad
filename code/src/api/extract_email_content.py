import email
import io
from email import policy
from email.parser import BytesParser

def extract_eml_content(file_obj: io.BytesIO):
    # Parse the email file from memory
    msg = BytesParser(policy=policy.default).parse(file_obj)

    email_text = ""
    attachments = []

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = part.get_content_disposition()

            # Extract plain text content
            if content_type.startswith("text/plain") and content_disposition is None:
                email_text += part.get_payload(decode=True).decode(part.get_content_charset(), errors="ignore") + "\n"
            # Extract attachments
            elif content_disposition == "attachment":
                filename = part.get_filename()
                file_content = io.BytesIO(part.get_payload(decode=True))  # Keep attachment in memory
                
                file_text = None
                
                if filename.endswith(".txt"):
                    file_text = file_content.read().decode("utf-8", errors="ignore")
                attachments.append((filename, file_text))
    else:
        email_text = msg.get_payload(decode=True).decode(msg.get_content_charset(), errors="ignore")

    return {"text": email_text.strip(), "attachments": attachments}
