heads = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Cookie': '',
    'Host': '',
    '': '',
    '': ''
}
exit() if not r.status_code == requests.code.ok else print("request success")
cookies = '_xsrf=7tnCyUdtWnwWNC8sQ6usg3JSqx7a0zWv; _zap=eeaf0a8e-7c11-481c-91eb-0a1e0a968704; d_c0="AGDhXNgZ-g-PTjc30GXv_ziA_PDz-9lb2yM=|1567262028"; capsion_ticket="2|1:0|10:1567262031|14:capsion_ticket|44:YTQ1ZDkzNTFkYzU3NDZjNTkyYjM0NzM2ZjViOTYwNmI=|8a9db8a39cea4d4588b20bb102045ac58183f81b35953050a6d545c7d2a7bbac"; z_c0="2|1:0|10:1567262039|4:z_c0|92:Mi4xaEg2ZEN3QUFBQUFBWU9GYzJCbjZEeVlBQUFCZ0FsVk5WOU5YWGdCM3otOV9XbFY3QmV4Q1BWRm9MRkZueHZtU09B|8f85ae94f563db6445deaf0630a3e5be4ed00b1d839c0e26a956561ca171c712"; tst=r; q_c1=600de0a083b04463864b5170902685cf|1567747965000|1567747965000; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569563758,1569566010; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569566241'
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get(url, cookies=jar, headers=heads)
