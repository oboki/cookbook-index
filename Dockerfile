FROM elasticsearch:7.13.4

COPY archives/userdict_ko.txt /usr/share/elasticsearch/config/

RUN cd /usr/share/elasticsearch \
 && bin/elasticsearch-plugin install analysis-nori
