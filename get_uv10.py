import cdsapi
import calendar
import os

time = ['%02d:00' % d for d in range(0, 24, 1)]

for iyear in range(2022, 2024):  # loop through years
    for imon in range(1, 13):    # loop through months

        year  = '%04d' % iyear
        month = '%02d' % imon

        print('################ ', year, '-', month, ' ##################')

        lastday1 = calendar.monthrange(iyear, imon)
        lastday = lastday1[1]+1

        days = ['%02d' % d for d in range(1, lastday, 1)]
        print(days)

        filename = 'ERA5_uv10m_%s-%02d.nc' % (year, imon)

        if os.path.isfile('./'+filename):
            print('this file is already downloaded: '+filename)
            continue

        successfully_downloaded = False
        tries = 0

        c = cdsapi.Client()
        while not successfully_downloaded:
            tries += 1
            try:
                c.retrieve(
                    'reanalysis-era5-single-levels', # reanalysis-era5.1-complete, reanalysis-era5-single-levels, reanalysis-era5-complete-preliminary-back-extension
                    {
                        'product_type': 'reanalysis',
                        'variable': ['10m_u_component_of_wind', '10m_v_component_of_wind'],
                        'year': year,
                        'month': month,
                        'day': days,
                        'time': time,
                        'format': 'netcdf'
                    },
                    filename)
                successfully_downloaded = True
            except Exception as ex:
                print('failed to dowload %s %d times' % (filename, tries))
                if tries == 50:
                    print('tries number exceeded 50!')
                    break
                else:
                    continue

# 2021-04-21 06:39:17,974 INFO Request is failed
# 2021-04-21 06:39:17,974 ERROR Message: the request you have submitted is not valid
# 2021-04-21 06:39:17,974 ERROR Reason:  Ambiguous parameter: day could be DATE or DATABASE - undefined value : reanalysis for parameter PRODUCT - Values are : - undefined value : 10m_u_component_of_wind for parameter VERIFY - Values are : - undefined value : 10m_v_component_of_wind for parameter VERIFY - Values are : - No request
# 2021-04-21 06:39:17,975 ERROR   Traceback (most recent call last):
# 2021-04-21 06:39:17,975 ERROR     File "/opt/cdstoolbox/cdscompute/cdscompute/cdshandlers/services/handler.py", line 55, in handle_request
# 2021-04-21 06:39:17,975 ERROR       result = cached(context.method, proc, context, context.args, context.kwargs)
# 2021-04-21 06:39:17,975 ERROR     File "/opt/cdstoolbox/cdscompute/cdscompute/caching.py", line 108, in cached
# 2021-04-21 06:39:17,975 ERROR       result = proc(context, *context.args, **context.kwargs)
# 2021-04-21 06:39:17,975 ERROR     File "/opt/cdstoolbox/cdscompute/cdscompute/services.py", line 118, in __call__
# 2021-04-21 06:39:17,975 ERROR       return p(*args, **kwargs)
# 2021-04-21 06:39:17,976 ERROR     File "/opt/cdstoolbox/cdscompute/cdscompute/services.py", line 59, in __call__
# 2021-04-21 06:39:17,976 ERROR       return self.proc(context, *args, **kwargs)
# 2021-04-21 06:39:17,976 ERROR     File "/home/cds/cdsservices/services/mars.py", line 352, in external
# 2021-04-21 06:39:17,976 ERROR       return mars(context, request, **kwargs)
# 2021-04-21 06:39:17,976 ERROR     File "/home/cds/cdsservices/services/mars.py", line 48, in mars
# 2021-04-21 06:39:17,976 ERROR       execute_mars(context, requests)
# 2021-04-21 06:39:17,976 ERROR     File "/home/cds/cdsservices/services/mars.py", line 192, in execute_mars
# 2021-04-21 06:39:17,977 ERROR       context.run_command("/usr/local/bin/mars", tmp, exception=MarsException)
# 2021-04-21 06:39:17,977 ERROR     File "/opt/cdstoolbox/cdscompute/cdscompute/context.py", line 207, in run_command
# 2021-04-21 06:39:17,977 ERROR       raise exception(call, proc.returncode, output)
# 2021-04-21 06:39:17,977 ERROR   home.cds.cdsservices.services.mars.py.MarsException: Ambiguous parameter: day could be DATE or DATABASE - undefined value : reanalysis for parameter PRODUCT - Values are : - undefined value : 10m_u_component_of_wind for parameter VERIFY - Values are : - undefined value : 10m_v_component_of_wind for parameter VERIFY - Values are : - No request
# failed to dowload ERA5_uv10m_2000-01.nc 1 times
