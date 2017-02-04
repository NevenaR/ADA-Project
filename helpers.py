#return maximal number of posts for each year 
def findmax(df_in):
    df=df_in.reset_index()
    years=df_in.index.get_level_values(0).unique()
    maxims=list()
    for x in years:
        max_num=max(df[df['year']==x]['userid'])
        maxims.extend([max_num])
    return maxims

#return names of places given geolocator response
def getPlaceNames(popular_places):
    names=[]
    for x in popular_places:
        try:
            names.extend([x.raw['address']['city']])
        except KeyError:
            try:
                names.extend([x.raw['address']['village']])
            except KeyError:
                    try:
                        names.extend([x.raw['address']['suburb']])
                    except KeyError:
                        names.extend([x.raw['address']['town']])
    return names
    
#retun number of distinct users who at given location in given year
def getNumUsers(x,y,z):
    return rounded_geo[(rounded_geo.lat==x) & (rounded_geo.lon==y) & (rounded_geo.year==z)].groupby("userid").count().shape[0]
    
#return number of occurences of each word in a text
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
    
#return number of occurences of each word in a dataframe column "tags"
def tagFreq(dfm,year=0):   
    string='  '.join(dfm.dropna().tags.values)
    dictionary=word_count(string)
    dfWords=pd.DataFrame.from_dict(dictionary,orient='index')
    dfWords=dfWords.reset_index()
    dfWords=dfWords.rename(columns={'index': 'word', 0: 'freq'})
    dfWords=dfWords.sort(['freq'],ascending=False)
    dfWords = dfWords.reset_index()[['word','freq']]
    if year!=0: dfWords['year']=year
    return dfWords

#return url for given tags (optional: latitute, longitude, year, skip-to return all photos returned by API)
def getUrlForTags(tags_,lati=0,long=0,year=0,skip=0):
    from flickrapi import FlickrAPI

    FLICKR_PUBLIC='5b03e0e556fc96c0ac2bb6256889b4de'
    FLICKR_SECRET = 'f73faeda2b4f164e'

    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
    if(lati!=0): cats = flickr.photos.search(tags = tags_, per_page=55,lat=lati,lon=long,min_taken_date=str(year)+'-01-01',max_taken_date=str(year)+'-12-31',extras=extras, tag_mode='all')
    else: cats = flickr.photos.search(tags = tags, per_page=55, extras=extras,tag_mode='all')
    photos = cats['photos']
    from pprint import pprint
    #print(photos['photo'])
    if(skip!=0): return  photos['photo']
    else: return photos['photo'][0]['url_m']

#return daytime given time
def daytime(x):
    noon= datetime.datetime(1900, 1, 2, 12, 0).time()
    morning=datetime.datetime(1900, 1, 2, 6, 0).time()
    eve=datetime.datetime(1900, 1, 2, 18, 0).time()
    midnight=datetime.datetime(1900, 1, 2, 23,59 ).time()
    if x<noon and x>morning:
        return "morning"
    elif x>noon and x<eve:
        return "afternoon"
    elif x>eve and x<midnight:
        return "evening"
    else:
        return "night"