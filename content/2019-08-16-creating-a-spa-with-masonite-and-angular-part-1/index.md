---
date: 2019-08-16
title: Creating a SPA with Masonite and Angular (Part 1)
cover: ./images/covers/spa-1.webp
categories:
    - Tech
tags:

    - spa

---

It has been a while since I have blogged, but there have been a lot of changes. Mainly, I moved to St. Louis, Missouri for my new job. I love the company ([positronic.ai](https://positronic.ai)), and I love what I do. I have the pleasure of being a machine learning engineer. I am not going to lie, it has been rough. Last May, I graduated with a Masters in Mathematics and I barely new Python. Now, I barely use math, and  I use Python everyday! So besides the Python learning curve (Thankfully, Matlab is very similar in terms of scientific computing functionality so I was not too lost.), overwhelming impostor syndrome (which I will probably write a post on soon), and lack of neural network concepts, one of the biggest hurdles I have had to overcome is learning Javascript, particularly Angular.

Creating machine learning models is great, but you need a way to interact with them. At my company, all developers are expected be &#x27;full-stack&#x27; engineers. Although we might not be experts at it, this flexibility allows us to work on a project from inception to deployment. Say what you want about that policy, being a diverse engineer allows one to be a better programmer.

So, I have had the pleasure (Well, it has been more like torture.) to learn Javascript and Angular for the SPAs we develop for our customers to view their data and make predictions.

From my previous posts, it should be clear that if I have to create an api backend, my go to tech stack is [Masonite](https://docs.masoniteproject.com/). I am an active contributor to the project, and I love to use it when I can. It has enough structure for you to use it out of the box, but it also is flexible enough to allow you to do what you want. Also, it has an amazing community.

One of the best pieces of advice I have received is if you want to learn something, the best way to learn it is put it in practice. If I want to learn JS and Angular better, then I need to implement it myself. My personal website was originally built with Jinja2 templates. Jinja2 is great for static sites, but I needed to practice creating Single Page Applications (SPAs). Thus, I have converted my website to Angular 8, and I was surprised with the responsiveness. With this frontend/backend concept, I figured the complexity would take me a while to figure out, and I was unsure if Heroku would allow me to deploy them both together. Thankfully, I figured it.

In the upcoming days, I will detail how I created the Masonite api backend and the Angular frontend. Stay tuned for more posts!