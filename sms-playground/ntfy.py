# install the app on your phone called nfty
# create a topic that is hard to guess because this where you get your message and its not password protected
import requests

# requests.post("https://ntfy.sh/jimwelllife",
#               data="Backup successful 😀".encode(encoding='utf-8'))

requests.post("https://ntfy.sh/jimwelllife",
              data="Please read this is important",
              headers={
                  "Title": "Priority notification!!!",
                  "Priority": "urgent",
                  "Tags": "warning,skull"
              })
