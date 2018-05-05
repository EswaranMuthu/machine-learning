import os
import json
import csv
from pandas.io.json import json_normalize
import pandas as pd
import re
#path = 'c:\\Users\\eswaran.muthu\\Desktop\\IOT'
path = 'c:\\Users\\eswaran.muthu\\Desktop\\IOT\\metrics\\bdbio\\processed'
with open('c:\\Users\\eswaran.muthu\Desktop\\publications.csv', "w+", newline='') as pubs, open('c:\\Users\\eswaran.muthu\Desktop\\dilutions.csv', "w+", newline='') as dils:
    fieldnames_dils = ['sku','application','dilution']
    fieldnames_pubs = ['sku','title', 'pubMedURL']
    header = csv.writer(dils)
    header.writerow(fieldnames_dils)
    header = csv.writer(pubs)
    header.writerow(fieldnames_pubs)
    good_pub = 0
    missing_pub = 0
    good_dil = 0
    missing_dil = 0
    for filename in os.listdir(path):
        with open(path+'\\'+filename, encoding='utf-8', errors='ignore' ) as openfile:
            y = json.load(openfile)
            if 'Catalog' in y['specifications']:
                if 'Catalog No.' in y['specifications']['Catalog']:
                    sku = y['specifications']['Catalog']['Catalog No.']
            if 'publications' in y:
                    pub_array = json_normalize(y,'publications')
                    pub_array = pub_array.astype(str)
                    pub_array['sku'] = sku#.replace("-","")
                    '''if 'url' in y['publications']:
                        pub_array = pub_array[['sku','title','url']]
                    else:
                         pub_array = pub_array[['sku','title']]'''
                    pub_array['title'] = pub_array['title'].map(lambda x: x.encode('unicode-escape').decode('utf-8'))
                    pub_array.to_csv(pubs, header=False, index=False, encoding='utf-8')
                #no dilutions in BD
            '''if 'Dilutions'in y['specifications']:
                dil_obj = y['specifications']['Dilutions']
                r = re.compile('([a-zA-Z\-\s\/]+)([0-9:\-\sngug\/ml]+)?')
                m = r.findall(dil_obj)
                dil_array = pd.DataFrame(m, columns=['application','dilution'])
                dil_array['sku'] = sku.replace("-","")
                dil_array = dil_array[['sku','application','dilution']]
                dil_array.to_csv(dils, header=False, index=False, encoding='utf-8')
                good_dil = good_dil + 1
            else:
                missing_dil = missing_dil + 1'''
    print('count good dil:', good_dil)
    print('count bad dil:', missing_dil)
    print('count good pub:', good_pub)
    print('count bad pub:' ,missing_pub)
