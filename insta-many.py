from instaloader import Instaloader

def download_posts_with_multiple_hashtags(instaloader, hashtags, max_per_hashtag):
    posts = []
    print("Getting posts with hashtag {}".format(hashtags[0]))
    for count, post in enumerate(instaloader.get_hashtag_posts(hashtags[0])):
        posts.append(post)
        print(count + 1, sep='', end='\r', flush=True)
        if count >= max_per_hashtag - 1:
            break

    for idx, hashtag in enumerate(hashtags[1:]):
        prev_posts = posts
        posts = []
        print("\nGetting posts with hashtag {} and {}".format(hashtag,
                                                              ','.join(hashtags[:(idx + 1)])))
        for count, post in enumerate(instaloader.get_hashtag_posts(hashtag)):
            if any(p == post for p in prev_posts):
                posts.append(post)
            print("{}, {} matching".format(count + 1, len(posts)), sep='', end='\r',
                  flush=True)
            if count >= max_per_hashtag - 1:
                break

    if posts:
        print("\nDownloading posts with hashtags {}".format(','.join(hashtags)))
        for count, post in enumerate(posts):
            print("[{:03d}/{:03d}] ".format(count + 1, len(posts)), end='', flush=True)
            instaloader.download_post(post, target=','.join(hashtags))


loader = Instaloader(sleep=True, filename_pattern='{date}')
try:
    download_posts_with_multiple_hashtags(loader,
                                          hashtags=['wine', 'windturbine', 'turbine'],
                                          max_per_hashtag=2500)
except KeyboardInterrupt:
    pass
