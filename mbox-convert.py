import mailbox
import time
import email
import os
import config
from datetime import datetime
from html2text import html2text

def remove_forwarded_text(text):
    return '\n'.join(line for line in text.split('\n') if not line.strip().startswith('>'))

username = config.username
mbox_file = 'mbox-source/convert-me.mbox'
output_file = 'converted-mbox.md'
unwanted_text = "unsubscribe"

current_timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# output_file = f"{current_timestamp}_{output_file}" # optional to include timestamp

print(f"\n*** Starting conversion at {current_timestamp}")
print(f"Including only 'from:' email addresses that include the string '{username}'")
print(f"Output_file will be: {output_file}\n")

all_mails = mailbox.mbox(mbox_file)
mbox_dict = {}
unsubscribe_count = 0
not_username_count = 0
non_text_messages = 0

for msg in all_mails:
    if msg['from'] and username in msg['from']:
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type in ('text/plain', 'text/html') and not part.get_filename():
                    body = part.get_payload(decode=True).decode(errors='replace')
                    if content_type == 'text/html':
                        body = html2text(body)
                    break
        else:
            content_type = msg.get_content_type()
            if content_type in ('text/plain', 'text/html'):
                body = msg.get_payload(decode=True).decode(errors='replace')
                if content_type == 'text/html':
                    body = html2text(body)

        if not body:
            non_text_messages += 1
            continue

        body = remove_forwarded_text(body)

        if unwanted_text in body or (msg['subject'] and unwanted_text.lower() in str(msg['subject']).lower()):
            unsubscribe_count += 1
        else:
            msg_id = hash(msg['Message-ID'])
            if msg['date']:
                formatted_date = email.utils.parsedate_to_datetime(msg['date']).strftime('%Y-%m-%d_%H-%M-%S')
            else:
                formatted_date = "unknown_date"
            valid_subject = ''.join(c for c in (str(msg['subject']) or '') if c.isalnum() or c.isspace() or c == '_')
            mbox_dict[msg_id] = {'subject': valid_subject, 'to': msg['to'], 'date': formatted_date, 'body': body, 'from': msg['from']}
    else:
        not_username_count += 1

with open(output_file, "a", encoding="utf-8") as f:
    for msg_id, msg_data in mbox_dict.items():
        f.write(f"From: {msg_data['from']}\n")
        f.write(f"Subject: {msg_data['subject']}\n")
        f.write(f"To: {msg_data['to']}\n")
        f.write(f"Date: {msg_data['date']}\n")
        f.write(msg_data['body'])
        f.write("\n")

print(f"\n*** Conversion complete at {datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}")
print(f"Total emails processed: {len(all_mails)}")
print(f"Unsubscribe emails skipped: {unsubscribe_count}")
print(f"Emails not from {username}: {not_username_count}")
print(f"Non-text messages skipped: {non_text_messages}")
