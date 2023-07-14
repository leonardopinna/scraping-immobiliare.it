# Scraper for Immobiliare.it website

## Description

This is a basic web scraper for the website immobiliare.it, by which you can create a csv file containing title, price and link to the real estate deal of the italian real estate website. Have fun using this application!

## How to use the app

You can fork or download the app with the standard procedure on github. See here for more information: https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives

To launch the app, you can run the command

```
cd <your-folder-path> && python3 main.py
```

You will be asked to input some information in the prompt, like the city you want to scrape or the minimum and maximum price of the houses you want to search.

Then the app will proceed and create a data.csv file in the app folder, which will contain the results of the web scraping. You can find a data.csv example file in this repository.

WARNING: when the app runs a second time, the previous data.csv file will be deleted, so if you want to keep your past search data, you should save the file with a different name or in a different folder.

### Disclaimer

#### No affiliation

I am not affiliated with the immobiliare.it website, the employees and/or the owners and stakeholders of the company that created the website. I do not guarantee that the app will return correct results, or any result at all.

#### Expect some errors to occur (right now or at some point in the future)

You should be warned that at any moment, immobiliare.it could change the HTML rendering of the pages, resulting in a partial or even total disruption of this app functionalities, as it requires i.e. some peculiar class names to retrieve data from HTML scraping that, if changed, cannot be retrieved in any way. In such a case, the code would need to be changed, and I cannot guarantee a fast fix (nor a fix ever) of the problem. You can always open a Issue for this repo, I will gladly try to fix the problem.

#### No investment advice

This disclaimer could be avoided, but I want to make it very clear that by using this app you are not given any financial advice in any way. When you search for a real estate deal, you should be careful in your investment choiches.

## Known problems and solutions

### SSL Certificate Error

You can incur in a "SSL CERTIFICATE ERROR" while running the script. To solve the problem, you can execute the file

```
<path to python3 folder>/Install Certificate.command
```

to solve the issue on MAC.
The problem is related to the certificate of a https request.

##
