import hashlib
import feedparser
import datetime
from time import mktime
import re

from lib import get_common_keyword, is_element_with_hash_exists, extract_rss_links_from_file

from elasticsearch import Elasticsearch
from goose import Goose


es_hadler = Elasticsearch()

goose_handler = Goose()

rss_links = extract_rss_links_from_file('rss_feed_links.txt')

for rss in rss_links:
    
    rss = feedparser.parse(rss)
    
    for index, item in enumerate(rss.entries):
        
        entry_link_hash = hashlib.md5(item.link).hexdigest()
        
        is_duplicate = is_element_with_hash_exists(entry_link_hash, 'rss', es_hadler)
        
        if not is_duplicate:
            doc_to_add = dict(item)
            doc_to_add['link_hash'] = entry_link_hash
            doc_to_add['published_parsed'] = datetime.datetime.fromtimestamp(mktime(doc_to_add['published_parsed']))
            
            try:
                
                extracted_page = goose_handler.extract(url=item.link)
                meta_description = extracted_page.meta_description
                domain = extracted_page.domain
                keyphrase = get_common_keyword(doc_to_add['title'], meta_description)
                doc_to_add['keyphrase'] = keyphrase
                doc_to_add['domain'] = domain
                
            except Exception, e:
                print "Error while fetching page. Error: "
                print e.__doc__
                print e.message
            
            
            es_hadler.index(index="rss",
                            doc_type="rss_doc",
                            body=doc_to_add,
                            timeout=30)

