from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
consumer_key='xxxxxxxxxxx'
consumer_secret='xxxxxxxxxxxx'
access_token='xxxxxxxxxx-xxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxx'
class StdOutListener(StreamListener):
	def on_data(self, data):
		d2=data[109:]
		for x in range(0,len(d2)):
			if d2[x]=='"':
				E=x
				break
		G=0
		for x in range(0,len(d2)):
			if d2[x]=='n':
				G=G+1
				F=x+1
				if G==3:
					break
		text=d2[F:E]
		text=text.replace('\\u200a','').replace('\\u2705','2').replace('\\ud83d\\udd36','1').replace('\\ud83d\\udd35','0')
		print(text)
		log=open('log.txt', 'w')
		log.write(text)
		return True
	def on_error(self, status):
		print(status)
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, StdOutListener())
stream.filter(track=['↪@AntiBotus'])
