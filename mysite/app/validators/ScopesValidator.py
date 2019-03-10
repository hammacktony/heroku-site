""" Authenticate user """
import jwt
import pendulum
from masonite.validator import Validator

from api.exceptions import (ApiNotAuthenticated, ExpiredToken, InvalidToken,
                            NoApiTokenFound, PermissionScopeDenied,
                            RateLimitReached)
from config.application import KEY


class ScopesValidator(Validator):
    
    def _fetch_token(self):
        """Gets the token from the request object
        Raises:
            NoApiTokenFound -- Raised if no API token can be located
        Returns:
            string -- Returns the token as a string
        """

        if self.request.input('token'):
            token = self.request.input('token')
        elif self.request.header('HTTP_AUTHORIZATION'):
            token = self.request.header(
                'HTTP_AUTHORIZATION').replace('Basic ', '')
        else:
            raise NoApiTokenFound

        return token

    def _get_token(self):
        """Returns the decrypted string as a dictionary. This method needs to be overwritten on each authentication class.
        
        Returns:
            dict -- Should always return a dictionary
        """

        try:
            return jwt.decode(self._fetch_token(), KEY, algorithms=['HS256'])
        except jwt.DecodeError:
            raise InvalidToken

    def _authenticate(self):
        """Authenticate using a JWT token
        """
        token = self._get_token()
        if pendulum.parse(token['expires']).is_past():
            raise ExpiredToken
        
    def _run_authentication(self):
        """Call the authenticate method and check for any exceptions thrown
        Returns:
            None|dict -- Should return None if a successful authentication or a dictionary with an error if not successfully authenticated
        """

        try:
            return self.request.app().resolve(self._authenticate)
        except ApiNotAuthenticated:
            return {'error': 'token not authenticated'}
        except ExpiredToken:
            return {'error': 'token has expired'}
        except InvalidToken:
            return {'error': 'token is invalid'}
        except NoApiTokenFound:
            return {'error': 'no API token found'}
        except PermissionScopeDenied:
            return {'error': 'token has invalid scope permissions'}
        except RateLimitReached:
            return {'error': 'rate limit reached'}
        except Exception as e:
            raise e
            return {'error': str(e)}

    def validate(self, reference):
        
        # Validate token
        self._run_authentication()

        # If we are authenticated
        try:
            token = self._get_token()
        except Exception:
            return False
        import logging
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        scopes = token.get('scopes')
        logger.debug(scopes)
        if not scopes:
            return False

        if reference in scopes.split(","):
            return True
