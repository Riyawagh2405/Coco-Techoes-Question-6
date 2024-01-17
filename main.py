import random
from datetime import datetime, timedelta

# Function to generate random reviews
def generate_reviews(num_reviews):
    reviews = []
    for _ in range(num_reviews):
        reviewer_name = f"User{random.randint(1, 100)}"
        review_type = random.choice(["negative", "positive", "neutral"])
        review_date = datetime.now() - timedelta(days=random.randint(0, 30))
        reviews.append({"reviewer_name": reviewer_name, "type": review_type, "date": review_date})
    return reviews

# Function to find user with maximum reviews of a specific type for a given month
def find_max_reviews(users, review_type, target_month):
    user_reviews = {user["reviewer_name"]: 0 for user in users}
    for user in users:
        if user["type"] == review_type and user["date"].month == target_month.month:
            user_reviews[user["reviewer_name"]] += 1
    max_user = max(user_reviews, key=user_reviews.get)
    return max_user, user_reviews[max_user]

# Generate random data for 20 topics with 30 reviews each
topics = [{"title": f"Topic{i}", "reviews": generate_reviews(30)} for i in range(1, 21)]

# Flatten the reviews data
all_reviews = [review for topic in topics for review in topic["reviews"]]

# Find the user with maximum negative reviews this month
this_month = datetime.now()
max_negative_user_this_month, max_negative_reviews_this_month = find_max_reviews(all_reviews, "negative", this_month)

# Find the user with maximum positive reviews this month
max_positive_user_this_month, max_positive_reviews_this_month = find_max_reviews(all_reviews, "positive", this_month)

# Find the user with maximum negative reviews last month
last_month = this_month - timedelta(days=30)
max_negative_user_last_month, max_negative_reviews_last_month = find_max_reviews(all_reviews, "negative", last_month)

# Find the user with maximum positive reviews last month
max_positive_user_last_month, max_positive_reviews_last_month = find_max_reviews(all_reviews, "positive", last_month)

# Print the results
print(f"User with maximum negative reviews this month: {max_negative_user_this_month} ({max_negative_reviews_this_month} reviews)")
print(f"User with maximum positive reviews this month: {max_positive_user_this_month} ({max_positive_reviews_this_month} reviews)")
print(f"User with maximum negative reviews last month: {max_negative_user_last_month} ({max_negative_reviews_last_month} reviews)")
print(f"User with maximum positive reviews last month: {max_positive_user_last_month} ({max_positive_reviews_last_month} reviews)")
