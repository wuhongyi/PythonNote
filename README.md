<!-- README.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 五 4月 20 22:48:26 2018 (+0800)
;; Last-Updated: 一 8月 27 11:49:31 2018 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 4
;; URL: http://wuhongyi.cn -->

# 简介

本文为吴鸿毅（wuhongyi@qq.com） Python使用的总结。


http://wuhongyi.cn/PythonNote/

[Python Cookbook 3rd Edition Documentation](http://python3-cookbook.readthedocs.io/zh_CN/latest/)


[Python爬虫小白入门（一）](http://www.cnblogs.com/Albert-Lee/p/6226699.html)


> https://www.python.org/
> https://morvanzhou.github.io/   好博客



本文主要面向python3(毕竟2.7会慢慢退出历史舞台)

```bash
#查询安装模块
pip list
```

```
#已经安装模块如下
alembic                           0.9.9    
argh                              0.26.2   
backcall                          0.1.0    
backports-abc                     0.5      
beautifulsoup4                    4.6.0    
bleach                            2.1.3    
certifi                           2018.1.18
cffi                              1.9.1    
chardet                           3.0.4    
CommonMark                        0.5.4    
cryptography                      1.7.2    
cycler                            0.10.0   
decorator                         4.0.11   
docutils                          0.14     
entrypoints                       0.2.3    
html5lib                          1.0.1    
idna                              2.6      
ipykernel                         4.8.2    
ipython                           6.3.1    
ipython-genutils                  0.1.0    
ipywidgets                        7.2.1    
jedi                              0.12.0   
Jinja2                            2.10     
jsonschema                        2.6.0    
jupyter                           1.0.0    
jupyter-client                    5.2.3    
jupyter-console                   5.2.0    
jupyter-contrib-core              0.3.3    
jupyter-contrib-nbextensions      0.5.0    
jupyter-core                      4.4.0    
jupyter-highlight-selected-word   0.2.0    
jupyter-latex-envs                1.4.4    
jupyter-nbextensions-configurator 0.4.0    
jupyterhub                        0.8.1    
jupyterthemes                     0.19.1   
kiwisolver                        1.0.1    
lesscpy                           0.13.0   
livereload                        2.5.1    
lxml                              4.2.1    
Mako                              1.0.7    
Markdown                          2.6.11   
MarkupSafe                        1.0      
matplotlib                        2.2.2    
metakernel                        0.20.14  
mistune                           0.8.3    
nbconvert                         5.3.1    
nbformat                          4.4.0    
notebook                          5.4.1    
numpy                             1.9.3    
pamela                            0.3.0    
pandas                            0.19.2   
pandas-datareader                 0.6.0    
pandocfilters                     1.4.2    
parso                             0.2.0    
pathtools                         0.1.2    
pexpect                           4.5.0    
pickleshare                       0.7.4    
pip                               10.0.0   
ply                               3.9      
port-for                          0.3.1    
prompt-toolkit                    1.0.15   
ptyprocess                        0.5.2    
pyasn1                            0.1.9    
pycparser                         2.14     
Pygments                          2.2.0    
pyparsing                         2.2.0    
python-dateutil                   2.7.2    
python-editor                     1.0.3    
python-oauth2                     1.1.0    
pytz                              2018.4   
PyYAML                            3.12     
pyzmq                             17.0.0   
qtconsole                         4.3.1    
recommonmark                      0.4.0    
requests                          2.18.4   
requests-file                     1.4.3    
requests-ftp                      0.3.1    
rise                              5.2.0    
selenium                          3.11.0   
Send2Trash                        1.5.0    
setuptools                        19.2     
simplegeneric                     0.8.1    
six                               1.10.0   
sphinx-autobuild                  0.7.1    
SQLAlchemy                        1.2.6    
sudospawner                       0.5.1    
terminado                         0.8.1    
testpath                          0.3.1    
tornado                           5.0.2    
traitlets                         4.3.2    
typing                            3.6.4    
urllib3                           1.22     
watchdog                          0.8.3    
wcwidth                           0.1.7    
webencodings                      0.5.1    
wheel                             0.31.0   
widgetsnbextension                3.2.1    
wrapt                             1.10.11  
zmq                               0.0.0 
```



以前测试版本2.7.5,安装了以下模块

```
appdirs (1.4.3)
argh (0.26.2)
Babel (0.9.6)
backports-abc (0.5)
backports.shutil-get-terminal-size (1.0.0)
backports.ssl-match-hostname (3.4.0.2)
Beaker (1.5.4)
BeautifulSoup (3.2.1)
beautifulsoup4 (4.6.0)
blivet (0.61.15.59)
Brlapi (0.6.0)
certifi (2017.4.17)
cffi (1.6.0)
chardet (2.2.1)
CommonMark (0.5.4)
configobj (4.7.2)
configshell-fb (1.1.18)
coverage (3.6b3)
cryptography (1.3.1)
cupshelpers (1.0)
custodia (0.1.0)
decorator (3.4.0)
di (0.3)
dnspython (1.12.0)
docutils (0.11)
enum34 (1.0.4)
ethtool (0.8)
firstboot (19.5)
freeipa (2.0.0a0)
fros (1.0)
gssapi (1.2.0)
gyp (0.1)
idna (2.0)
iniparse (0.4)
initial-setup (0.3.9.36)
iotop (0.6)
ipaclient (4.4.0)
ipaddr (2.1.9)
ipaddress (1.0.16)
ipalib (4.4.0)
ipaplatform (4.4.0)
ipapython (4.4.0)
IPy (0.75)
ipython (3.2.1)
ipython-genutils (0.2.0)
javapackages (1.0.0)
Jinja2 (2.7.2)
jsonpointer (1.9)
jsonschema (2.5.1)
jupyter-client (5.0.1)
jupyter-core (4.3.0)
jwcrypto (0.2.1)
kdcproxy (0.3.2)
kerberos (1.1)
kitchen (1.1.1)
kmod (0.1)
langtable (0.0.31)
livereload (2.5.1)
lvm (2.02.166-2-RHEL7.-2016-11-16-)
lxml (3.2.1)
M2Crypto (0.21.1)
Magic-file-extensions (0.2)
Mako (0.8.1)
Markdown (2.6.8)
MarkupSafe (0.11)
matplotlib (1.2.0)
mistune (0.5.1)
MySQL-python (1.2.5)
netaddr (0.7.5)
netifaces (0.10.4)
nose (1.3.0)
ntplib (0.3.2)
numpy (1.7.1)
openlmi (0.5.0)
packaging (16.8)
pandas (0.20.1)
pandas-datareader (0.4.0)
Paste (1.7.5.1)
path.py (5.2)
pathtools (0.1.2)
pcp (1.0)
perf (0.1)
pexpect (2.3)
Pillow (2.0.0)
pip (9.0.1)
ply (3.4)
policycoreutils-default-encoding (0.1)
port-for (0.3.1)
psycopg2 (2.5.1)
ptyprocess (0.5.1)
pyasn1 (0.1.9)
pycparser (2.14)
pycups (1.9.63)
pycurl (7.19.0)
Pygments (1.4)
pygobject (3.14.0)
pygpgme (0.3)
pyinotify (0.9.4)
pykickstart (1.99.66.10)
pyliblzma (0.5.3)
pyOpenSSL (0.13.1)
pyparsing (1.5.6)
pyparted (3.9)
pysmbc (1.0.13)
python-augeas (0.5.0)
python-dateutil (2.6.0)
python-dmidecode (3.10.13)
python-ldap (2.4.15)
python-meh (0.25.2)
python-memcached (1.48)
python-nss (0.16.0)
python-yubico (1.2.3)
pytz (2012d)
pyudev (0.15)
pyusb (1.0.0b1)
pywbem (0.7.0)
pyxattr (0.5.1)
PyYAML (3.10)
pyzmq (14.3.1)
qrcode (5.0.1)
recommonmark (0.4.0)
repoze.lru (0.4)
requests (2.6.0)
requests-file (1.4.2)
requests-ftp (0.3.1)
rtslib-fb (2.1.57)
selenium (3.4.3)
seobject (0.1)
sepolicy (1.1)
setproctitle (1.1.6)
setroubleshoot (1.1)
setuptools (0.6rc11)
simplegeneric (0.8)
singledispatch (3.4.0.3)
six (1.9.0)
slip (0.4.0)
slip.dbus (0.4.0)
Sphinx (1.1.3)
sphinx-autobuild (0.6.0)
SSSDConfig (1.14.0)
targetcli-fb (2.1.fb41)
targetd (0.7)
Tempita (0.5.1)
terminado (0.6)
tornado (4.5)
traitlets (4.3.2)
urlgrabber (3.10)
urllib3 (1.10.2)
urwid (1.1.1)
virtualenv (1.10.1)
watchdog (0.8.3)
yum-axelget (1.0.4)
yum-langpacks (0.4.2)
yum-metadata-parser (1.1.4)
```

<!-- README.md ends here -->
