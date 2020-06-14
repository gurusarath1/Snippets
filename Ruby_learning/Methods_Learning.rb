def simpleMethod
	"Last statement is returned by default"
end

puts simpleMethod #Last statement is returned by default

def methodWithArgument(first, second = "all")
	return "Message: #{first} #{second}"
end

puts methodWithArgument("Hi", "Guru") #Message: Hi Guru
puts methodWithArgument("Hi") #Message: Hi all

def methodWithVariableLengthArguments(first, *rest)
	return first + ", " + rest.join(", ")
end

puts methodWithVariableLengthArguments("Apple", "Mango", "Orange", "Papaya", "Coconut")

def method3(*input)

	if block_given?
	
		input.each do |x|
			yield(x)
		end

	else
		puts "Block was not given !"
	end

end


method3("Plants", "Tree", "Animal", "Pipe") #Block was not given !

method3("Plants", "Tree", "Animal", "Pipe") { |fromFunction| puts "Yielded this - #{fromFunction} "}
=begin
Yielded this - Plants
Yielded this - Tree
Yielded this - Animal
Yielded this - Pipe
=end