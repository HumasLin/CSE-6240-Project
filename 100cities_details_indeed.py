import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

urls = ['url', 'title', 'location', 'salary']

locations=['New+York%2C+NY','Los+Angeles%2C+CA','Chicago%2C+IL','Houston%2C+TX','Phoenix%2C+AZ','Philadelphia%2C+PA','San+Antonio%2C+TX','San+Diego%2C+CA','Dallas%2C+TX','San+Jose%2C+CA','Austin%2C+TX','Jacksonville%2C+FL','San+Francisco%2C+CA','Columbus%2C+OH','Indianapolis%2C+IN','Fort+Worth%2C+TX','Charlotte%2C+NC','Seattle%2C+WA','Denver%2C+CO','El+Paso%2C+TX','Boston%2C+MA','Detroit%2C+MI','Nashville%2C+TN','Memphis%2C+TN','Portland%2C+OR','Oklahoma+City%2C+OK','Las+Vegas%2C+NV','Louisville%2C+KY','Baltimore%2C+MD','Milwaukee%2C+WI','Albuquerque%2C+NM','Tucson%2C+AZ','Fresno%2C+CA','Sacramento%2C+CA','Mesa%2C+AZ','Kansas+City%2C+MO','Atlanta%2C+GA','Long+Beach%2C+CA','Omaha%2C+NE','Colorado+Springs%2C+CO','Raleigh%2C+NC','Miami%2C+FL','Virginia+Beach%2C+VA','Oakland%2C+CA','Minneapolis%2C+MN','Tulsa%2C+OK','Arlington%2C+TX','New+Orleans%2C+LA','Wichita%2C+KS','Cleveland%2C+OH','Tampa%2C+FL','Bakersfield%2C+CA','Aurora%2C+CO','Urban+Honolulu%2C+HI','Anaheim%2C+CA','Santa+Ana%2C+CA','Corpus+Christi%2C+TX','Riverside%2C+CA','Lexington%2C+KY','St.+Louis%2C+MO','Stockton%2C+CA','Pittsburgh%2C+PA','St.+Paul%2C+MN','Cincinnati%2C+OH','Anchorage%2C+AK','Henderson%2C+NV','Greensboro%2C+NC','Plano%2C+TX','Lincoln%2C+NE','Newark%2C+NJ','Toledo%2C+OH','Orlando%2C+FL','Chula+Vista%2C+CA','Irvine%2C+CA','Durham%2C+NC','Fort+Wayne%2C+IN','Jersey+City%2C+NJ','St.+Petersburg%2C+FL','Laredo%2C+TX','Buffalo%2C+NY','Madison%2C+WI','Lubbock%2C+TX','Chandler%2C+AZ','Scottsdale%2C+AZ','Norfolk%2C+VA','Glendale%2C+AZ','Reno%2C+NV','Winston-Salem%2C+NC','Irving%2C+TX','Garland%2C+TX','Chesapeake%2C+VA','Gilbert%2C+AZ','Hialeah%2C+FL','North+Las+Vegas%2C+NV','Paradise%2C+NV','Fremont%2C+CA','Arlington%2C+VA','Baton+Rouge%2C+LA','Boise+City%2C+ID','Richmond%2C+VA']

for i in locations:
    oriT = time.time()
    real_url = []
    sample_url = pd.DataFrame(columns = urls)

    for s in range(20000,100000,10000):
        start = 0
        print(len(real_url))
        for start in range(0,990,10):
            address = ('https://www.indeed.com/jobs?q=${}&l={}' + '&start=' + str(start)).format(s,i)
            print(address)
            page = requests.get(address)
            
            time.sleep(1)  #ensuring at least 1 second between page grabs
            soup = BeautifulSoup(page.text, "html.parser", from_encoding='utf-8')
            #print(soup)
            for div in soup.find_all(name='div', attrs={'class':'row'}): 
            #specifying row num for index of job posting in dataframe
                num_u = (len(sample_url) + 1) 
            #creating an empty list to hold the data for each posting
                url_list = []    
            #grabbing jk to get url
                try:
                    jk1 = div['data-jk']
                    start += 1

                except:
                    jk1 = 'not jk found'
                    continue

                url_now = "https://www.indeed.com/viewjob?jk=" + jk1

                if url_now in real_url:
                    continue
                else:                
                    url_list.append(url_now)
                
                for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
                    url_list.append(a['title'])

                c = div.findAll('div', attrs={'class': 'recJobLoc'}) 
                for span in c: 
                    url_list.append(span['data-rc-loc'])

                try:
                    url_list.append(div.find('nobr').text) 
                except:
                    try:
                        div_two = div.find(name='span', attrs={'class':'salaryText'})  
                        url_list.append(div_two.text.strip())
                    except:
                        url_list.append('Nothing_found')
            #appending list of job post info to dataframe at index num
                # print(url_list)
                real_url.append("https://www.indeed.com/viewjob?jk=" + jk1)
                sample_url.loc[num_u] = url_list

    # print(real_url)
    sample_url.to_csv(("{}_url.csv").format(i))

    columns = ['url', 'title', 'company_name', 'description']
    sample_df = pd.DataFrame(columns = columns)

    for num in range(len(real_url)):
        visit = real_url[num]
        print(visit)
        page = requests.get(visit)
        time.sleep(1)  #ensuring at least 1 second between page grabs
        soup = BeautifulSoup(page.text, "html.parser", from_encoding='utf-8')

        #specifying row num for index of job posting in dataframe
        num_s = (len(sample_df) + 1)
        #creating an empty list to hold the data for each posting
        job_details = []

        job_details.append(visit)
        #grab the title of the job
        title = soup.findAll('h3',{'class': 'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'})
        if len(title) < 1:
            real_url.append(visit)
            continue
        else:
            job_details.append(title[0].text.strip())

        #grab the company of the job
        company = soup.findAll('div',{'class': 'icl-u-lg-mr--sm icl-u-xs-mr--xs'})
        if len(company) < 1:
            real_url.append(visit)
            continue
        else:
            job_details.append(company[0].text.strip()) 

        #grab the detailed description of the job
        description = soup.findAll('div',{'class': 'jobsearch-jobDescriptionText'})
        if len(description) < 1:
            real_url.append(visit)
            continue
        else:
            job_details.append(description[0].text.strip())

        # print(job_details)
        sample_df.loc[num_s] = job_details
        print(str(num)+"/"+str(len(real_url)))

    # print(sample_df)
    sample_df.to_csv(("{}_Details.csv").format(i))
    endT = time.time()
    print(oriT - endT)

