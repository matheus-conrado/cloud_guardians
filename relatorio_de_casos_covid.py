#!/usr/bin/env python
# coding: utf-8
from ETL.help_function.connect_rds_mysql import connect_mysql
import pandas as pd
db = connect_mysql()
query_1 = """ with 
	major as (select 
			 cc.country_name
			,max(cc.confirmed) as confirmed
		from 
			Cases_covid cc
		group by
			country_name
		order by 
			confirmed desc
		limit 1)
select * from Cases_covid cc2 inner join major mj on mj.country_name = cc2.country_name limit 500"""

query_2 = """with 
	major as (select 
			 cc.country_name
			,max(cc.deaths) as  deaths
		from 
			Cases_covid cc
		group by
			country_name
		order by 
			deaths desc
		limit 1)
select * from Cases_covid cc2 inner join major mj on mj.country_name = cc2.country_name limit 500"""

query_3 = """select max(deaths) as deaths
	  ,country_name
from Cases_covid cc 
group by 
	country_name
order BY 
	deaths DESC
limit 10 """

query_4 = """select max(confirmed) as  confirmed
	  ,country_name
from Cases_covid cc 
group by 
	country_name
order BY 
	confirmed DESC
limit 10"""

df1 = pd.read_sql(query_1,db)
df2 = pd.read_sql(query_2,db)
df3 = pd.read_sql(query_3,db)
df4 = pd.read_sql(query_4,db)

print(df1)
print("+-----------------------------------------------------------+")
print(df2)
print("+-----------------------------------------------------------+")
print(df3)
print("+-----------------------------------------------------------+")
print(df4)

