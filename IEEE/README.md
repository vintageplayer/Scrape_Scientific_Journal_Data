#IEEE Journal Scrape API

The script is present in src folder and is called scrape.py.

##REQUIREMENTS
The script uses python 2 as the interpreter.
It requires bs4 and json packages pre-installed along with the default packages.

##USAGE
The script currently could be used to scrape any or all journals, information about which are present in the data folder. The script accepts two-three parameters.

###How to execute:
python(2) x y [z]
 - x : The starting index of the journal to be scraped (Indexed from 0)
 - y : The limiting journal index to be scraped (Indexed journal is not scraped)
 - z : Optional parameter. Specifies the Volume number(Indexed from 0) to start scraping from for the first journal(index - x). All the volumes are scraped for the subsequent journals.

As of now there is no provision to scrape from a specific article. The whole
volume will be scraped. In case of connection breaks (due to power cut etc)
you may have to restart the script from an appropriate volume of the journal
being scraped. 

#MORE INFO
Usually an article is scraped and processed within 25-35 seconds. If the time elapsed since the previous article is much more than that (say > 1-2 minute(s)) it is possible that a connection break occured and you might have to restart the script with appropriate parameters. This efficiency was measured on a MACBOOKPRO 2015 with a 14MbPS connection. Your average access and process time for an article could differ based on the device or network connection load.


Thankyou for using and feel free to flag an issue when faced with one.


