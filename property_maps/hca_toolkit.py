# SPDX-License-Identifier: MPL-2.0
# Author: Andrei Jiroh Halili (Recap Time Squad) <ajhalili2006@crew.recaptime.dev>
# Description: Collect Hack Club Auth user info and save them as custom attributes for use in Authentik

# Retrieve Hack Club Slack user ID from OIDC claims
# Additional scopes required: slack_id, verification_status
hca_userinfo = {
  "user_id": info.get("sub"),
  "slack_id": info.get("slack_id"),
  "verification_status": info.get("verification_status", "needs_submission"),
  "ysws_eligible": info.get("ysws_eligible", False),
}

return {
  "attributes": {
    "auth.hackclub.com/userinfo": hca_userinfo,
    "idproofstoolkit.recaptime.dev/hackclub_auth/verification_status": hca_userinfo.verification_status,
  }
}
