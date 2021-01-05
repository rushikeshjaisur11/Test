import turicreate as tc
model = tc.load_model("model_v1.model")
 
interested_items = ['SOSLLGM12A6D4F6F2A', 'SOVKTEK12AB0185DA2', 'SOFPFUM12AB018AC7A']
similar_items = model.get_similar_items(interested_items, k=2)
print("Application 1 : We know few insurance policies and want to find similar more insurance policies...")
print(similar_items)

interested_users = ['276aff7e222be66e5e69298f631c726907afa1cf','806ccae96c8ecb1c198482aff785ccd6bbe17143']
top_2_recommendation = model.recommend(interested_users,k=2)
print("Application 2 : To find in which insurance policy(song_id in this case) our particlar customer is interested(user_id in this case)")
print(top_2_recommendation)


#print("Initial model")
#print(model.recommend(k=5))

#popularity recommender : model which makes recommendations using item popularity.

#model2 = tc.load_model("model_v3.model")
#print("Popularity")
#print(model.recommend(k=5))
