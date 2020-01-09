import mailbox
import quopri
from email.header import decode_header

inbox = mailbox.mbox('inbox.mbox')

for message in inbox:
    print(message["to"])
    print(message["from"])
    print(message["subject"])
    print()


def get_subject(subject):
    subject_parts = []
    subjects = decode_header(subject)
    for content, encoding in subjects:
        try:
            subject_parts.append(content.decode(encoding or "utf8"))
        except:
            subject_parts.append(content)

    return "".join(subject_parts)


print(get_subject("=?UTF-8?B?VGhlcmXigJlz?= more to the story"))

parts = {part.get_content_type(): part for part in inbox[0].get_payload()}

plain_content = parts["text/plain"]
html_content = parts["text/html"]

print(plain_content.get_payload())

decoded = quopri.decodestring(plain_content.get_payload())

print(decoded.decode("utf8"))

encoded_html = quopri.decodestring(html_content.get_payload())
# display(HTML(encoded_html.decode("utf8")))
