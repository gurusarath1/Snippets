a = 3
loop do

	if(a < 0)
		break
	end

	puts "value of a = " + a.to_s
	a = a - 1

end
=begin
value of a = 3
value of a = 2
value of a = 1
value of a = 0	
=end

a = 0
while a < 10
	print a.to_s + " "
	a += 2
end
#0 2 4 6 8

puts

for i in 1..5 do
	print i.to_s + ", "
end
#1, 2, 3, 4, 5,

puts

x = ["Apple", "Orange", "Peas", "Mango", "Grapes"]
for i in x do
	print i
end
#AppleOrangePeasMangoGrapes

puts

#Iterators

#each with a block
count = 1
x.each {|name| puts count.to_s + " - " + name; count += 1}
=begin
1 - Apple
2 - Orange
3 - Peas
4 - Mango
5 - Grapes
=end
puts

nums = [4,7,8,1,2,1]
sum = 0
nums.each do |numX|
	sum += numX
end

puts sum #23

5.times do |numY|
	print numY.to_s + ", "
end
#0, 1, 2, 3, 4,