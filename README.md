## Infoga - Email Information Gathering

Infoga is a tool gathering email accounts informations (ip,hostname,country,...) from different public source (search engines, pgp key servers and shodan) and check if emails was leaked using hacked-emails API. Is a really simple tool, but very effective for the early stages of a penetration test or just to know the visibility of your company in the Internet.

![screen](https://raw.githubusercontent.com/m4ll0k/Infoga/master/screen.PNG)

## Installation
```
$ git clone https://github.com/m4ll0k/Infoga.git infoga
$ cd infoga
```
__Linux__
```
$ pip3 install requests
$ python3 infoga.py
```
__Windows__
```
$ python3 -m pip install requests 
$ python3 infoga.py
```

## Usage

```
$ python3 infoga.py --domain cia.gov --source google --verbose 3
```

```
________________________________________
 Infoga - Email Information Gathering
        Momo Outaadi (m4ll0k)
      https://github.com/m4ll0k
________________________________________

[*] Searching "cia.gov" in Google...
[i] Found 5 emails in Google
[+] Email: Info@cia.gov (198.81.129.68)
 |  Hostname: mail1.cia.gov
 |  Country: US (United States)
 |  City: Oakton (VA)
 |  ASN: AS7046
 |  ISP: ANS Communications
 |  Map: Map: https://www.google.com/maps/@38.89320000000001,-77.3341,10z (38.89320000000001,-77.3341)
 |  Organization: Central Intelligence Agency
 |  Ports: [25]

[+] Email: Info@cia.gov (198.81.129.148)
 |  Hostname: mail2.cia.gov
 |  Country: US (United States)
 |  City: Oakton (VA)
 |  ASN: AS7046
 |  ISP: ANS Communications
 |  Map: Map: https://www.google.com/maps/@38.89320000000001,-77.3341,10z (38.89320000000001,-77.3341)
 |  Organization: Central Intelligence Agency
 |  Ports: [25]

[+] Email: njbroderick@cia.gov (198.81.129.148)
 |  Hostname: mail2.cia.gov
 |  Country: US (United States)
 |  City: Oakton (VA)
 |  ASN: AS7046
 |  ISP: ANS Communications
 |  Map: Map: https://www.google.com/maps/@38.89320000000001,-77.3341,10z (38.89320000000001,-77.3341)
 |  Organization: Central Intelligence Agency
 |  Ports: [25]

```

```
$ python3 infoga.py --domain cia.gov --source google --breach --verbose 3
```

```
________________________________________
 Infoga - Email Information Gathering
        Momo Outaadi (m4ll0k)
      https://github.com/m4ll0k
________________________________________

[*] Searching "cia.gov" in Google...
[i] Found 5 emails in Google
[+] Email: Info@cia.gov (198.81.129.148)
 |  Hostname: mail2.cia.gov
 |  Country: US (United States)
 |  City: Oakton (VA)
 |  ASN: AS7046
 |  ISP: ANS Communications
 |  Map: Map: https://www.google.com/maps/@38.89320000000001,-77.3341,10z (38.89320000000001,-77.3341)
 |  Organization: Central Intelligence Agency
 |  Ports: [25]

[!] This email was leaked... found 16 results..
 |  Leaked in: CIA.GOV EMAILS
 |  Data Leaked: 2017-12-02T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/31109ea0447325b7c7e4/cia-gov-emails
 |  Source Network: clearnet

 |  Leaked in: CIA Emails
 |  Data Leaked: 2017-11-03T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/c3928b43c7c31c0e6307/cia-emails
 |  Source Network: clearnet

 |  Leaked in: emaildatalist.net
 |  Data Leaked: 2017-09-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/0600f5a565572edeceff/emaildatalist-net
 |  Source Network: darknet

 |  Leaked in: Feds GET DOXED
 |  Data Leaked: 2017-08-19T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/90f6246ac74367888aa4/feds-get-doxed
 |  Source Network: clearnet

 |  Leaked in: Untitled
 |  Data Leaked: 2017-08-19T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/c0dce19fdc615367cb82/untitled
 |  Source Network: clearnet

 |  Leaked in: #justiceforpaigedoherty (F.B.I &amp; C.I.A) LEAKED
 |  Data Leaked: 2017-02-27T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/5c362e1dc7e6d7dc40ab/justiceforpaigedoherty-f-b-i-amp-c-i-a-leaked
 |  Source Network: clearnet

 |  Leaked in: More Emails
 |  Data Leaked: 2017-02-16T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/94886ba1c051c603c5c6/more-emails
 |  Source Network: clearnet

 |  Leaked in: CIA Info MEGA File - Directory of Employees and Of
 |  Data Leaked: 2016-11-06T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/e559a561ae2d6ae0335d/cia-info-mega-file-directory-of-employees-and-of
 |  Source Network: clearnet

 |  Leaked in: Gambling Pack French data
 |  Data Leaked: 2016-10-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/e9f9fcbc3aa793f287e5/gambling-pack-french-data
 |  Source Network: darknet

 |  Leaked in: betsson.com
 |  Data Leaked: 2016-10-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/a4a8b82016d6221cf951/betsson-com
 |  Source Network: darknet

 |  Leaked in: 1234
 |  Data Leaked: 2015-10-20T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/256014514bce58d4b306/1234
 |  Source Network: clearnet

 |  Leaked in: Yum CIA Emails :L
 |  Data Leaked: 2015-10-18T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/ad7ef54392fd710e83f3/yum-cia-emails-l
 |  Source Network: clearnet

 |  Leaked in: THE TOP SECRET CIA PLAN TO DESTROY AMERICA
 |  Data Leaked: 2014-11-14T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/a6479554708494d787ab/the-top-secret-cia-plan-to-destroy-america
 |  Source Network: clearnet

 |  Leaked in: Leaks | CIA emails by Alfariizy39
 |  Data Leaked: 2014-05-04T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/4cd5e4250296634ba4ea/leaks-cia-emails-by-alfariizy39
 |  Source Network: clearnet

 |  Leaked in: Email hacked
 |  Data Leaked: 2013-07-22T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/f1f0da97a2da0bff475b/email-hacked
 |  Source Network: clearnet

 |  Leaked in: Fbi/Cia/justice.gov/mi5/ Emails Leaked.
 |  Data Leaked: 2013-06-08T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/62750db8a8bbc9323352/fbi-cia-justice-gov-mi5-emails-leaked
 |  Source Network: clearnet

[+] Email: Info@cia.gov (198.81.129.68)
 |  Hostname: mail1.cia.gov
 |  Country: US (United States)
 |  City: Oakton (VA)
 |  ASN: AS7046
 |  ISP: ANS Communications
 |  Map: Map: https://www.google.com/maps/@38.89320000000001,-77.3341,10z (38.89320000000001,-77.3341)
 |  Organization: Central Intelligence Agency
 |  Ports: [25]

[!] This email was leaked... found 16 results..
 |  Leaked in: CIA.GOV EMAILS
 |  Data Leaked: 2017-12-02T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/31109ea0447325b7c7e4/cia-gov-emails
 |  Source Network: clearnet

 |  Leaked in: CIA Emails
 |  Data Leaked: 2017-11-03T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/c3928b43c7c31c0e6307/cia-emails
 |  Source Network: clearnet

 |  Leaked in: emaildatalist.net
 |  Data Leaked: 2017-09-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/0600f5a565572edeceff/emaildatalist-net
 |  Source Network: darknet

 |  Leaked in: Feds GET DOXED
 |  Data Leaked: 2017-08-19T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/90f6246ac74367888aa4/feds-get-doxed
 |  Source Network: clearnet

 |  Leaked in: Untitled
 |  Data Leaked: 2017-08-19T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/c0dce19fdc615367cb82/untitled
 |  Source Network: clearnet

 |  Leaked in: #justiceforpaigedoherty (F.B.I &amp; C.I.A) LEAKED
 |  Data Leaked: 2017-02-27T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/5c362e1dc7e6d7dc40ab/justiceforpaigedoherty-f-b-i-amp-c-i-a-leaked
 |  Source Network: clearnet

```

```
$ python3 infoga.py --info matteo.rossi@gmail.com --verbose 3
```

```
________________________________________
 Infoga - Email Information Gathering
        Momo Outaadi (m4ll0k)
      https://github.com/m4ll0k
________________________________________

[+] Email: matteo.rossi@gmail.com (64.233.187.27)
 |  Hostname: tj-in-f27.1e100.net
 |  Country: US (United States)
 |  ASN: AS15169
 |  ISP: Google
 |  Map: Map: https://www.google.com/maps/@34.05439999999999,-118.244,10z (34.05439999999999,-118.244)
 |  Organization: Google
 |  Ports: [25]

```

```
$ python3 infoga.py --info matteo.rossi@gmail.com --breach --verbose 3
```

```
________________________________________
 Infoga - Email Information Gathering
        Momo Outaadi (m4ll0k)
      https://github.com/m4ll0k
________________________________________

[+] Email: matteo.rossi@gmail.com (64.233.187.26)
 |  Hostname: tj-in-f26.1e100.net
 |  Country: US (United States)
 |  City: Mountain View (CA)
 |  ASN: AS15169
 |  ISP: Google
 |  Map: Map: https://www.google.com/maps/@37.41919999999999,-122.0574,10z (37.41919999999999,-122.0574)
 |  Organization: Google
 |  Ports: [25]

[!] This email was leaked... found 6 results..
 |  Leaked in: emaildatalist.net
 |  Data Leaked: 2017-09-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/0600f5a565572edeceff/emaildatalist-net
 |  Source Network: darknet

 |  Leaked in: elance.com
 |  Data Leaked: 2017-03-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/fa468625387cae31ceab/elance-com
 |  Source Network: darknet

 |  Leaked in: modbsolutions.com
 |  Data Leaked: 2016-09-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/bb2b8fd5d8df4e76c359/modbsolutions-com
 |  Source Network: darknet

 |  Leaked in: Unknown Crawler Database
 |  Data Leaked: 2016-09-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/ebff7f33ba79739f4157/unknown-crawler-database
 |  Source Network: darknet

 |  Leaked in: Unknown Subscribers Database
 |  Data Leaked: 2016-07-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/25fee9233cf4ef0f75de/unknown-subscribers-database
 |  Source Network: darknet

 |  Leaked in: myspace.com
 |  Data Leaked: 2013-05-01T00:00:00+00:00
 |  Details: https://hacked-emails.com/leak/1d48d9be2f718eb6ab2e/myspace-com
 |  Source Network: clearnet

```
