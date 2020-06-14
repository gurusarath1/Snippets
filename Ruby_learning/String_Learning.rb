puts 'Ruby'.size # Get the length of the string

name = "Guru Sarath Thangamani"

puts name[0,4] #Guru 
puts name[0..4] #Guru

puts name #Guru Sarath Thangamani
name[0,4] = 'AAAA'
puts name #AAAA Sarath Thangamani

name[0,4] = 'Guru'
puts name


# Removing the last character
StringUserX = "Hi GuysM"
StringUserX_new = StringUserX.chop
puts StringUserX_new #Hi Guys
StringUserX.chop! #Chop inplace
puts StringUserX #Hi Guys
StringUserX.chop!
puts StringUserX #Hi Guy


#String and checking
strX = "Today is a beautiful day"
puts strX.index("is") #6
puts strX.index("a") #3
puts strX.include?("day") #true
puts strX.include?("iss") #false


#Justification
strY = "Hi"
strY = strY.rjust(8, "-")
puts strY # ------Hi
strY = strY.ljust(16, "-")
puts strY # ------Hi--------

strZ = '   Aruna Devi   '
puts strZ.upcase #   ARUNA DEVI
puts strZ.downcase #   aruna devi

#Remove white spaces on both sides
strZ = strZ.strip   # Use lstrip and rstrip to strip left or right side only
puts strZ #Aruna Devi


#Strings and Arrays
strX_Array = strX.split 
print strX_Array #["Today", "is", "a", "beautiful", "day"]
strXX = "ABC-DEF-GHIJKL"
strXX_Array = strXX.split("-")
puts
print strXX_Array # ["ABC", "DEF", "GHIJKL"]


#String to number
x = "45".to_i #45
y = "a".to_i #0 (If no number)

charsInString = "ABCD_XYZ".chars
puts
print charsInString #["A", "B", "C", "D", "_", "X", "Y", "Z"]

#Find and replace
SringX = "Guru is Guru, but he is guru"
SringY = SringX.gsub("Guru", "Cat")
puts
puts SringY #Cat is Cat, but he is guru


puts SringX.count("G") #2
puts SringX.encoding #UTF-8
SringX.force_encoding("UTF-16")