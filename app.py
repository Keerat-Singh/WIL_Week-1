# Importing essential libraries
from flask import Flask,render_template,request,redirect,url_for,send_from_directory,jsonify,flash
from werkzeug.utils import secure_filename
import os
import socket
import re
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity


# defining our flask application
app = Flask(__name__)
app.secret_key = 'zvzbAXPehjTMe4AmM4sk'

'''Get host IP address'''
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

df_grouped = pd.read_csv('week_1_df_v2.csv')

# Function to get recipe recommendations based on ingredients
def get_recommendations(recipe_id, df, similarities):
    # Get the index of the specified recipe
    idx = df.index[df['Recipe ID'] == recipe_id].tolist()[0]

    # Get similarity scores for the specified recipe
    recipe_similarities = similarities[idx]

    # Create a DataFrame with Recipe ID, title, and corresponding similarity scores
    sim_df = pd.DataFrame({
        'Recipe ID': df['Recipe ID'],
        'Title': df['Title'],
        'Similarity': recipe_similarities
    })

    # Sort by similarity in descending order
    sim_df = sim_df.sort_values(by='Similarity', ascending=False)

    # Exclude the recipe itself and get top 10 similar recipes
    recommendations = sim_df[sim_df['Recipe ID'] != recipe_id].head(10)

    return recommendations[['Recipe ID', 'Title']]

# @app.route('/')
# def index():
#     return render_template('index.html', options=data['options_column'])

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':    
        dictrecipe = {}
        dictrecipe.clear()
        print(df_grouped.head()) 
        selected_recipe = request.form['dropdown']
        print(selected_recipe)
        recipe_id = df_grouped[df_grouped['Title'] == selected_recipe]['Recipe ID'].values[0]
        print(recipe_id)
        ingredient_sums = df_grouped.iloc[:, 2:].sum()
        columns_to_keep = ingredient_sums[ingredient_sums >= 10].index
        df_filtered = df_grouped[['Recipe ID', 'Title'] + list(columns_to_keep)]
        rows_to_keep = df_filtered[df_filtered.iloc[:, 2:].sum(axis=1) > 5]
        rows_to_keep.reset_index(inplace= True, drop= True)
        ingredient_columns = rows_to_keep.columns[2:]
        binary_matrix = rows_to_keep[ingredient_columns].values
        n_components = 10
        pca = PCA(n_components=n_components)
        reduced_matrix = pca.fit_transform(binary_matrix)
        similarities = cosine_similarity(reduced_matrix)
        recommendations = get_recommendations(recipe_id,rows_to_keep,similarities)
        print(recommendations)
        # dictrecipe[recipe_id]= recommendations.copy()

        # if recommendations:
        
        #     resp = jsonify(recommendations)
        #     resp.status_code = 201
        #     final_dict_df = pd.DataFrame.from_dict(dictimages)
        #     orient_df = pd.DataFrame.from_dict(dictimages, orient = 'index')
        #     # final_dict_df['Images'] = images
        #     print(final_dict_df)    
        #     store_json(dictimages)
        #     store_excel(orient_df)
        #     dictimages.clear()

        return render_template('IRR_result.html', data=recommendations)
    return render_template('IRR_home.html', options=df_grouped['Title'])



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5051,debug = True)