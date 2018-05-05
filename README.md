# machine-learning
Data explore using python and Pandas

# High level design :
![alt text](https://github.com/EswaranMuthu/machine-learning/blob/master/dataExplore.png)


# Problem statement : Recommend product to the customer.

Existing solution : get input from orders table, find all placed orders use R / Python to slice and dice the data with dataframe and copy the out put to csv file. 

proposed solution : along with existing solution, get host site visitor recording and analyse the data and use them along with placed order to recomend the products to the user.

Description : 
1. Using (https://www.hotjar.com/) or custom java script track all host site visitor. all their user experience like user click, searched products, products added/deleted to cart, time spent on each product page etc.


2. all host site visiting user's browser will be an "IOT" and send data to public cloud (amazon S3)
3.  Python / R will receive the data from S3, with internal dataframe will remove the noise, analyse the data and generate output similar to "placed order" DB.


4. Input from placed order and from step 3 is analysed further to generate csv file will all product recommendations.
5. from csv generated from step 4, product recommendation application will display in a web.  


