class Song:
  def __init__(self, **dic):
    self.update(**dic)

  @classmethod
  def from_dict(cls, dic):
    return cls(**dic)

  def to_dict(self):
    return {
      'title': self.title,
      'uploader': self.uploader,
      'duration': self.duration,
      'url': self.url
    }

  def update(self, **dic):
    if ('title' in dic) and (dic['title']):
      self.title = dic['title']
    if ('uploader' in dic) and (dic['uploader']):
      self.uploader = dic['uploader']
    if ('duration' in dic) and (dic['duration']):
      self.duration = int(dic['duration'])
    if ('url' in dic) and (dic['url']):
      self.url = dic['url']
    if ('thumbnail' in dic) and (dic['thumbnail']):
      self.thumbnail = dic['thumbnail']
    if ('upload_date' in dic) and (dic['upload_date']):
      self.upload_date = dic['upload_date']
    if ('view_count' in dic) and (dic['view_count']):
      self.view_count = int(dic['view_count'])
    if ('like_count' in dic) and (dic['like_count']):
      self.like_count = int(dic['like_count'])
    if ('description' in dic) and (dic['description']):
      self.description = dic['description']

  def fixed_duration(self):
    m, s = divmod(self.duration, 60)
    h, m = divmod(m, 60)
    if h > 0:
      return f'{h:02d}:{m:02d}:{s:02d}'
    else:
      return f'{m:02d}:{s:02d}'
  
  def fixed_title(self, limit = 60):
    t = self.title
    t = ' '.join(t.split(' '))
    if t[0] == ' ':
      t = t[1:]
    if t[-1] == ' ':
      t = t[:-1]
    cs = ['|', '`', '*', '_', '>']
    for c in cs:
      t = t.replace(c, '')
    if len(t) > limit:
      t = t[:limit] + '...'
    return t
   
  def fixed_uploader(self, limit = 32):
    t = self.uploader
    t = ' '.join(t.split(' '))
    if t[0] == ' ':
      t = t[1:]
    if t[-1] == ' ':
      t = t[:-1]
    cs = ['|', '`', '*', '_', '>']
    for c in cs:
      t = t.replace(c, '')
    if len(t) > limit:
      t = t[:limit] + '...'
    return t
  
  def to_str(self, limit = True):
    if limit:
      return f'🕒 {self.fixed_duration()} 🎵 {self.fixed_title()} 👤 {self.fixed_uploader()}';
    else:
      return f'🕒 {self.fixed_duration()} 🎵 {self.fixed_title(999)} 👤 {self.fixed_uploader(999)}';

    