#/usr/bin/python
#coding = utf-8
import sys, os, time, httplib,urllib


if sys.platform == 'linux' or sys.platform == 'linux2':
	clearing = 'clear'
else:
	clearing = 'cls'
os.system(clearing)


if len(sys.argv) != 2:
	print "\n|-------------------------------------------------|"
	print "| Help: webadmin.py -h                            |"
	print "| Visit https://lpericena.blogspot.com/           |"
        print "|-------------------------------------------------|"

	sys.exit(1)
	
for arg in sys.argv:
	if arg == '-h':
		print "\n|--------------------------------------------------|"
                print "|      Admin login           v1.0                  |"
	        print "| Example: webadmin.py site.com  >>page.txt                  |"
	        print "| Visit https://lpericena.blogspot.com/            |"
                print "|--------------------------------------------------|\n"
		sys.exit(1)
		
site = sys.argv[1].replace("http://","").rsplit("/",1)[0] 
site = site.lower()

admin_path = [
'admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
		'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
		'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
		'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
		'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
		'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
		'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
		'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
		'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
		'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
		'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
		'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
		'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
		'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
		'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
		'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
		'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
		'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
		'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','/adminpanel'





'robots.txt',
'ads.txt',
'ip.php',
'verify=True',
'ip.txt', 
'login.html',
'login.php',
'usernames.txt', 
'admin.php',
'admin/',
'administrator/',
'moderator/',
'webadmin/',
'adminarea/',
'bb-admin/',
'adminLogin/',
'admin_area/',

'admin/admin',
'wp-login',
'wp-admin/',
'root',
':8080/',
':80',
'admin/login/',
'pregrado/',
'panel-administracion/',
'instadmin/',
'memberadmin/',
'administratorlogin/','adm/',
'admin/account.php',
'admin/index.php','admin/login.php',
'admin/admin.php',
'admin/account.php','joomla/administrator',
'login.php',
'admin_area/admin.php',
'admin_area/login.php','siteadmin/login.php',
'siteadmin/index.php',
'siteadmin/login.html','admin/account.html',
'admin/index.html','admin/login.html',
'admin/admin.html','admin_area/index.php',
'bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php',
'admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admincp/index.asp','admincp/login.asp',
'admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html',
'admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php',
'nsw/admin/login.php','webadmin/login.php','admin/admin_login.php',
'admin_login.php','administrator/account.php','administrator.php',
'admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php',
'admin-login.php','bb-admin/index.html','bb-admin/login.html',
'bb-admin/admin.html','admin/home.html','modelsearch/login.php','moderator.php',
'moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html',
'admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html',
'home.html','rcjakar/admin/login.php','adminarea/index.html',
'adminarea/admin.html','webadmin.php','webadmin/index.php','webadmin/admin.php',
'admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php',
'moderator.html','administrator/index.html','administrator/login.html','user.html',
'administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html',
'panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html',
'user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php',
'wp-login.php','adminLogin.php','admin/adminLogin.php','home.php',
'adminarea/index.php','adminarea/admin.php','adminarea/login.php',
'panel-administracion/index.php','panel-administracion/admin.php',
'modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php',
'adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php',
'admin2/index.php','adm/index.php','adm.php','affiliate.php','adm_auth.php',
'memberadmin.php','administratorlogin.php'
,'pregrado/login/index.php','robots.txt','contrasenas.html','log.html',





]
print "\n|--------------------------------------------------|"
print "|      Admin login           v1.0                  |"
print "| Example: webadmin.py site.com                    |"
print "| Visit https://lpericena.blogspot.com/            |"
print "|--------------------------------------------------|"

print "[-] %s" % time.strftime("%X")
		
print "[+] Target:",site
print "[+] Checking paths..."
print
print "|Value|   Constant          |    url-Definition"
try:
  
	for admin in admin_path:
		admin = admin.replace("\n","")
		admin = "/" + admin
		connection = httplib.HTTPConnection(site)
		connection.request("GET",admin)
		response = connection.getresponse()
		
		print "[ %s ]   %s |  %s%s  " % (response.status,response.reason,site,admin)
			
		
except(KeyboardInterrupt,SystemExit):
		raise
except:
		pass	
		