class Song

	attr_accessor :name  #name variable gets read and write permission
	attr_reader :artist #Only read permission
	attr_writer :duration #Only write permission

	#attr_reader :NumberOfObjects # Cannot do this for class methods
	@@NumberOfObjects = 0 #Class variable
	

	def initialize(nameX, artistX, durationX)
		@name = nameX
		@artist = artistX
		@duration = durationX
		@@NumberOfObjects += 1
	end

	# Override the default to_s method
	def to_s
		"Song: #{@name} #{@artist} #{@duration}"
	end

	def duration_in_minutes
		@duration/60.0
	end

	def duration_in_minutes=(new_duration)
		@duration = (new_duration*60).to_i
	end

	def Song.PrintPlay # This is a class method
		puts "Playing song . . . ."
	end

	def NumberOfObjects # This is how we access class methods
		@@NumberOfObjects
	end

	private #Other access specifiers -> protected and public
	def printCodesName
		puts "Guru Sarath"
	end

end 


X =  Song.new('James Bond', 'Cool', 45)

puts X.inspect ##<Song:0x0000000004b22fb0 @name="James Bond", @artist="Cool", @duration=45>
puts X.to_s #Song: James Bond Cool 45
puts X.name #James Bond
X.name = "New James Bond"
puts X.to_s #Song: New James Bond Cool 45
puts X.artist #Cool
#X.artist = 'Very Cool' #This will throw an error #NO write permission
#puts X.duration #This will throw an error #NO read permission
X.duration = 90
puts X.to_s #Song: New James Bond Cool 90


puts X.to_s #Song: New James Bond Cool 90
puts X.duration_in_minutes #1.5
X.duration_in_minutes = 2
puts X.duration_in_minutes #2
puts X.to_s #Song: New James Bond Cool 120

puts X.NumberOfObjects #1

Y =  Song.new('James Bond', 'Cool', 45)
Z =  Song.new('James Bond', 'Cool', 45)

puts X.NumberOfObjects #3