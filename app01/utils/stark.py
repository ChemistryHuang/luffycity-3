# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/11/10 14:47 
# @Author : TrueNewBee
from stark.service.stark import site,ModelStark
from app01.models import *


site.register(CourseCategory)
site.register(CourseSubCategory)
site.register(DegreeCourse)
site.register(Teacher)
site.register(Scholarship)
site.register(Course)
site.register(CourseDetail)
site.register(OftenAskedQuestion)
site.register(CourseOutline)
site.register(CourseChapter)
site.register(CourseSection)
site.register(Homework)
site.register(PricePolicy)
site.register(ArticleSource)
site.register(Article)
site.register(Collection)
site.register(Comment)
site.register(Account)
site.register(UserAuthToken)
