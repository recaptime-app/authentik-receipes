# SPDX-License-Identifier: MPL-2.0
# Author: Andrei Jiroh Halili (Recap Time Squad) <ajhalili2006@crew.recaptime.dev>
# Description: Collect Hack Club Auth user info and save them as custom attributes for use in Authentik
# Canonical source: https://github.com/recaptime-app/authentik-receipes/blob/main/property_maps/hca_toolkit.py

# Retrieve Hack Club Slack user ID and verification details from OIDC claims provided by HC Auth
# Additional scopes required: slack_id, verification_status
hca_userinfo = {
  "user_id": info.get("sub"),
  "slack_id": info.get("slack_id"),
  "verification_status": info.get("verification_status", "needs_submission"),
  "ysws_eligible": info.get("ysws_eligible", False),
}

# Then pass them to Authentik as custom user attributes.
return {
  #"hackclub_auth": hca_userinfo
  "attributes": {
    "auth.hackclub.com/userinfo": hca_userinfo,
    "idproofstoolkit.recaptime.dev/hackclub_auth/user_id": hca_userinfo.user_id,
    "idproofstoolkit.recaptime.dev/hackclub_auth/verification_status": hca_userinfo.verification_status,
    "idproofstoolkit.recaptime.dev/hackclub_auth/ysws_eligible": hca_userinfo.ysws_eligible
  }
}
