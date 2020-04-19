---
date: 2019-08-16
title: Writing a blog with Masonite pt. 1
author: Tony Hammack
cover: ./images/Screenshot-2018-10-28-22.42.16.webp
categories:
    - Tech
tags:

    - Masonite

---

## Introduction

From a previous post ["From Flask to Masonite"](http://www.tonyhammack.com/blog/post/from-flask-to-masonite), I detailed my Python backend journey. As a small fish in a big pond, I jumped in headfirst and attempted to take on Django. It was too big a project for me at the time.. I had no clue what views and controllers were. I was scared of using Models and ORMs. Oh the joys of being young!

I swam to the other end of Python web frameworks - I swam to Flask. It is so easy to understand. You have a pile of clay, and you can make anything you want - Django, not so much.

But, I found my way to the [Masonite Framework](https://docs.masoniteproject.com/). It is simple, yet powerful. I was impressed by the amount of documentation there is. Clearly, the creator understands open source and wants others to contribute to his project. Joseph Mancuso, the creator, heavily emphasizes documentation throughout the source code as well. There are projects I look at on Github which have next to no documentation surrounding classes, methods, functions, etc. As annoying as it is to write up docstrings for obvious functions, I know it is worth it in the long run.

I noticed Masonite does not have native blogging functionality. There are a few things a web framework should have. The ability to host a blog is one of them. 

Modeling Wordpress, in terms of functionality, I created a (near) fully featured blog engine. As most things, it can always be improved. But, it has a lot of features out of the box. 

## Functionality

Before we begin, it is always necessary to create a roadmap for the application we want to create. 

I asked myself the questions: 

- "What is it I want to do to create and update the blog?" 
- "What do I want users to see and interact with?"

On the frontend, I came up with a list of things I wanted to do.

- It should have a main page that listed all posts by title. 
- It should also have the author's name and when it was created and/or updated recently. 
- On the main page, the author's name should be a link to a page where it displays all the posts posted by that author.
- When you click on a post, it should have a featured image (if uploaded). The title should be displayed. 
- The post should render (I'll talk how it loads later.)
-  At the bottom of the page, there should be the ability to display the category this post is in.
-  You should be able to click on the category and be taken to a page listing all the posts in that category.
-  It should have the ability to display a snippet about the author (as a widget). 
-  It should have the ability to display the 5 most recent posts (as a widget).

I came up with another list of things I wanted to do in the backend.

- I want the ability to create, update, preview, and activate posts.
- I want the ability to use Markdown or any other parser to render text to html.
- I want the ability to create a user profile. 

## Roadmap for My Application

First, I will describe how I set up my migrations. Second, I will describe how I coded the backend. Third, I will discuss how I used `Jinja2` to create the frontend. Be prepared for more posts to come!

## Check It Out!

If you want to see the source code for my site, here is my Github [repo](https://github.com/hammacktony/heroku-site). If you want to play with a demo of my blog, checkout [masonite-blog.herokuapp.com](masonite-blog.herokuapp.com). The source code for the demo can be found [here](https://github.com/hammacktony/masonite-demo-blog).

Stay turned for part two of this series!