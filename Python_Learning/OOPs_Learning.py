# Written by Guru Sarath
# 17 - Nov - 2018

class Box:

	def __init__(self, l, b, h):
		self.l = l
		self.b = b
		self.h = h

	def volume(self):
		print(self.l * self.b * self.h)

	def __add__(self, rhs):
		new_l = self.l + rhs.l
		new_b = self.b + rhs.b
		new_h = self.h + rhs.h
		newBox = Box(new_l, new_b, new_h)
		return (newBox)

	def __str__(self):
		return (str(self.l) + '-' + str(self.b) + '-' + str(self.h))


box1 = Box(1,2,3)
box2 = Box(1,1,1)
box3 = box1 + box2


box1.volume()
box3.volume()
print(str(box3))

