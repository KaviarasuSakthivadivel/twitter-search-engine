# twitter-search-engine

For server build

1. Install required python modules
   
    `pip3 install django djangorestframework django-cors-headers googletrans==4.0.0-rc1 google-cloud-language pysolr tweepy`

3. Change working directory to `web-server/betasearch`
4. Run `python3 manage.py runserver`

For Client build

1. Change working directory to `client`
2. Install Node version v14
3. Run `npm install` in this folder to initialize node modules or to update packages
4. For development build run `npm run serve`
