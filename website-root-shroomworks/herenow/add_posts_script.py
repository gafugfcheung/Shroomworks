array = []
array.append(['Post 1', 'posts/Photo1.jpg', 34.457273, 6.191111])
array.append(['Post 2', 'posts/Photo2.jpg', 38.660948, -2.832371])
array.append(['Post 3', 'posts/Photo3.jpg', 41.622547, 13.241491])
array.append(['Post 4', 'posts/Photo4.jpg', 45.275715, 2.530006])
array.append(['Post 5', 'posts/Photo5.jpg', 47.543471, 9.013686])
array.append(['Post 6', 'posts/Photo6.jpg', 57.066100, -4.443216])
array.append(['Post 7', 'posts/Photo7.jpg', 51.640808, -0.149897])
array.append(['Post 8', 'posts/Photo8.jpg', 51.646455, 6.691372])
array.append(['Post 9', 'posts/Photo9.jpg', 52.736266, 12.276732])
array.append(['Post 10', 'posts/Photo10.jpg', 49.270427, 17.363879])
array.append(['Post 11', 'posts/Photo11.jpg', 44.645009, 23.553241])
array.append(['Post 12', 'posts/Photo12.jpg', 61.305673, 6.729652])
array.append(['Post 13', 'posts/Photo13.jpg', 58.816978, 16.900343])
array.append(['Post 14', 'posts/Photo14.jpg', 55.106565, 24.384436])
array.append(['Post 15', 'posts/Photo15.jpg', 49.358012, 29.990032])
array.append(['Post 16', 'posts/Photo16.jpg', 37.881976, 30.909031])
array.append(['Post 17', 'posts/Photo17.jpg', 44.102645, 37.145775])
array.append(['Post 18', 'posts/Photo18.jpg', 34.554323, 43.478470])
array.append(['Post 19', 'posts/Photo19.jpg', 40.484530, 49.139515])
array.append(['Post 20', 'posts/Photo20.jpg', 43.964683, 60.077805])
array.append(['Post 21', 'posts/Photo21.jpg', 58.221728, 36.556270])
array.append(['Post 22', 'posts/Photo22.jpg', 60.605470, 56.939094])
array.append(['Post 23', 'posts/Photo23.jpg', 53.713835, 47.565175])
array.append(['Post 24', 'posts/Photo24.jpg', 52.146938, 59.432245])

u = User.objects.get(id=4)
p = Profile.objects.get(user=u)

for a in array:
    lat = a[2]
    lon = a[3]
    cap = a[0]
    img = a[1]
    print str(lat) + " - " + str(lon) + " - " + cap + " - " + img
    location = Location.objects.create(lat=lat, lon=lon)
    post = Post.objects.create(location=location, profile=p)
    post.caption = cap
    post.image = img
    post.save()
