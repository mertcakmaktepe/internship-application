SELECT Device_Type, REPLACE(REPLACE(REPLACE(REPLACE(Stats_Access_Link,'<url>',''),'</url>',''),'https://',''),'http://','') 
FROM xml_data
WHERE Device_Type = 'AXO145'