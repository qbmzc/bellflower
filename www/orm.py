#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ ='congco'

import asyncio,logging
import aiomysql

def log(sql,args=()):
	logging.info("SQL:%s" % sql)

@asyncio.coroutine
async def create_pool(loop,**kw):
	logging.info("create datebase connection pool......")
	global __pool
	__pool = await aiomysql.create_pool(
		host=kw.get('host','localhost')
		port=kw.get('port',3306)
		user=kw.['user']
		password=kw['password']
		db=kw['db']
		charset=kw.get('charset','utf-8')
		autocommit=kw.get('autocommit',True)
		maxsize=kw.get('maxsize',10)
		minsize=kw.get('minsize',1)
		loop=loop
		)
	