''' A Controller for Dashboard Profiles '''
from app.User import User
from masonite.auth import Auth
from masonite.helpers import password as bcrypt_password
from masonite.view import View
from masonite.request import Request
from masonite.managers import UploadManager
from lib.helpers.DashboardHelper import remove_whitespaces

	
class ProfileController:

	def __init__(self):
		pass

	def show(self, request: Request, view: View):
		""" Controller to show user profile page """


		return view.render('dashboard/user/profile', {'Auth': Auth(request)})
	
	def store(self, request: Request, upload: UploadManager, view: View):
		""" Store user profile information """


		# Get current user
		user = User.where('user_name', Auth(request).user().user_name).get()

		# Update user info
		user[0].name = remove_whitespaces(request.input('name'))
		user[0].website = remove_whitespaces(request.input('website'))
		user[0].linkedin = remove_whitespaces(request.input('linkedin'))
		user[0].twitter = remove_whitespaces(request.input('twitter'))
		user[0].facebook = remove_whitespaces(request.input('facebook'))
		user[0].github = remove_whitespaces(request.input('github'))
		user[0].gitlab = remove_whitespaces(request.input('gitlab'))
		user[0].devto = remove_whitespaces(request.input('devto'))
		user[0].bio = remove_whitespaces(request.input('bio'))

		# Save image
		try:
			image = upload.driver('s3').store_prepend(request.input('file_upload'), 'user/img/')
			user[0].image = image
		except AttributeError:
			# If user did not pick image, check and see if there was a previous image. 
			if user[0].image != "":
				pass

		# Update user info
		user[0].save()

		return view.render('dashboard/user/profile', {'Auth': Auth(request)})

