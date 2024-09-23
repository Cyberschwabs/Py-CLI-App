from dotenv import load_dotenv

import app as rcapp
import sys,os
from dotenv import load_dotenv
from ringcentral import SDK

load_dotenv(".env")

# Info to Sign Into RC API
RC_CLIENT_ID_TEST       = os.getenv("RC_CLIENT_ID_TEST")
RC_CLIENT_SECRET_TEST   = os.getenv("RC_CLIENT_SECRET_TEST")
RC_SERVER_URL_TEST      = os.getenv("RC_SERVER_URL_TEST")
accountId_TEST          = os.getenv("accountId_TEST")
RC_JWT_TEST             = os.getenv("RC_JWT_TEST")

# Login to RingCentral Platform with JWT
rcsdk = SDK((RC_CLIENT_ID_TEST),
            (RC_CLIENT_SECRET_TEST),
            (RC_SERVER_URL_TEST))
platform = rcsdk.platform()
accountId = (accountId_TEST)
try:
    platform.login(jwt=(RC_JWT_TEST))
except Exception as e:
    sys.exit("Unable to authenticate to platform. Check credentials." + str(e))

print(f'Login with JWT successful.')

