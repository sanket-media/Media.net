driverPath = r'D:\chromedriver.exe'
logFile = r'D:\GitHub\Media.net\leadGen\runtimeLogs.txt'

stage_my_sql = {
    'database': 'leadgen-new',
    'host': 'staging-mysql-private.cap-cloud.co',
    'port': 3306,
    'user': 'read_write_devs',
    'password': '4TU^R&I$FEWE%HGFEAG',
}

live_my_sql = {
    'database': 'live-leadgen',
    'host': 'cap-leadgen-mysql-readonly.cap-cloud.co',
    'port': 25060,
    'user': 'sanket.o_ro',
    'password': 'fW32$3#$R42ERWf34r23',
}

live_redshift = {
    'database': 'imedia',
    'host': 'web-apps.cepyv1ofeibj.us-west-2.redshift.amazonaws.com',
    'port': 5439,
    'user': 'sanketoswal_ro',
    'password': 'VWA#%b46v$n8u&%EA$v5&TM(<8n76rXQ',
}

fspu_qav1 = {
    'site': 'https://qa-v1.freesamplesprousa.com/?cid=qa-slug1&test=1',
    'env': 'qa-v1',
    'domain': 'freesamplesprousa',
    'cid': 'qa-slug1',
    'db': ('stage_my_sql',)
}

fspu_qav2 = {
    'site': 'https://qa-v2.freesamplesprousa.com/?cid=qa-slug2&test=1',
    'env': 'qa-v2',
    'domain': 'freesamplesprousa',
    'cid': 'qa-slug2',
    'db': ('stage_my_sql',)
}

fspu_live_full_tcpa = {
    'site': 'https://freesamplesprousa.com/?cid=vn1ws&test=1',
    'env': '',
    'domain': 'freesamplesprousa',
    'cid': 'vn1ws',
    'db': ('live_my_sql', 'live_redshift')
}
