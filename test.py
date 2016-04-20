#!/bin/env python 
# -*- coding: utf-8 -*-
import sys
from zoomeye.ZoomeyeApiSdk import ZoomeyeSDK

user = "your login name"
passwd = "your login passwd"
app = ZoomeyeSDK(user,passwd)

#���ø߼���������,webSearch����hostSearch�Ժ󣬱����
app.advancedSearchArgs.os = "FreeBSD"
app.advancedSearchArgs.apple= "balalalala"
#app.advancedSearchArgs.app = "apple"

#�ȵ�¼api
app.login()
#print app.access_token

#��ȡ�û���Ϣ
app.resourcesInfo()

#��������,����ȫ��Ϣ
result = app.hostSearch("cms",facets="os",page=1)

#��ȡ��������IP��ַ
print app.getIp_ZoomeyeSearch(result)

#����web������ȫ��Ϣ
result = app.webSearch("cms",facets="os",page=1)

#��ȡ��������IP��ַ
print app.getIp_ZoomeyeSearch(result)

#��ȡ����������
print app.total_ZoomeyeSearch(result)
