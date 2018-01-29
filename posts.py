from blog.models import Post

posts = Post.objects.all()
post = posts[0]
print(post)
print(type(post))
# print(dir(post))
for elem in dir(post):
  print("Trying: %s" % elem)
  if elem[0] != "_":
    print("Interesting: %s" % elem)
