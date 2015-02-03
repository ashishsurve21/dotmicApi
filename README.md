# dotmicApi

dotmicApi :-

A python wrapper for the dotmic api (A prodcut search engine to search for products from various sites such as flipkart, amazon, ebay and 
many more.)

Pre-requisites : 

1) An api key for the dotmic Api. ( http://www.dotmic.com/api/ )

2) Json module for python

3) urllib3 module for python


Example :- To use DotmicApi

import dotmic

prd = dotmic.Dotmic(Api_key)

result = prd.search(product_name)
