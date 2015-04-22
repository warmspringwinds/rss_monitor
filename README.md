# Rss feed monitor tool

The tool regularly checks the specified by you in `rss_feed_links.txt` rss links for new entries.
When it detects new entry, it stores it in a Elasticsearch database with domain information, keywords,
date etc.

## Installation

### Services you need to install

In order for this tool to work, you will need the following products installed on you machine and runnig:
1. [Elasticsearch](https://www.elastic.co/downloads/elasticsearch). (just install it using provided by them `.deb` file)
2. [Kibana visualization tool](https://www.elastic.co/downloads/kibana). (also can be installed on the website of Elasticsearch)
3. [Kopf plugin](https://github.com/lmenezes/elasticsearch-kopf) for Elasticsearch.
4. Create index in Elasticsearch with the name `rss` through kopf plugin after installation.

### Script installation

You will need:

1. Python `2.7.8` and `pip` installed.
2. Run `pip install -r requirements.txt`
3. Make sure elasticsearch is runnig and the index is set up.
4. Set up a cron job to make this script run each 1 hour. Run `corontab -e` and add the following line to
the end of the file `0 * * * * /path/to/you/script/folder/cron_job.sh > /dev/null`.
But before it, also change the `cron_job.sh` accordingly to your file locations.

## Usage

1. In order to see the result run `kibana` and go to the page where it runs.
2. Select `rss` index and create the visualizations that you need.
