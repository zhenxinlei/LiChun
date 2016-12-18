import quandl

apiKey= 'xv2Z88x2Pe9HCL7kcieF'
apiVersion = '2015-04-09'

def intiQuandlApi():
    quandl.ApiConfig.api_key = apiKey
    quandl.ApiConfig.api_version = apiVersion