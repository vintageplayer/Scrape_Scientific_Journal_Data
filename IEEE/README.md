#IEEE Journal Scrape API

The script is present in src folder and is called scrape.py.

#REQUIREMENTS
The script uses python 2 as the interpreter.
It requires bs4 and json packages pre-installed along with the default packages.

#USAGE
The script currently could be used to scrape any or all journals information
about which is present in the data folder.
The script accepts two-three parameters.
How to execute:

python(2) x y [z]
*x - The starting index of the journal to be scraped (Indexed from 0)
*y - The limiting journal index to be scraped (Indexed journal is not scraped)
*z - Optional parameter. Specifies the Volume number to start scraping from for the first journal(index - x). All the volumes are scraped for the subsequent journals.

As of now there is no provision to scrape from a specific article. The whole
volume will be scraped. In case of connection breaks (due to power cut etc)
you may have to restart the script from an appropriate volume of the journal
being scraped. 

#MORE INFO
Usually an article is scraped and processed within 15-20 seconds. If the time
elapsed since the previous article is much more than that (say > 1 minute) it
is possible that a connection break occured and you might have to restart the
script.


Thankyou for using and feel free to flag an issue when faced with one.


