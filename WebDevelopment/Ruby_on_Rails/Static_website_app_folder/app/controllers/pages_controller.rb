class PagesController < ApplicationController
  def ContactUs
    @name = 'Guru Sarath'
    @content = "This is a Ruby learning web applicaiton"
  end

  def About
    @name = 'Guru Sarath'
    @content = "Learning for Amazon 2020 Fall internship"
  end

  def KnowMore
    @content = "Vist you nearest local office"
  end
end
