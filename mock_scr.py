import xarray as xr

#считывает из инициализационного файла FCAN и CMAS и возвращает dataset tsl_monthly

def mock_class (init_file):
    fcan = init_file.FCAN.values.flatten()[3]
    cmas = init_file.CMAS.values.flatten()[3]

    if fcan > 0.975:
        if cmas > 0.46:
            output = 'tsl_monthly_more.nc'
        else: raise Exception('Impossible parameters')
    elif fcan <= 0.975 and fcan > 0.90:
        if cmas <= 0.75 and cmas > 0.30:
            output = 'tsl_monthly_ND.nc'
        else: raise Exception('Impossible parameters')
    elif fcan <= 0.90 and fcan > 0.77:
        if cmas <= 0.53 and cmas > 0.27:
            output = 'tsl_monthly_LD.nc'
        else: raise Exception('Impossible parameters')
    elif fcan <= 0.77 and fcan > 0.62:
        if cmas <= 0.38 and cmas > 0.12:
            output = 'tsl_monthly_MD.nc'
        else: raise Exception('Impossible parameters')
    elif fcan <= 0.62 and fcan > 0.275:
        if cmas <= 0.30 and cmas > 0.0:
            output = 'tsl_monthly_HD.nc'
        else: raise Exception('Impossible parameters')

    else: output = 'tsl_monthly_bare.nc'

    return xr.open_dataset(output)