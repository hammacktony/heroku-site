---
date: 2019-08-16
title: Using Rollbar for Error Catching
author: Tony Hammack
cover: ./images/Screenshot-2018-10-29-11.15.23.webp
categories:
    - Tech
tags:

    - Masonite

---

## Introduction

- Have you ever had your application stop because of an error? 
- Did your application not perform a certain, critical function because of a bug you did not know existed?

If you have said yes to at least one of the above, you know how frustrating it is when you application fails and you did not catch the bug. Errors are thrown all the time, and it is important for you, the developer, to deal with them in a timely manner. 

Rollbar is a great way to catch errors. It can automatically catch them and post the name of the error and all relevant information to an online dashboard for you and your team to analyze. It will email you as well when an error was thrown.

For web frameworks, it is imperative to catch errors. 500 errors provide little to no information, and it is near impossible (given limited time) to find the cause of the bug. Thankfully with [Masonite Framework Hooks](https://docs.masoniteproject.com/useful-features/framework-hooks), it is easy to catch errors when they are thrown. 

## Getting a Rollbar Access Token

When you signup for Rollbar, you will be given an access token. This token allows your application to send errors to your Rollbar account. 

Keep this token in a safe place, you will need it soon.

## Creating the Rollbar Hook

To use Rollbar with Python, we need to download the Python-SDK. 

We can install this SDK with `pip install rollbar`. 

_More information on Rollbar's Python-SDK can be found [here](https://docs.rollbar.com/docs/python)._


First, we need to create a `hooks` folder in our `app` directory. Next in our favorite text editor or IDE, we need to create a class called `RollbarHook` and place it in `app/hooks/rollbar.py`. 

```python

''' Rollbar Hook '''
import rollbar

rollbar.init(Your_Access_Token)

class RollbarHook:
    def __init__(self):
        pass
    
    def load(self, app):
        rollbar.report_exc_info()

```

Every hook requires a `load` method, and it requires the service container (`app`) be passed as a parameter. But for this example, this parameter is not needed.

`rollbar.init('Your_Access_Token')` initializes the rollbar instance. The `report_exc_info()` function captures the entire stack trace when the error is thrown.

## Adding Rollbar to the Container

Now, we need to add the Rollbar Hook to the service container. Adding third party features to the service container is as simple as creating a new provider. 

To create a provider for custom framework hooks, enter `craft provider HookProvider`. This will create a new provider inside `app/providers/HookProvider.py` that looks like:

```python

from masonite.provider import ServiceProvider
​
class RollbarServiceProvider(ServiceProvider):
    def register(self): 
        pass
​
    def boot(self): 
        pass

```

Now, we just add our hook to it:

```python

from masonite.provider import ServiceProvider
from app.hooks.rollbar import RollbarHook
​
class RollbarServiceProvider(ServiceProvider):
    def register(self): 
        self.app.bind('RollbarExceptionHook', RollbarHook())
​
    def boot(self): 
        pass

```

For the final step, we need to register this provider to the `PROVIDERS` constant in `config/providers.py`file via: 

```python

from app.providers.RollbarServiceProvider import RollbarServiceProvider
...
UserModelProvider,
MiddlewareProvider,
​
RollbarServiceProvider,
...

```

## Conclusion

Boom! We now have added automatic error catching via Rollbar to our Masonite project. 

Also, it is pretty simple to extend Masonite, especially with Framework Hooks. 

If you want to know more about Masonite, check out the [documentation](https://docs.masoniteproject.com/). If you want to see how an example of Rollbar in a Masonite application, checkout my [repo](https://github.com/hammacktony/heroku-site) for [tonyhammack.com](tonyhammack.com).
 
Have fun using Masonite!