import re


def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


def is_element_with_hash_exists(hash_to_check, index, es_handler):
    
    query = \
    {
        "query": {
            "filtered": {
                "query": {
                    "match_all": {}
                },
                "filter": {
                    "term": {
                        "link_hash": hash_to_check
                    }
                }
            }
        }
    }
    
    res = es_handler.search(index=index, body=query)
    return res['hits']['total'] != 0


def get_common_keyword(title, description):
    
    title_array = re.sub(r'[.!,-]', ' ', title.lower()).split()
    description_array = re.sub(r'[.!,-]', ' ', description.lower()).split()
    
    common_sequence = longest_common_substring(title_array, description_array)
    
    return " ".join(common_sequence)

def extract_rss_links_from_file(file_name):
    
    links = []
    
    file_handler = open(file_name)
    
    for line in file_handler:
        
        line = line.strip()
        
        if line:
            links.append(line)
    
    return links
    
    