---
date: 2018-10-25
title: From Flask to Masonite
author: Tony Hammack
cover: ./images/BLOG_EN_1207_How-to-Make-Your-Computer-Crash-proof.webp
categories:
    - Tech
tags:

    - Masonite

---

I love Python. There, I said it. It is simple and expressive while immensely powerful. I started coding in Visual Basic and C#. From there, I used Matlab for undergrad and graduate school. All the while, Python lurked in the background. It caught my eye the second year of undergrad, but it is easier to manipulate matrices in Matlab. (It is pretty simple to work with matrices in Python, but not as simple!) The more I looked into Python, the more I realized what ALL you can do with it. You can create backends for websites, statistical analysis, create micro-services, work with mathematical data, an os for some IoTs, and other various projects. 

Frameworks like Angular, React, and Vue are immensely powerful. PHP lives on the server, but Javascript lives on the client's browser. This made sense to me. Having a popular website render all the content on the server would create a very high server load. With Google's V8 Javascript engine, I foresaw a new era of programming. Applications would be agnostic of the underlying operating system, but live in the client's browser instead of some GUI app. But, Javascript, just like PHP, is hard to read. All the curly brackets and semicolons are hard to keep up with. I am not saying those languages are bad in some way; they are still very popular languages. And, it would be good for me to learn more about these languages. For my projects, I use no PHP and minimal Javascript. If I need it, I will look to Stack Overflow.

When I heard of a Python web framework named Django, I became extremely excited. I can create websites with Python. How cool! I tried Django, but became overwhelmed with how vast the project was. It does have a steep learning curve, and it did not help I found Django when I was a newbie Python developer. I ditched Django in search of an "easier" framework. I found Flask.

_(Note: I have gotten back into Django; it is not my main backend though. To all of you Django lovers, I have not abandoned you!)_

Flask is nice, it is lightweight and simple. With the help of a tutorial, I can get a site or api up and running in no time. But, I was not satisfied with the way one would build an application. The logic in my code was all intertwined. I ignored the [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter). I did my best to separate the logic through multiple iterations of refactoring my project, and I still was not happy with the result. The thing that irked me the most were the Flask view decorators mixing with controllers. 

I tried to create one application in Flask, but failed miserably. I wanted to create a site where it accessed the NewsApi, weather api, and the Google Calendar api to create a webpage that displayed all the relevant information for that day. The goal was to use this site in the morning when I got up. But, my Flask application was...not good. It was extremely slow and clunky. I wanted to work with a language played nicely with JSON. Naturally, I chose Javascript. I created an Angular web app, and this attempt was successful. I realized I never used this site much so I got rid of it, but I realized something. I really liked the Model-View-Controller (MVC) design of Angular. It just made sense. Keep everything abstracted and then bring it all together at the end. It followed the Law of Demeter.

One day, I listened to [_Podcast.__init__.py_](https://www.podcastinit.com/) and the host had a guy speak about his new framework, [Masonite](https://docs.masoniteproject.com/). I was captivated. Most of the frameworks talked about these days were these hack attempts using `asyncio`. I think async programming and web development go hand in hand (async is a core part of Javascript), but these frameworks jumped onto the async bandwagon. One of the biggest turn offs to these new age frameworks were the lack of documentation. I still had my main Flask site, and I was happy with it. It did what I needed it to do. There was no need for my application to be asynchronous. But, this guy's framework seemed solid. It was written completely in Python 3. Django and Flask still has components and plugins written in Python 2.7. And, it had EXTENSIVE documentation. What got me to look at the Github repo was his mentioning of how Masonite implemented the MVC architecture. 

That night, I decided to try it out. I was completely surprised with how easy everything was. It took me one hour to port all of the functionality of my Flask site to Masonite. (A good chunk of it was me missing with some css files. I found a bug in my site where it was not correctly adjusting to mobile view. But, that is on my end and not Masonite.) This Masonite application served each page twice as fast as the Flask one. It also was half the size of the Flask site. (I host my application on Heroku, and at the time I was on the free plan. I had to keep an eye on the application so that its size did not grow too far. Flask plugins added A LOT of code into my project.) The guy who created Masonite mentioned there was a Slack community channel. I immediately joined that channel and messaged the creator directly. I messaged the creator, [Joseph Mancuso](https://github.com/josephmancuso/), as quickly as possible and told him how happy I was to find his framework. I briefly told him where I came from and my surprise with how fast Masonite was and impressed with the ease of use.

And, I have been an ardent contributor to [Masonite](https://github.com/MasoniteFramework/core) ever since. 

There are an active group of devs working on it just as passionately as I do. Each of them come from different experiences but are amazed with Masonite. Even though the project is really young, it is simple to create complex projects. 

I have a personal Wordpress blog, and I realized if Masonite wanted to become elite, it needed to have a mature blog system. I created [one](https://github.com/hammacktony/masonite-demo-blog) in a week and a half. (A lot of that time was spent on the design of the blog.) It is still being improved each and every day, but it has a lot of the important functionality of the Wordpress blog system. (You can check out the demo at [https://masonite-blog.herokuapp.com/](https://masonite-blog.herokuapp.com/).) 

Each day Joseph is merging pull requests which add big, new features. 

I encourage you to check out [Masonite](https://docs.masoniteproject.com/). It really is a great framework. Masonite 2.1 will be releasing in December. I am proud of the work we have achieved.