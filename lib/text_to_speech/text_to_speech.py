import speake3

def readText(phrase):
    engine = speake3.Speake()
    engine.set('voice', 'en')
    engine.set('speed', '104')
    engine.set('pitch', '99')
    engine.say(phrase)
    engine.talkback()
