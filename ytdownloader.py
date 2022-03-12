from pytube import YouTube
import time

link = input("Enter link here: ")
video = YouTube(link)

print('Title: ' , video.title)
print('Author: ',video.author)
print('Number of views: ', video.views)
print('Length of video: ', time.strftime("%H:%M:%S", time.gmtime(video.length))) #*see line 21
print('Description video: ', video.description)
print('Ratings: ', video.rating)
print('Video thumbnail link: ',video.thumbnail_url)
print('Video upload date: ',video.publish_date)

ys = video.streams.get_highest_resolution()
print('Starting download')
ys.download('''location''')
print('Download completed!')

#or you can also use this method to get the video length:
'''
hour = int(video.length / 3600)
minute = int(video.length / 60)
for i in range(hour):
    minute-=60
second = int(video.length % 60)
print(hour,':',minute,':',second)
'''