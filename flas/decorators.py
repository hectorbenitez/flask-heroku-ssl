from functools import wraps
import os
from flask import request
from werkzeug.utils import redirect

ssl_required_flag = os.environ.get('SSL_REQUIRED', False) == 'True'

def ssl_required(fn):
	@wraps(fn)
	def decorated_view(*args, **kwargs):
		if ssl_required_flag and not request.is_secure:
			return redirect(request.url.replace("http://", "https://"))
		return fn(*args, **kwargs)

	return decorated_view
