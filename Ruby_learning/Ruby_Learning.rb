puts "Amazon intern 2020"

a = 3

if a > 3
    puts "a is greater than 3 (a = #{a})"
  else
    puts "a is not greater than 3 (a = #{a})"
end


class Book



  def initialize(title, author,num_pages)
    @title = title
    @author =  author
    @num_pages = num_pages
  end
end
#
#book1 = Book.new
book2 = Book.new("Happy feet", "Some guy", 10)
puts "#{book2.instance_variable_get(:@title)}"
