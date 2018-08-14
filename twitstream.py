from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    
    def on_success(self, data):
        with open('twitterstream_druglist.txt', 'a', encoding='UTF-8') as twitstream:
            if 'text' in data and 'retweeted_status' not in data:
                if data['lang']=='en':
                    if data['truncated']==True:
                        if not "http" in data['extended_tweet']['full_text'].lower():
                            if not "trump" in data['extended_tweet']['full_text'].lower():
                                if not "obama" in data['extended_tweet']['full_text'].lower():
                                    print(data['id'], data['user']['id'], data['user']['screen_name'],data['created_at'],data['extended_tweet']['full_text'])
                                    twitstream.write(data['id_str']+'|'+ data['user']['id_str']+'|'+data['user']['screen_name']+'|'+data['created_at']+'|'+data['extended_tweet']['full_text'].replace('\n', ' ').replace('\r', '').replace('|', '').strip()+'\n')
                    else:
                        if not "http" in data['text'].lower():
                            if not "trump" in data['text'].lower():
                                if not "obama" in data['text'].lower():
                                    print(data['id'], data['user']['id'], data['user']['screen_name'],data['created_at'],data['text'])
                                    twitstream.write(data['id_str']+'|'+ data['user']['id_str']+'|'+data['user']['screen_name']+'|'+data['created_at']+'|'+data['text'].replace('\n', ' ').replace('\r', '').replace('|', '').strip()+'\n')

    def on_error(self, status_code, data):
        print(status_code)
        
mykeys=[]
with open("keys.txt") as instream:
    for line in instream:
        mykeys.append(line)
        
APP_KEY = mykeys[0].rstrip()
APP_SECRET = mykeys[1].rstrip()
OAUTH_TOKEN = mykeys[2].rstrip()
OAUTH_TOKEN_SECRET = mykeys[3].rstrip()

drugs =['cymbalta','zoloft','lexapro','bupropion','prozac','sertraline','celexa','citalopram','wellbutrin xl','fluoxetine',
'abilify','wellbutrin','xanax','effexor','effexor xr','venlafaxine','escitalopram','pristiq','duloxetine','paxil','trazodone',
'mirtazapine','wellbutrin sr','remeron','paroxetine','viibryd','amitriptyline','alprazolam','seroquel','seroquel xr',
'deplin','lamotrigine','zyprexa','aripiprazole','nortriptyline','quetiapine','tramadol','desyrel','fetzima','trintellix',
'alprazolam intensol','budeprion','budeprion sr','budeprion xl','olanzapine','oleptro','aplenzin','desvenlafaxine','dividose',
'desyrel dividose','doxepin','forfivo','forfivo xl','methylphenidate','niravam','paxil cr','risperidone',
'serzone','desipramine','fluvoxamine','imipramine','irenka','rapiflux','vortioxetine','amoxapine','asendin','clomipramine',
'emsam','methylfolate','l-methylfolate','methylin','methylin er','modafinil','nardil','nefazodone','niacin','pamelor',
'parnate','pexeva','remeron soltab','sinequan','symbyax','vilazodone','zydis','zyprexa zydis','abilify ','mycite',
'abilify mycite','chlordiazepoxide','perphenazine','anafranil','armodafinil','atomoxetine','aventyl','aventyl hydrochloride','brexpiprazole',
'fluoxetine','levomilnacipran','limbitrol','limbitrol ds','norpramin','paliperidone','phenelzine','rexulti','selegiline',
'tofranil','tranylcypromine','duo-vil','etrafon','etrafon forte','isocarboxazid','khedezla','l-methylfolate formula','l-methylfolate forte',
'lisdexamfetamine','ludiomil','maprotiline','marplan','protriptyline','surmontil','tofranil-pm','triavil','trimipramine',
'vivactil','xaquil','xaquil xr','clonazepam','ativan','lorazepam','buspar','buspirone','valium','hydroxyzine',
'diazepam','cymbalta','vistaril','gabapentin','propranolol','clonidine','tenormin','atenolol','librium','tranxene',
'lorazepam intensol','diazepam intensol','clorazepate','oxazepam','diastat','diastat acudial','diastat pediatric','oxcarbazepine',
'prochlorperazine','vanspar','corgard','nadolol','phenytoin','stelazine','meprobamate','equagesic','micrainin',
'tranxene t','tranxene t-tab','trifluoperazine'
]

       
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track=smaller_drugs)