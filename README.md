# Heroku Site

This is a Masonite deployment for Heroku. This site is where I will be showing some of my side projects I am working on.

## Current Projects

##### Comic News
One of my projects is the "Batman Universe Comic News Aggregator." This uses BeautifulSoup4 to scour 3 of the top comic news sites for Batman-related character's articles. It displays the first 3 pages of resulsts of each site.

The seven news sites currently supported: [bleedingcool.com](https://www.bleedingcool.com/), [cbr.com](https://www.cbr.com/category/comics/news/), [comicsbeat.com](http://www.comicsbeat.com/category/news/), [ign.com](http://www.ign.com/articles?tags=news), [nerdist.com](https://nerdist.com/category/comics/), [newsarama.com](https://www.newsarama.com/comics), and [theouthousers.com](http://www.theouthousers.com/index.php/news.html).

This project accesses a Postgres database to receive the output of scraped information. There are also apis so that you can access the scraped news data. 

##### Active Volcanoes
My second project is "An Interactive Map of Active Volcanoes Classified by Last Known Eruption Date." The heavy work to create the map is found [here.](https://github.com/hammacktony/python-projects/tree/master/volcanos)

### Prerequisites

Enter database url for scraped content in an .env environment config file.

### Installing

Install dependencies

```
pipenv install
```

## Deployment

Create Procfile for Heroku deployment
```
touch heroku/Procfile
echo 'web: gunicorn heroku_site.wsgi:application\(\) -b 0.0.0.0:$PORT -w 3' > Procfile
```

## Built With

* [Orator](https://github.com/sdispater/orator) - A lightweigh and fast ActiveRecord ORM
* [Masonite](https://github.com/MasoniteFramework/masonite) - I want to give a shout out to Joseph Mancusco for creating this amazing framework.
I came upon this framework while listening to a podcast that was going over python news. It is extremely lightweight and customizable. It is a MVC, unlike Django.
Also, it is extremely more intuitive.

## Authors

* **Tony Hammack**
[hammacktony](https://github.com/hammacktony/)

## License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details
