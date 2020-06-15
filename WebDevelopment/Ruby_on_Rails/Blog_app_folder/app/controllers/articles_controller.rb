class ArticlesController < ApplicationController

  def index
    @articles = Article.all
  end

  # CREATING NEW
  def new
    @article = Article.new(:title => "12345")
  end

  #When you press the submit button
  def create
    #render plain: params[:article].inspect
    @article = Article.new(params.require(:article).permit(:title,:text))
    if @article.save
      redirect_to @article
    else
      render 'new'
    end
  end

  def show
    @article = Article.find(params[:id])
  end


  # EDITING
  def edit
    @article = Article.find(params[:id])
  end

  def update
    @article = Article.find(params[:id])

    if @article.update(article_params)
      redirect_to @article
    else
      render 'edit'
    end
  end


  def destroy
    @article = Article.find(params[:id])
    @article.destroy

    redirect_to articles_path
  end



end
