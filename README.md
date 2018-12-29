# Heroku Site

This is a Masonite deployment for Heroku. My personal site and blog. This is where I will be showing some of my side projects I am working on.

### Installing

Install dependencies

```
pip install -r requirements.txt
```

## Deployment

Create Procfile for Heroku deployment
```
touch heroku/Procfile
echo 'web: gunicorn heroku_site.wsgi:application\(\) -b 0.0.0.0:$PORT -w 3' > Procfile
```

## Built With

* [Orator](https://github.com/sdispater/orator) - A lightweight and fast ActiveRecord ORM
* [Masonite](https://github.com/MasoniteFramework/masonite) - I want to give a shout out to Joseph Mancusco for creating this amazing framework.
I came upon this framework while listening to a podcast that was going over python news. It is extremely lightweight and customizable. It is a MVC, unlike Django.
Also, it is extremely more intuitive.
* [Sentry](https://docs.sentry.io/) Easy error tracking

## Authors

* **Tony Hammack**
[hammacktony](https://github.com/hammacktony/)

## License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details
