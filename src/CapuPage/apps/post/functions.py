from apps.post.models import Post, Category


def get_categories():
    posts = Post.objects.all()
    categories = []
    categories_1 = []
    categories_2 = []
    counter = 0
    for post in posts:
        if post.category.number not in categories:
            number = post.category.number
            categories.append(number)
            if counter % 2 == 0:
                categories_1.append(Category.objects.get(number=number))
            else:
                categories_2.append(Category.objects.get(number=number))
            counter += 1
    return categories_1, categories_2
