import json
from decouple import config as decouple

CLIENT_ID          = json.loads(open('client_secret.json', 'r').read())['web']['client_id']
GOOGLE_API_KEY     = decouple('GOOGLE_API_KEY')

FB_APP_ID          = decouple('FACEBOOK_APP_ID')
FB_GRAPH_URL       = "https://graph.facebook.com"
FB_PERMISSION_URL  = FB_GRAPH_URL + "/%s/permissions"
FB_TOKEN_URL       = FB_GRAPH_URL + "/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&" \
                    "fb_exchange_token=%s"
FB_USER_URL        = FB_GRAPH_URL + "/v2.8/me"
FB_USER_INFO_URL   = FB_USER_URL + "?access_token=%s&fields=name,id,email"
FB_USER_PIC_URL    = FB_USER_URL + "/picture?access_token=%s&redirect=0&height=200&width=200"

MESSAGE_NOT_LOGGED = "You weren't logged in to begin with!"
MESSAGE_LOGOUT     = "You have successfully been logged out."

SCRIPT_FOR_RESTAURANT = """
<script>
    function myFunction() {
        alert(
            'You are not authorized to delete this restaurant. Please create your own restaurant in order to delete.'
        );
    }
</script>
<body onload='myFunction'>"
"""
LOGIN_OUTPUT = """
<h1>Welcome, %s!</h1>
<img src="%s" style="width:300px; height: 300px; border-radius: 150px; -webkit-border-radius: 150px;
-mox-border-radius: 150px;">
"""