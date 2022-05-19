import pandas as pd
from googleAnalytics.Service import Service

class Query:
    def __init__(self) -> None:
        self.name = None
        self.metrics = None
        self.dimensions = None
        self.filters = None
        self.table = None
        self.ids = None

    def asRawDF(self):
        return self.results

    def asSQLDF(self):
        return self.results

    def get_results(self,service : Service, start_date, end_date):
        self.response = service.resource.data().ga().get(ids=self.ids,start_date=start_date, end_date=end_date,
            metrics=self.metrics, dimensions=self.dimensions, start_index='1', max_results='1000',filters=self.filters).execute()
        self.results = self.parse_query_response()
    
    def parse_query_response(self) -> pd.DataFrame:
        cols = []
        data = []
        for i in self.response['columnHeaders']:
            cols.append(i['name'][3:])

        for i in self.response['rows']:
            data.append(i)

        df = pd.DataFrame(data, columns=cols)
        df['Origen'] = self.response['profileInfo']['profileName']
        
        return df

class ConditionalQuery(Query):
    pass

class TraficoTotal(Query):
    def __init__(self,ids):
        self.name = "Trafico total"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = None
        self.table = ""
        self.ids = ids

class TraficoXCanal(Query):
    def __init__(self,ids):
        self.name = "Trafico aperturado por Canal"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth,ga:channelGrouping"
        self.filters = None
        self.table = "_xCanal"
        self.ids = ids

class TraficoXPais(Query):
    def __init__(self,ids):
        self.name = "Trafico aperturado por Pais"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth,ga:country"
        self.filters = None
        self.table = "_xPais"
        self.ids = ids

class TraficoXPaisDispositivo(Query):
    def __init__(self,ids):
        self.name = "Trafico aperturado por Pais y por dispositivo"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth,ga:country,ga:deviceCategory"
        self.filters = None
        self.table = "_xPais_xDispositivo"
        self.ids = ids

class TraficoXDispositivo(Query):
    def __init__(self,ids):
        self.name = "Trafico aperturado por dispositivo"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth,ga:deviceCategory"
        self.filters = None
        self.table = "_xDispositivo"
        self.ids = ids

class TraficoXFuente(Query):
    def __init__(self,ids):
        self.name = "Trafico aperturado por Red Social de llegada"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth,ga:socialNetwork"
        self.filters = None
        self.table = "_xFuente"
        self.ids = ids

class TraficoTotalXRRSS(Query):
    def __init__(self,ids):
        self.name = "Trafico total proveniente de redes sociales (FB,IG,TW,WPP)"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = "ga:source=@facebook,ga:source=@twitter,ga:source=@instagram,ga:source=@whatsapp"
        self.table = "_xSocialMedia"
        self.ids = ids

class TraficoPlayersRedCienRadios(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico total de los players de la red completa"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = "ga:pagePath=@/player/,ga:pagePath=@/hd/,ga:pagePath=@/MITREHD/,ga:pagePath=@/embed/live.php?streamname=MITREHD-10002&autoplay=true,ga:pagePath=@/embed/live.php?streamname=cienradioshd-10002&autoplay=true;ga:hostname=@radiomitre.cienradios.com,ga:hostname=@la100.cienradios.com,ga:hostname=@ar.cienradios.com,ga:hostname=@vmf.edge-apps.net"
        self.table = "_xPlayer"
        self.ids =  "ga:66731516"

class TraficoPlayersLa100(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico total de los players de La 100"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = "ga:pagePath=@/player/,ga:pagePath=@/hd/,ga:pagePath=@/embed/live.php?streamname=cienradioshd-10002&autoplay=true;ga:hostname=@la100.cienradios.com,ga:hostname=@vmf.edge-apps.net"
        self.table = "_xPlayer"
        self.ids = "ga:167591365"

class TraficoSinPlayerLa100(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico de la 100 sin el player"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = "ga:pagePath!@/player/;ga:pagePath!@/hd/"
        self.table = "_sinPlayer"
        self.ids = 'ga:167591365'

class TraficoPlayersMitre(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico total de los players de Mitre"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = "ga:pagePath=@/player/,ga:pagePath=@/hd/,ga:pagePath=@/MITREHD/;ga:hostname=@radiomitre.cienradios.com,ga:hostname=@vmf.edge-apps.net"
        self.table = "_xPlayer"
        self.ids = "ga:167562445"

class TraficoPlayersCienradios(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico total de los players de Cienradios"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = "ga:pagePath=@/player/;ga:hostname=@ar.cienradios.com"
        self.table = "_xPlayer"
        self.ids = "ga:167618622"

class TraficoPlayerLa100Alternativo(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico de los players alternativos de la 100 aperturado por player"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth,ga:hostname"
        self.filters = "ga:pagePath==/player/la100-2-rock-nacional/,ga:pagePath==/player/la100-3-top-40/,ga:pagePath==/player/la100-4-clasicos/,ga:pagePath==/player/la100-5-latino/,ga:pagePath==/player/la100-6-nuevos-clasicos/,ga:pagePath==/player/la100-7-reggaeton/"
        self.table = "_xPagina"
        self.ids = "ga:167591365"

class TraficoPlayersLa100XPlayer(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico de los players alternativos de la 100 aperturado por player"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth,ga:pagePath"
        self.filters = "ga:pagePath==/player/la100-2-rock-nacional/,ga:pagePath==/player/la100-3-top-40/,ga:pagePath==/player/la100-4-clasicos/,ga:pagePath==/player/la100-5-latino/,ga:pagePath==/player/la100-6-nuevos-clasicos/,ga:pagePath==/player/la100-7-reggaeton/,ga:pagePath==/player/la100/"
        self.table = "_xPagina"
        self.ids = "ga:167591365"

class TraficoTotalPlayersLa100(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico total de los players de la 100"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = "ga:pagePath==/player/la100-2-rock-nacional/,ga:pagePath==/player/la100-3-top-40/,ga:pagePath==/player/la100-4-clasicos/,ga:pagePath==/player/la100-5-latino/,ga:pagePath==/player/la100-6-nuevos-clasicos/,ga:pagePath==/player/la100-7-reggaeton/,ga:pagePath==/player/la100/"
        self.table = "_xPagina"
        self.ids = "ga:167591365"

class TraficoXHostnameADC(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico de los ADC aperturado por hostname"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth,ga:hostname"
        self.filters = "ga:hostname==marcelolongobardi.radiomitre.com.ar,ga:hostname==marcelolongobardi.cienradios.com,ga:hostname==marcelobonelli.cienradios.com,ga:hostname==jorgefernandezdiaz.cienradios.com,ga:hostname==cristinaperez.cienradios.com,ga:hostname==pablorossi.cienradios.com,ga:hostname==marcelatauro.cienradios.com,ga:hostname==lauradimarco.cienradios.com,ga:hostname==peladolopez.cienradios.com,ga:hostname==guillermocoppola.cienradios.com,ga:hostname==www.tatoyoung.com.ar"
        self.table = "_xHostname"
        self.ids = "ga:66731516"

class TraficoTotalHostnameADC(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico total de los ADC"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = "ga:hostname==marcelolongobardi.radiomitre.com.ar,ga:hostname==marcelolongobardi.cienradios.com,ga:hostname==marcelobonelli.cienradios.com,ga:hostname==jorgefernandezdiaz.cienradios.com,ga:hostname==cristinaperez.cienradios.com,ga:hostname==pablorossi.cienradios.com,ga:hostname==marcelatauro.cienradios.com,ga:hostname==lauradimarco.cienradios.com,ga:hostname==peladolopez.cienradios.com,ga:hostname==guillermocoppola.cienradios.com,ga:hostname==www.tatoyoung.com.ar"
        self.table = "_xHostname"
        self.ids = "ga:66731516"

class TraficoXHostnameVertical(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico de los Verticales aperturado por hostname"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth,ga:hostname"
        self.filters = "ga:hostname==fashionclick.cienradios.com,ga:hostname==libros.cienradios.com,ga:hostname==miafm.cienradios.com,ga:hostname==mitreyelcampo.cienradios.com,ga:hostname==planetavivo.cienradios.com,ga:hostname==mundoclasico.cienradios.com,ga:hostname==motortrend.cienradios.com"
        self.table = "_xHostname"
        self.ids = "ga:66731516"

class TraficoTotalHostnameVertical(ConditionalQuery):
    def __init__(self):
        self.name = "Trafico de los Verticales"
        self.metrics = "ga:users,ga:sessions,ga:pageviews,ga:bounceRate,ga:avgSessionDuration"
        self.dimensions = "ga:yearMonth"
        self.filters = "ga:hostname==fashionclick.cienradios.com,ga:hostname==libros.cienradios.com,ga:hostname==miafm.cienradios.com,ga:hostname==mitreyelcampo.cienradios.com,ga:hostname==planetavivo.cienradios.com,ga:hostname==mundoclasico.cienradios.com,ga:hostname==motortrend.cienradios.com"
        self.table = "_xHostname"
        self.ids = "ga:66731516"