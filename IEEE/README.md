#IEEE Journal Scrape API

The script is present in src folder and is called scrape.py.

##REQUIREMENTS
The script uses python 3 as the interpreter.
It requires bs4 and jsone packages pre-installed along with the default packages.

##USAGE
The script currently could be used to scrape any or all journals, information about which is present in the data folder. The script accepts 2-4 parameters.

###How to execute:
python(2) x y [i] [j] 
 - x : The starting index of the journal to be scraped (indexed starting from 1)
 - y : The limiting journal index to be scraped (indexed journal is not scraped)
 - i : Optional parameter. Specifies the Volume number(indexed starting from 1) to start scraping from for the first journal specified by parameter `x`. All the volumes are scraped for the subsequent journals.
 - j : Optional parameter. Specifies the starting Issue number(index starting from 1) for the first volume being scraped. Any further issues are scraped. All other volumes are completely scraped.

As of now there is no provision to scrape from a specific article. The whole
issue will be scraped. In case of connection breaks (due to power cut etc)
you may have to restart the script from an appropriate volume of the journal
being scraped. 

#MORE INFO
NOT APPLICABLE ANYMORE for v2!!

Usually an article is scraped and processed within 25-35 seconds. If the time elapsed since the previous article is much more than that (say > 1-2 minute(s)) it is possible that a connection break occured and you might have to restart the script with appropriate parameters. This efficiency was measured on a MACBOOKPRO 2015 with a 14MbPS connection. Your average access and process time for an article could differ based on the device or network connection load.


Thankyou for using and feel free to flag an issue when faced with one.

#CHANGELOG
v2
 - The IEEE website was revamped and was fetching data dynamically. The source URLs were found and request are made directly to it reducing the data usage and server load. Resposiveness increased.
 - Updated script for python3 instead of python2
 - Provieded option of specifying a specific start issue index
 - Set a addtional 30sec timeout limit to get a response from server
