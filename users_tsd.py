import csv
import math

file = open(r"C:\Users\uddha\Desktop\SocialBot\SocialBot\Benign196DataSet\tweets_2.csv")

reader = csv.reader(file)

# creating a list called users_tsd with user id, average tweet time as seen on a polar plot, standard deviation
# of the coordinates.
#

n = -1
users_tsd = [[]]
number_tweets = 0
sum_time = (0,0)
times = []

average_time = (0,0)
tsd = 0

for line in reader:
    if n == -1:
        n += 1
        pass
    else:  
        if len(users_tsd[n]) == 0:
            users_tsd[n].append(line[1])
        else:
            if (users_tsd[n][0] != line[1]):
                users_tsd.append([])
                average_time = (sum_time[0]/number_tweets, sum_time[1]/number_tweets)
                users_tsd[n].append(average_time)
                for i in range(len(times)):
                    squares = (average_time[0]-times[i][0])**2 + (average_time[1]-times[i][1])**2
                    tsd += squares
                tsd = tsd/number_tweets
                users_tsd[n].append(tsd)
                sum_time = (0,0)
                times = []
                number_tweets = 0
                tsd = 0
                n+= 1
            
        tweet_time_string = line[2].split()[1].split(':')
        tweet_time = (float(tweet_time_string[0])+ float(tweet_time_string[1]))
        tweet_time = (math.cos(tweet_time*3.14159/(180*24*60)), math.sin(tweet_time*3.14159/(180*24*60)))
        sum_time = (sum_time[0]+tweet_time[0], sum_time[1]+tweet_time[1])
        number_tweets += 1
        times.append(tweet_time)
    
average_time = (sum_time[0]/number_tweets, sum_time[1]/number_tweets)
users_tsd[n].append(average_time)
for i in range(len(times)):
    squares = (average_time[0]-times[i][0])**2 + (average_time[1]-times[i][1])**2
    tsd += squares
tsd = tsd/number_tweets
users_tsd[n].append(tsd)
sum_time = (0,0)
times = []
number_tweets = 0
tsd = 0
n += 1 
        
        



    
