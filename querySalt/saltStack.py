import requests

class SaltStack(object):
    cookies = None
    target = None
    def __init__(self, host, username, password, port='8000', secure=True, eproto='auto'):
        proto = 'https' if secure else 'http'
        self.target = '%s://%s:%s' % (proto, host, port)

        r = requests.post('%s/login' % self.target, data={'username': username,
                                                               'password': password,
                                                               'eauth': eproto})
        if r.status_code == 200:
            self.cookies = r.cookies
        else:
            raise Exception('Error from source %s' % r.text)


    def get_ip_addr(self, tgt, expr_form='compound', client='local'):
        r = requests.post(self.target, data={'fun': 'network.interface_ip',
                                             'tgt': tgt,
                                             'client': client,
                                             'expr_form': expr_form,
                                             'arg': 'eth0'}, cookies=self.cookies)
        if r.status_code == 200:
            return r.json()['return']
        else:
            raise Exception('Error from source %s' % r.text)

    def restart_service(self, service, tgt, expr_form='compound', client='local'):
        r = requests.post(self.target, data={'fun': 'service.restart',
                                             'tgt': tgt,
                                             'client': client,
                                             'expr_form': expr_form,
                                             'arg': service}, cookies=self.cookies)
        if r.status_code == 200:
            return r.json()['return']
        else:
            raise Exception('Error from source %s' % r.text)

    def get_roles(self, tgt, expr_form='compound', client='local'):
        r = requests.post(self.target, data={'fun': 'grains.item',
                                             'tgt': tgt,
                                             'client': client,
                                             'expr_form': expr_form,
                                             'arg': 'roles'}, cookies=self.cookies)
        if r.status_code == 200:
            return r.json()['return']
        else:
            raise Exception('Error from source %s' % r.text)

