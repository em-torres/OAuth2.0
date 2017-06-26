import json
from decouple import config as decouple

CLIENT_ID = json.loads(open('client_secret.json', 'r').read())['web']['client_id']
GOOGLE_API_KEY = decouple('GOOGLE_API_KEY')

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
