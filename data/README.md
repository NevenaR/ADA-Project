In this folder the original data scrapped from Flickr is stored. It is stored in parts because of limitations of data size that can be stored on github. In order to reassemble the data in one csv file that is used in all the notebooks in this project, notebook getData should be run.

The data with cantons is stored in the pickled file for efficiency (since mapping the locations to cantons using geopy showed to be very time consuming). The notebook getCanton is still given for reference in order to reproduce the results.
