module PagesHelper

  def putName_Custom_Helper_function
    if @name.nil?
      return "NO NAME (recieved from pages_helper.rb)"
    else
      return @name + "(recieved from pages_helper.rb)"
    end
  end


end
