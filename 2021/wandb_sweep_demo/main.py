import click
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# From: https://stackoverflow.com/questions/52986253/scoring-strategy-of-sklearn-model-selection-gridsearchcv-for-latentdirichletallo
class MyLDAWithPerplexityScorer(LatentDirichletAllocation):

    def score(self, X, y=None):

        # You can change the options passed to perplexity here
        score = super(MyLDAWithPerplexityScorer, self).perplexity(X, sub_sampling=False)

        # Since perplexity is lower for better, so we do negative
        return -1*score


import pandas as pd
import wandb

@click.command()
@click.option("--n_components", type=click.INT, help="num components")
@click.option("--lr_decay", type=click.FLOAT, help="no")
@click.option("--min_df", default=10, type=click.INT, help="no")
def main(n_components, lr_decay, min_df):
   wandb.init(project='bugs')
   wandb.log({
      'n_components':n_components,
      'lr_decay': lr_decay,
      'min_df': min_df,
      })

   min_vectorizer = CountVectorizer(min_df=min_df)
   df = pd.read_parquet('https://github.com/HSV-AI/bug-analysis/blob/master/data/df-xtext.parquet.gzip?raw=true')


   
   min_tf = min_vectorizer.fit_transform(df.loc[:,'text'])
   tf_feature_names = min_vectorizer.get_feature_names()
   # Materialize the sparse data
   lda = MyLDAWithPerplexityScorer(learning_method='online')
   lda.fit(min_tf)
   score = lda.score(min_tf)
   print(score)
   wandb.log({"score": score})

if __name__ == "__main__":
   main()