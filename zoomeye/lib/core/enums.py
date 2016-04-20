#!/bin/env python
# -*- coding: utf-8 -*-

"""
Author:liangrt
Date:2016-03-10
"""

import os
import sys

class SYS:
	_ = os.path.abspath(os.path.dirname(__file__))
	ROOT_PATH = _.split('zoomeye')[0]
	ROOT_PATH = os.path.join(ROOT_PATH,"zoomeye")

	CONF_PATH = os.path.join(ROOT_PATH, "conf")
	LOG_PATH = os.path.join(ROOT_PATH, "log")
	SRC_PATH = os.path.join(ROOT_PATH, "src")
	APP_PATH = os.path.join(SRC_PATH, "app")

	CONF_FILE = os.path.join(CONF_PATH, "sysconfig.conf")
	LOG_FILE = os.path.join(LOG_PATH, "system.log")

class ZOOMEYEURL:
	LOGINURL = "http://api.zoomeye.org/user/login"
	RESOURCESINFOURL = "http://api.zoomeye.org/resources-info"
	HOSTSEARCHURL = "http://api.zoomeye.org/host/search"
	WEBSEARCHURL = "http://api.zoomeye.org/web/search"

class ZOOMEYE_ECODE:
	OK = {
		200:	"request succeeded",
		201:	"resource created succeeded. for example user account has been registered successfully"
	}

	"""no use"""
	CLIENT_ERROR = {
		400:	"request invalid, validate usage and try again",
		401:	"request not authenticated, API token is missing, invalid or expired",
		402:	"credits of the account was insufficient",
		403:	"request not authorized, provided credential could not access to specified resource",
		404:	"request failed, the specified resource does not exist",

		422:	"request failed, validate parameters try again",	
		405:	"There is no official explanation!!",
	}
	
	SERVER_ERROR = {
		500:	"error occurred, we are notified",
		503:	"the request source was not available",
	}
	
class ZOOMEYE_FACETS:
	HOST = set([
		"app",
		"device",
		"service",
		"os",
		"port",
		"country",
		"city",
	])
	WEB = set([
		"webapp",
		"component",
		"framework",
		"frontend",
		"server",
		"waf",
		"os",
		"country",
		"city",
	])

class ZOOMEYE_ADVANCED_ARGS:
	ARGS = {
		"app":"���������",
		"ver":"�汾����",
		"os":"����ϵͳΪ",
		"country":"����Ϊ",
		"city":"����Ϊ",
		"device":"�豸����Ϊ",
		"port":"�˿ں�Ϊ",
		"hostname":"����������",
		"services":"��������Ϊ",
		"ip":"IP ��ַΪ",
		"cidr":"IP �� CIDR ����",
		"site":"��������",
		"desc":"�ؼ��ʰ���",
		"keywords":"��������",
	}
