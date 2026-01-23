from sklearn.feature_extraction.text import CountVectorizer

document = ["I love Pizza","Pizza is the best","I love pasta","Pasta is great"]
vectorizer = CountVectorizer()

X= vectorizer.fit_transform(document)
print("Vocabulary:",vectorizer.get_feature_names_out())
print("\nvecotrized array:\n",X.toarray())