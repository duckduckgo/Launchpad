# I am only testing this in python 2.6 and 2.7. it will probably not work in python 3.x

from urllib import urlopen 


try: lp = urlopen('https://launchpad.net/projects/+all').read() # download the page's HTML
except: exit() # if there are any errors, just give up

# this splits the whole thing into a list of the project divs
projects = '<div>'.join(lp.split("<div>")[1:]).split("""    </table>
    <table style="width: 100%;" class="lower-batch-nav">
  <tbody>
    <tr>
      <td style="white-space: nowrap" class="batch-navigation-index">""")[0] # it was kinda hard to find something unique to say where the end is, but this should do


first = True # the first one is slightly different
for proj in projects.split("""    </div>
  </div>
</div>""")[0:-1]: # this is always at the end of each project section
    lpp = proj.strip().split("\n")
    namesec = lpp[1]
    descsec = ' '.join(lpp[3:]).split("</div>")[0]
    authorsec = ' '.join(lpp[5:])
    
    if first: 
        namesec = lpp[0]
        descsec = ' '.join(lpp[2:]).split("</div>")[0]
        authorsec = lpp[4]
        
    
    url = 'https://launchpad.net' + namesec.split('<a href="')[1].split('"')[0]
    name = namesec.split(">")[1].split("<")[0]
    desc = descsec.split("<div>")[1]
    authorurl = 'https://launchpad.net' + authorsec.split('<a href="')[1].split('"')[0]
    author = authorsec.split(">")[1].split("<")[0]
    
    print name
    print url
    print desc
    print author
    print authorurl
    print '---'
    
    
    first = False


##### COLLECT THE MOST RECENT PROJECT #####
#print "\nThis is the most recently added project:"

# link
#print 'https://launchpad.net' + lp.split("<div>")[1].split('<a href="')[1].split('" class="sprite product">')[0]
# name
#print lp.split("<div>")[1].split(' class="sprite product">')[1].split("</a>")[0]
# Short description
#print lp.split("<div>")[2].split("</div>")[0]

#autharea = lp.split("<div>")[3].split()

# author's page
#print 'https://launchpad.net' + autharea[3].split('"')[1]
# author's name
#print ' '.join(autharea[5:7]).split(">")[1].split("<")[0]








