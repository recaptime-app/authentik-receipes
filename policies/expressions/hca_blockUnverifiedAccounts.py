# SPDX-License-Identifier: MPL-2.0
# Author: Andrei Jiroh Halili (Recap Time Squad) <ajhalili2006@crew.recaptime.dev>
# Description: Authentik Expression Policy for blocking unverified Hack Club Auth accounts using the verification_status OIDC claim.

# If someone at Hack Club HQ or even us at Recap Time Squad (or simply Andrei Jiroh himself) is signing in via HC Auth,
# just bypass this through the email domain allowlisting. See the Authentik docs for details: https://next.goauthentik.io/customize/policies/expression/whitelist_email/
# Note to those using this: Change allowed_domains values after Hack Club HQ's domain to use yours instead of Recap Time Squad specifics
# or remove them altogether.
allowed_domains = ["hackclub.com","crew.recaptime.dev","andreijiroh.dev"]
current_domain = request.context["prompt_data"]["email"].split("@")[1] if request.context.get("prompt_data", {}).get("email") else None
if current_domain in allowed_domains:
  return ak_is_sso_flow

# Grab verification status OIDC claim from HC Auth first
verified_state = context.get("oauth_userinfo").get("verification_status")

match verified_state:
  case "verified":
    return True
  case "needs_submission":
    ak_message("Complete identity verification first at https://auth.hackclub.com/verifications/new to continue using Hack Club Auth as your signin method.")
    return False
  case "pending":
    ak_message("Your identity verification with Hack Club is currently pending. Try again once you are verified or see https://auth.hackclub.com/docs/contact on how to contact Hack Club regarding identity verification.")
    return False
  case "ineligible":
    ak_message("Looks like either you are ineligible to use Hack Club services (e.g. adult trying to join YSWS programs + events, reported fraud case, misconduct, etc.) or your identity documents are rejected. Try again at https://auth.hackclub.com/verifications/new or see https://auth.hackclub.com/docs/contact on how to contact Hack Club regarding identity verification.")
    return False
