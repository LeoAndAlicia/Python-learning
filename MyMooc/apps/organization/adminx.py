# -*- coding:utf-8 -*-
__author__ = 'Leonardo'
__date__ = '2019/3/26 21:02'
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'tag', 'category', 'address', 'city', 'students',
                    'course_nums', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums' 'tag', 'category', 'address', 'city', 'students',
                     'course_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'tag', 'category', 'address', 'city__name', 'students',
                   'course_nums', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'age', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                     'age']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                   'fav_nums', 'age', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
