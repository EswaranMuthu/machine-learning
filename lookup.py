import csv
import pandas as pd



pub_path = 'c:\\Users\\Joe.Bell\Desktop\\BD_publications.csv'
input_path = 'c:\\Users\\Joe.Bell\Desktop\\BD_1.csv'
with open('c:\\Users\\Joe.Bell\Desktop\\pubskus.csv', "w+", newline='') as pubfile:
    pubs = pd.read_csv(pub_path)
    #removes dashes before join on pubs
    pubs['sku']=pubs['sku'].astype(str)
    #pubs['sku'] = pubs['sku'].replace(['-'],[''])
    skus = pd.read_csv(input_path)
    skus['sku']=skus['sku'].replace(['-'],[''])
    #print(skus)
    new = pubs.merge(skus, on='sku', how='left')
    #print(new)
    #sets the order of the columns
    new = new[['SITE_PRODUCT','GLOBAL_PRODUCT','sku','title','pubMedURL']]
    new.to_csv(pubfile, index=False)
