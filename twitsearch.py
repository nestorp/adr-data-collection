from twython import Twython

def processtweet(data):
    with open('twittersearch.txt', 'a', encoding='UTF-8') as twitstream:
            if 'text' in data and 'retweeted_status' not in data:
                if data['lang']=='en':
                    if data['truncated']==True:
                        if not "http" in data['full_text'].lower():
                            if not "trump" in data['full_text'].lower():
                                if not "obama" in data['full_text'].lower():
                                    print(data['id'], data['user']['id'], data['user']['screen_name'],data['created_at'],data['full_text'])
                                    twitstream.write(data['id_str']+'|'+ data['user']['id_str']+'|'+data['user']['screen_name']+'|'+data['created_at']+'|'+data['full_text'].replace('\n', ' ').replace('\r', '').replace('|', '').strip()+'\n')
                    else:
                        if not "http" in data['text'].lower():
                            if not "trump" in data['text'].lower():
                                if not "obama" in data['text'].lower():
                                    print(data['id'], data['user']['id'], data['user']['screen_name'],data['created_at'],data['text'])
                                    twitstream.write(data['id_str']+'|'+ data['user']['id_str']+'|'+data['user']['screen_name']+'|'+data['created_at']+'|'+data['text'].replace('\n', ' ').replace('\r', '').replace('|', '').strip()+'\n')

        
mykeys=[]
with open("keys.txt") as instream:
    for line in instream:
        mykeys.append(line)
        
APP_KEY = mykeys[0].rstrip()
APP_SECRET = mykeys[1].rstrip()
OAUTH_TOKEN = mykeys[2].rstrip()
OAUTH_TOKEN_SECRET = mykeys[3].rstrip()

drugs=['abilify','alprazolam','amitriptyline','aplenzin','aripiprazole','atenolol','ativan',
'budeprion','bupropion','buspar','buspirone','celexa','citalopram','clonazepam','clonidine',
'cymbalta','deplin','desvenlafaxine','desyrel','diazepam','doxepin','duloxetine','effexor',
'escitalopram','fetzima','fluoxetine','forfivo','gabapentin','hydroxyzine','lamotrigine ',
'lexapro','librium','lorazepam','methylphenidate','mirtazapine','nortriptyline','olanzapine ',
'oleptro','paroxetine','paxil','pristiq','propranolol','prozac','quetiapine','remeron','seroquel',
'sertraline','tenormin','tramadol','trazodone','trintellix','valium','venlafaxine','viibryd',
'vistaril','wellbutrin','xanax','zoloft','zyprexa']


tw_auth = Twython(APP_KEY, APP_SECRET, oauth_version=2)
token = tw_auth.obtain_access_token()
twitter = Twython(APP_KEY, access_token=token)

#twitter = Twython(APP_KEY, APP_SECRET,
                    #OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
       
results = twitter.cursor(twitter.search, q=drugs, count='100', result_type='recent', lang='en', tweet_mode='extended')
for result in results:
    print(result)
    processtweet(result)