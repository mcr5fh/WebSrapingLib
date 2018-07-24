# Credentials you get from registering a new application
client_id = '770jc8r54ghlx3'
client_secret = '5B7myRpqsvTv65zf'

# OAuth endpoints given in the LinkedIn API documentation
authorization_base_url = 'https://www.linkedin.com/uas/oauth2/authorization'
token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'

from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
import requests

linkedin = OAuth2Session(
    client_id, redirect_uri='https://www.linkedin.com/developer/apps/5139153/auth')
linkedin = linkedin_compliance_fix(linkedin)

# # Redirect user to LinkedIn for authorization
authorization_url, state = linkedin.authorization_url(authorization_base_url)

# print 'Please go here and authorize,', authorization_url
# session = requests.Session()

# response = session.get(authorization_url)
# print response.__dict__
# print '\n\nLook here! ', response.status_code
# print '\n\nLook here! ', response.history
# print '\n\nLook here! ', response.url
# print '\n\nLook here! ', response.text

# # Get the authorization verifier code from the callback url
# redirect_response = raw_input('Paste the full redirect URL here:')
# linkedin
# # Fetch the access token
# linkedin.fetch_token(token_url, client_secret=client_secret,
#                      authorization_response=response.url)

# # Fetch a protected resource, i.e. user profile
# r = linkedin.get('https://api.linkedin.com/v1/people/~')
# print r.content


import re
import ConfigParser as cp
import urlparse

from linkedin import linkedin
import mechanize
from mechanize import _response
from mechanize import _rfc3986

# Read secrets:
# cfg_file = 'linkedin_config'
# config = cp.ConfigParser()
# config.read(cfg_file)
# if not config.has_section('Secrets'):
#     raise RuntimeError('no secrets specified')
# secrets = {}
# for s in config.items('Secrets'):
#     secrets[s[0]] = s[1]


class MyRedirectHandler(mechanize.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):

        # Code from mechanize._urllib2_fork.HTTPRedirectHandler:
        if 'location' in headers:
            newurl = headers.getheaders('location')[0]
        elif 'uri' in headers:
            newurl = headers.getheaders('uri')[0]
        else:
            return
        newurl = _rfc3986.clean_url(newurl, "latin-1")
        newurl = _rfc3986.urljoin(req.get_full_url(), newurl)

        new = self.redirect_request(req, fp, code, msg, headers, newurl)
        if new is None:
            return

        if hasattr(req, 'redirect_dict'):
            visited = new.redirect_dict = req.redirect_dict
            if (visited.get(newurl, 0) >= self.max_repeats or
                    len(visited) >= self.max_redirections):
                raise HTTPError(req.get_full_url(), code,
                                self.inf_msg + msg, headers, fp)
        else:
            visited = new.redirect_dict = req.redirect_dict = {}
        visited[newurl] = visited.get(newurl, 0) + 1

        fp.read()
        fp.close()

        # If the redirected URL doesn't match
        new_url = new.get_full_url()
        if not re.search('^http(?:s)?\:\/\/.*www\.linkedin\.com', new_url):
            return _response.make_response('', headers.items(), new_url, 200, 'OK')
        else:
            return self.parent.open(new)

    http_error_301 = http_error_303 = http_error_307 = http_error_302
    http_error_refresh = http_error_302


# Set up headless browser:
br = mechanize.Browser()
br.set_cookiejar(mechanize.CookieJar())
br.handler_classes['_redirect'] = MyRedirectHandler
br.set_handle_redirect(True)
br.set_handle_robots(False)

client_id = '770jc8r54ghlx3'
client_secret = '5B7myRpqsvTv65zf'

return_uri = 'http://127.0.0.1:8080'

auth = linkedin.LinkedInAuthentication(client_id,
                                       client_secret,
                                       return_uri,
                                       linkedin.PERMISSIONS.enums.values())

br.open(authorization_url)
br.select_form(nr=0)
br.form['session_key'] = "mcr5fh@virginia.edu"
br.form['session_password'] = "Googler95!"
r = br.submit()

# auth.authorization_code = urlparse.parse_qs(
#     urlparse.urlsplit(r.geturl()).query)['code']
access_token = auth.get_access_token()
print linkedin.get_access_token()
linkedin.fetch_token(token_url, client_secret=client_secret,
                     authorization_response=r.geturl())

# Fetch a protected resource, i.e. user profile
r = linkedin.get('https://api.linkedin.com/v1/people/~')
print r.content
