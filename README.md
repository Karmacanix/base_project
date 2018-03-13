create with base django project, a starting django project that has:
- home page with sidebar navigation menu
- identity and access management (allauth)
	- register (includes email verification)
	- log-in
	- log-out
	- reset password
- basic user settings
	- change/add email address(es)
	- change password
- styled with W3 CSS
- basic messaging e.g.: successful login

install instructions (wip: needs to be fleshed out with actual code):
- set-up virtual environment
- download git archive
- install requirements
- set-up super user
- migrate
- run server

notes:
- emails are being sent to the console atm via a dummy backend

usage:
- install base project
- create a new branch to manage code separately
- start/add/develop new apps
- add your new apps template(html pages) urls to the site_base.html side menu so user can navigate to them

edits to allauth:
- change login form (allauth/account/forms.py line 92) to 
		remember = forms.BooleanField(label=_("Remember me?"),
                                  required=False)
- overwrite the templates with your altered templates