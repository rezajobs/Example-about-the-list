blog_list =  [["post1", 3, 4, 5], ["post2", 4, 4, 4], ["post3", 5,3,5]]

for posts in blog_list:
    sum_list = 0

    for numbers in posts[1:]:
        sum_list = sum_list + numbers
        
    ave = sum_list/ (len(posts)-1)

    print('Average for', posts[0], 'is:', ave)
