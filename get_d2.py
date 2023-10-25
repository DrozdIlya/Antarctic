#!/usr/bin/env python2.7
# months = ['01','02','03','04','05','06','07','08','09','10','11','12']
from ecmwfapi import ECMWFDataServer
import calendar
months = range(1,13,1) 
server = ECMWFDataServer()
for year in range(2010, 2022):
	print 'YEAR ',year
	for m in months:
		days =  calendar.monthrange(year,m)[1]
		bdate="%s%02d01"%(year,m)
		edate="%s%02d%s"%(year,m,days)
		print bdate, ' to ', edate
		server.retrieve({
			"class": "ea",
			"dataset": "era5",
			"stream": "oper",
			"type": "an",
			"levtype": "sfc",
			"grid": "0.3/0.3", 
			"param": "2d",
			"step": "0",
			"expver": "1",
			"date": "%s/to/%s"%(bdate,edate),
			"time": "00/to/23/by/1",
			"format": "netcdf",
			"target": "era5_d2_%s-%02d.nc"%(year,m)
		})
