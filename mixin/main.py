from log import LogFileMixin, LogPrintMixin

lf = LogFileMixin()
lf.log_success('Ola mundo')
lf.log_error('Ola mundo')

lp = LogPrintMixin()
lp.log_success('Ola mundo')
lp.log_error('Ola mundo')
