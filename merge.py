import pandas as pd

locations = ['Los+Angeles%2C+CA','Chicago%2C+IL','Houston%2C+TX','Phoenix%2C+AZ','Philadelphia%2C+PA','San+Antonio%2C+TX','San+Diego%2C+CA','Dallas%2C+TX','San+Jose%2C+CA','Austin%2C+TX','Jacksonville%2C+FL','San+Francisco%2C+CA','Columbus%2C+OH','Indianapolis%2C+IN','Fort+Worth%2C+TX','Charlotte%2C+NC','Seattle%2C+WA','Denver%2C+CO','El+Paso%2C+TX','Boston%2C+MA','Detroit%2C+MI','Nashville%2C+TN','Memphis%2C+TN','Portland%2C+OR','Oklahoma+City%2C+OK','Las+Vegas%2C+NV','Louisville%2C+KY','Baltimore%2C+MD','Milwaukee%2C+WI','Albuquerque%2C+NM','Tucson%2C+AZ','Fresno%2C+CA','Sacramento%2C+CA','Mesa%2C+AZ','Kansas+City%2C+MO','Atlanta%2C+GA','Long+Beach%2C+CA','Omaha%2C+NE','Colorado+Springs%2C+CO','Raleigh%2C+NC','Miami%2C+FL','Virginia+Beach%2C+VA','Oakland%2C+CA','Minneapolis%2C+MN','Tulsa%2C+OK','Arlington%2C+TX','New+Orleans%2C+LA','Wichita%2C+KS','Cleveland%2C+OH','Tampa%2C+FL','Bakersfield%2C+CA','Aurora%2C+CO','Urban+Honolulu%2C+HI','Anaheim%2C+CA','Santa+Ana%2C+CA','Corpus+Christi%2C+TX','Riverside%2C+CA','Lexington%2C+KY','St.+Louis%2C+MO','Stockton%2C+CA','Pittsburgh%2C+PA','St.+Paul%2C+MN','Cincinnati%2C+OH','Anchorage%2C+AK','Henderson%2C+NV','Greensboro%2C+NC','Plano%2C+TX','Lincoln%2C+NE','Newark%2C+NJ','Toledo%2C+OH','Orlando%2C+FL','Chula+Vista%2C+CA','Irvine%2C+CA','Durham%2C+NC','Fort+Wayne%2C+IN','Jersey+City%2C+NJ','St.+Petersburg%2C+FL','Laredo%2C+TX','Buffalo%2C+NY','Madison%2C+WI','Lubbock%2C+TX','Chandler%2C+AZ','Scottsdale%2C+AZ','Norfolk%2C+VA','Glendale%2C+AZ','Reno%2C+NV','Winston-Salem%2C+NC','Irving%2C+TX','Garland%2C+TX','Chesapeake%2C+VA','Gilbert%2C+AZ','Hialeah%2C+FL','North+Las+Vegas%2C+NV','Paradise%2C+NV','Fremont%2C+CA','Arlington%2C+VA','Baton+Rouge%2C+LA','Boise+City%2C+ID','Richmond%2C+VA']

url = pd.read_csv('New+York%2C+NY_url.csv', delimiter=",")
detail = pd.read_csv('New+York%2C+NY_Details.csv', delimiter=",")
df_jobs = pd.merge(url, detail, on=['url', 'url'])

for i in locations:
    urls_name = "{}_url.csv".format(i)
    details_name = "{}_Details.csv".format(i)
    url = pd.read_csv(urls_name, delimiter=",")
    detail = pd.read_csv(details_name, delimiter=",")
    all_details = pd.merge(url, detail, on=['url', 'url'])
    df_jobs = pd.concat([df_jobs, all_details])

df_jobs=df_jobs.drop(columns='Unnamed: 0_x')
df_jobs=df_jobs.drop(columns='Unnamed: 0_y')
df_jobs=df_jobs.drop(columns='title_y')
df_jobs.rename(columns={'title_x':'title'}, inplace=True)
print(df_jobs)
df_jobs.to_csv("indeed_details.csv")