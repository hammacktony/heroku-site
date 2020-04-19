---
date: 2019-08-16
title: Creating a Bitly Driver for Masonite
author: Tony Hammack
cover: ./images/Screen-Shot-2018-12-31-at-11.57.06-AM.webp
categories:
    - Tech
tags:

    - Masonite

---

## Introduction

My website, [tonyhammack.com](tonyhammack.com), is a Python powered website. Django is probably the most famous Python web framework with Flask coming in second. The first iteration of my site was in Flask. I found the Masonite project one day and immediately made the [switch](http://www.tonyhammack.com/blog/tech/post/from-flask-to-masonite) to it.

This project heavily uses common software design patterns. These patterns were made the most famous by the [Gang of Four](https://en.wikipedia.org/wiki/Design_Patterns). These four engineers realized most solutions to different applications followed basic patterns. Thus, they wrote down their knowledge for time immemorial. Masonite is built with these patterns for readability, stability, and ease of contribution - if other software developers wanted to contribute, they can easily follow predefined patterns and integrate their solutions quickly. 

Masonite uses [managers](https://docs.masoniteproject.com/v/v2.0/managers-and-drivers/about-managers), [drivers](https://docs.masoniteproject.com/v/v2.0/managers-and-drivers/about-drivers), and [contracts](https://docs.masoniteproject.com/v/v2.0/managers-and-drivers/contracts) for easily extending their applications. These managers come from the Manager pattern (or Builder Pattern). Think of the Manager Pattern as attaching a manager to a specific feature (driver). This manager is responsible for instantiating driver classes. Drivers are simply extensions to features that are managed by the Manager Pattern. And, the documentation describes "contracts are used when creating drivers to ensure they conform to Masonite requirements. They are a form of interface in other languages where the child class is required to have the minimum number of methods needed for that driver to work. It is a promise to the class that it has the exact methods required. Contracts are designed to follow the 'code to an interface and not an implementation' rule. While this rule is followed, all drivers of the same type are swappable."


## The Problem

With Masonite, I have created a blogging system. (I will detail this process in future posts.) I wanted a way to create short links for these articles automatically for sharing on social media. Instead of going to either `bit.ly` or `goog.l` and manually entering the url of the post, I want to create these on the fly and save them in the database. This is a great use case for creating a custom driver.

But, what if I wanted to use a couple different short link creators? Would I have to reimplement a new solution each time I wanted to use a different service? No! That is the beauty of managers and drivers. A manager is used by the programmer as the frontward facing part of the implementation while the specific implementation is done by the driver. Each manager manages different drivers, so us -- the programmer -- does not have to care about the nuts and bolts. I want to be able to use `bit.ly`, `goog.l`, or some custom implementation to create short links. A manager will simplify implementing these solutions.

---

Note I am using Masonite 2.0.36. Masonite just released version 2.1 earlier this month. When I upgrade to 2.1 one, I will update this post accordingly.

---

## Creating the Config File

To create a driver for the `bit.ly` service, you will need a few things. You will need to create an account with `bit.ly` and obtain an access token. This token will be used to authenticate that you are a user with `bit.ly`. It is imperative you keep this token in a safe place. A good option is the `.env` file. 

For our `bit.ly` driver, we must be able to access the access token. This configuration is stored in `config/urlshortener.py`. This is also where you might store other config variables for other url shortener drivers. Here is a sample of my file -- feel free to copy it.

```
DRIVER = os.getenv('URL_SHORTENER', 'bitly')

URL_SHORTENER = {
    "bitly": {
        "token": os.getenv("BITLY_API_TOKEN", None)
    }
}
```

`DRIVER` just denotes the default driver.


## Creating the Manager

This manager will manage all url shorteners we decide to use. 

Managers can go anywhere in our application, but I have placed mine in `app/managers`. In this folder, I created a file named `UrlShortenerManager.py`. Make sure you keep your naming consistent, this is important in the future. 

You only need to import one module in this file -- the default manager class in Masonite. Each custom manager is a subclass of this default manager. Each manager requires two fields `config` and `driver_prefix`. `config` is where the manager looks for configuration variables (like the `bit.ly` access token).
`driver_prefix` is just for consistency. All drivers will have the form `UrlShortener~~~~Driver.py`. 

So, our manager will look like: 

```
""" Manger for Url Shorteners """
from masonite.managers import Manager

class UrlShortenerManager(Manager):
    
    config = 'UrlShortenerConfig'
    driver_prefix = 'UrlShortener'
```

And there you go, we have created our own custom manager

## Creating the Contract

In `app/contracts`, I created a contract for our driver called `UrlShortenerContract`. This contract has one method called `shorten`. All url shorteners we create must have this one method. Just by the name, it makes sense why we have it. This method will create our shortened link.

```
""" Url Shortener Contract """
from abc import ABC, abstractmethod


class UrlShortenerContract(ABC):

    @abstractmethod
    def shorten(self):
        """ Shorten Urls """

```


## Creating the Driver

You will also need the api endpoint that you will send your REST request to. This link is `https://api-ssl.bitly.com/v4/bitlinks`. Now that we have what we need from `bit.ly`, we can create the driver.

Drivers can go anywhere in our application, but I have placed mine in `app/drivers`. In this folder, I created a file named `UrlShortenerBitlyDriver.py`. Make sure you keep your naming consistent, this is important in the future. 

Just like our custom manager, our custom driver is a subclass of the `BaseDriver` in Masonite. It is also a subclass of our `UrlShortenerContract`. The only outside dependency we need is `requests`. We will use this to send a POST request to the `bit.ly` api.

Here is the setup for our driver:

```
class UrlShortenerBitlyDriver(UrlShortenerContract, BaseDriver):
    """Bitly Url Shortener driver."""

    # Source: https://dev.bitly.com/v4_documentation.html

    def __init__(self, UrlShortenerConfig):
        """ Url Shortener Driver Constructor
        Arguments:
            url_shortener {masonite.managers.UrlShortenerManager}
               -- The URL Shortener Manager object.
            UrlShortenerConfig {config.urlshortener} 
               -- Url shortener config  configuration.
        """
        self.config = UrlShortenerConfig.URL_SHORTENER
```

Note, in our `__init__(self)` method, we have an attribute called `self.config`. This attribute loads all configuration variables in our `config.urlshortener` file. 

Now for the fun part...the `shorten` method.

Here is the method: 

```
def shorten(self, **payload):
        """ Bitly Url Shortener 
        
        args
            **payload {dict} - json payload for api

        returns
            response {dict} - json response of query
        """

        # Bitly Api Endpoint
        api = "https://api-ssl.bitly.com/v4/bitlinks"

        # Headers for Bitly authorization (uses OAuth Token) 
        headers = {'Authorization': 'Bearer 
        	{token}'.format(token=self.config["bitly"]["token"])}

        r = requests.post(url=api, headers=headers, json=payload)

        # Appened status code to response
        status_code = {'status_code': r.status_code}
        response = {**r.json(), **status_code}
        return response
```

Notice how this method takes in `**payload`. These are just keyword arguments for our json response. All arguments can be found in the [bit.ly documentation](https://dev.bitly.com/v4_documentation.html). The only one we are most interested in is the `long_url` argument. This is the link we want to shorten. Notice the `headers` dictionary. The access token is placed in the header of our request to grant access to their services.

The json response we get from `bit.ly` contains the shortened url and other interesting information. I have add the status code of the request for debugging purposes.

## Creating the Provider

Masonite is built around something called a Service Container. Think of this container as a dictionary to store all necessary components you need for your application. This central repository distinguishes Masonite from Flask or Django. To read more in depth about the container, read the [documentation](https://docs.masoniteproject.com/v/v2.0/architectural-concepts/service-container).

To utilize the container and the drivers our application, we must create a service provider. Service providers add new objects into the container for future use. In `app/providers`, we need to create a service provider called `UrlShortenerProvider`. As in all custom providers, this is a subclass of the default provider in Masonite, `ServiceProvider`. 

Let's look at the provider and go over it in detail. 

```
class UrlShortenerProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UrlShortenerConfig', urlshortener)
        self.app.bind('UrlShortenerBitlyDriver', UrlShortenerBitlyDriver)
        self.app.bind('UrlShortenerManager', UrlShortenerManager(self.app))

    def boot(self, UrlShortenerConfig, UrlShortenerManager):
        self.app.bind('UrlShortener', 
        	UrlShortenerManager.driver(
        		self.app.make('UrlShortenerConfig').DRIVER))
```

`wsgi=False` just means this provider needs to be started only at the application's initiation instead of being started on each request.

First, we bind the url shortener config into the container with its custom name. Then we bind the driver and manager into the container. Lastly, to create this driver, we need to utilize the `boot` method. This just links the manager to the driver with the driver's specific configuration. If we had more drivers, we would continue this process.

Lastly, we need to register this provider. In `config/providers.py`, import this provider and add it to the list of providers that are to be used.

Thus, we can now use the manager `UrlShortener` as the front facing part of the driver. We can use this anywhere in our application. 

## An Example

In the `create` method of the `BlogEditorController`, I have the `UrlShortener` as a parameter. 

```
...    
def create(self, Request, Upload, UrlShortener):
...
```

This lets the application know we need to get `UrlShortener` from the container to use. 

Now we can use this anywhere in our method.

When I create a post, I grab the title of the post and create a slug for it. This slug is used to create the long-form url of the post. Then, I shorten this url and obtain the `bit.ly` response. If something is wrong, then the short link is an empty string. If it exists, I add it into the database and it is displayed in the dashboard to be able to copy and past into either facebook, twitter, or some other site. 

```
		 # Create slug
        slug = slugify(remove_whitespaces(Request.input('title')))

        # Get full url of article
        url = "http://www.tonyhammack.com/blog/{blog}/post/{slug}".format(
            blog=self.blog_name, slug=slug)

        # Create shortened link for sharing
        shortened_url = UrlShortener.shorten(long_url=url)
        try:
            link = shortened_url["link"]
        except KeyError:
            link = None
```

(`self.blog_name` is just the current name of the blog I am working on. I have two blogs, and this allows me to have one controller for manage both blogs.)

## Conclusion

Extending Masonite is pretty simple. Once you understand how managers and drivers interact, creating new functionality is easy. If you have anymore questions about Masonite and its patterns, I would check out its [documentation](https://docs.masoniteproject.com/v/v2.0/).

Otherwise, feel free to check out my [repo](https://github.com/hammacktony/heroku-site) for guidance.