import urllib2, urlparse
from bs4 import BeautifulSoup


url = "http://stuy.enschool.org/apps/pages/index.jsp?type=d&uREC_ID=%s&pREC_ID=%s"

depts = [
    {'uREC_ID': '126957', 'pREC_ID': '254108'}, 
    {'uREC_ID': '126653', 'pREC_ID': '252233'}, 
    {'uREC_ID': '126654', 'pREC_ID': '253403'}, 
    {'uREC_ID': '126657', 'pREC_ID': '253626'}, 
    {'uREC_ID': '126661', 'pREC_ID': '253617'}, 
    {'uREC_ID': '126659', 'pREC_ID': '253269'}, 
    {'uREC_ID': '126961', 'pREC_ID': '253554'}, 
    {'uREC_ID': '126662', 'pREC_ID': '253947'}, 
    {'uREC_ID': '126663', 'pREC_ID': '254002'},
    {'uREC_ID': '126658', 'pREC_ID': '253719'}
]


def get_description(path):
    """
    Super sus way to grab the first paragraph of the course description from the page

    Params: path - string representing url 
    Returns: a string of the description
    """
    try:
        request = urllib2.urlopen(path)
        html = request.read()
        soup = BeautifulSoup(html, 'html.parser')

    except:
        print "Couldn't open: %s" % path
        
    content = soup.find_all(id = "pageContentWrapper")[0]
    for string in content.stripped_strings:
        if len(string) > 70:
            return unicode(string).encode('utf-8')

    return "No description provided."
  

def lookup_courses_in_dep(path):
    """
    Find course info of all courses on page and add to database
    Params: path - string representing url 
    """

    request = urllib2.urlopen(path)
    html = request.read()
    soup = BeautifulSoup(html, 'html.parser')

    """
    for course in soup.find_all(td_with_a):
        try: 
            name = " ".join([unicode(s)for s in course.a.stripped_strings]).encode('utf-8')
        
            tds = course.parent.find_all("td")
            code = " ".join([unicode(s) for s in tds[1].stripped_strings]).encode('utf-8')
            if (len(tds) > 3):
                misc = " ".join([unicode(s) for s in tds[3].stripped_strings]).encode('utf-8')
            else:
                misc = "None"

            #resolve relative path into absolute
            url = urlparse.urljoin(path, course.a['href'])
            descript = get_description(url)

            print name + " " + code
            print misc
            print descript
            print "\n\n"

        except:
            print "something went wrong"
    """
    table = soup.find_all("table")

            
def td_with_a(tag):
    """
    Custom function for filtering with BeautifulSoup. 
    Pass as parameter to find_all

    Returns: True - the tag is a td with a as immediate child
             False - otherwise
    """
    return tag.name == 'td' and tag.contents and tag.contents[0].name == 'a'


if __name__ == "__main__":

    """
    path = url % ('126957', '254108')
    lookup_courses_in_dep(path)

    path = url % ('126967', '359851')
    get_description(path)
    """

    for dept in depts:
        path = url % (dept['uREC_ID'], dept['pREC_ID'])
        if dept['pREC_ID']:
            try:
                lookup_courses_in_dep(path)
            except:
                print "this entire page is screwed"
