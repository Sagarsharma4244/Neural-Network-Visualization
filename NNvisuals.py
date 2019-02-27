import pygame

Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
display_x = 800
display_y = 600

gameDisplay = pygame.display.set_mode((display_x,display_y))
pygame.init()


gameDisplay.fill(White)


def text_objects(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()


def button(x,y, w, h, msg, prev_msg):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	# print(mouse)

	if x + w >mouse[0]  >x and y + h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, Green, (x,y, w, h))
		if click[0] == 1:
			
			prev_msg = msg
			# print(prev_msg)
			return prev_msg
		
	else:
		pygame.draw.rect(gameDisplay, White, (x,y, w, h))
		
	smallText = pygame.font.SysFont("comicsansms",20)
	textSurf, textRect = text_objects(str(msg), smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)

	return prev_msg


def map( x,  in_min,  in_max,  out_min,  out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def getweigshad(weights, r, c ):
	sup=[]
	for i in weights:
		for k in i:
			sup.append(k)
	# return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
	kal =  map(weights[r][c], min(sup), max(sup), 255, 10)
	return int(kal)



def getnodeRad(layer, index, ipCategory ): # ipCategory is columns
		dup=[]
		for i in layer:
			for k in i:
				dup.append(k)

		# return (x - in_min) * (out_max-out_min) / (in_max - in_min) + out_max;	
		val =  map(layer[ipCategory][index], min(dup), max(dup), 5, 25)
		return int(val)

class start:
	def __init__(self, Layer0, weights1, Layer1, weights2, Layer2):
		
		self.Layer0 = Layer0
		self.weights1 = weights1
		self.Layer1 = Layer1
		self.weights2 = weights2
		self.Layer2 = Layer2
		self.prev_msg = 0

		

	def makeNodesList(self):
		# ipcat = L0[0]
		L0Nodes = self.Layer0.shape[1]
		W1Lines = self.weights1.shape[0]
		L1Nodes = self.Layer1.shape[1]
		W2Lines = self.weights2.shape[0]
		L2Nodes = self.Layer2.shape[1]

		return L0Nodes,L1Nodes, L2Nodes

	def drawNode(self, L0Nodes,L1Nodes, L2Nodes):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
					
			pygame.display.update()
			gameDisplay.fill(White)

			ipCategory = button(50,10, 100, 30, 0, self.prev_msg)
			self.prev_msg = ipCategory
			ipCategory = button(250,10, 100, 30, 1, self.prev_msg)
			self.prev_msg = ipCategory
			ipCategory = button(450,10, 100, 30, 2, self.prev_msg)
			self.prev_msg = ipCategory
			ipCategory = button(650,10, 100, 30, 3, self.prev_msg)
			self.prev_msg = ipCategory
			# print(ipCategory)
			smallText = pygame.font.SysFont("comicsansms",20)
			textSurf, textRect = text_objects(str(self.prev_msg), smallText)
			textRect.center = ( display_x /2, 19*(display_y/20) )
			gameDisplay.blit(textSurf, textRect)
			
			total_no_of_layers = 3
			margin_x = int(display_x/ (total_no_of_layers+1))
			# Draw and Update Nodes
			position =[[],[],[]]
			x = margin_x
			
			for index  in range(L0Nodes):
				margin_y = int(display_y/ (L0Nodes+1))
				y = (index+1) * margin_y
				position[0].append((x,y))
				current_Node_Rad = getnodeRad(self.Layer0, index, ipCategory )
				pygame.draw.circle(gameDisplay, Black, (x,y),current_Node_Rad + 2, 1)
				pygame.draw.circle(gameDisplay, Black, (x,y) ,current_Node_Rad)
				

			x = 2*margin_x
			# CONNECT NODES OF L1 TO L0 WITH WEIGHTS BY STORING THE POSITION OF L0 NODES IN A ARRAY FROM PREVIOUS FOR LOOP
			for index  in range(L1Nodes):
				margin_y = int(display_y/ (L1Nodes+1))
				y = (index+1) * margin_y
				position[1].append((x,y))
				
				# Draw Nodes
				current_Node_Rad = getnodeRad(self.Layer1, index, ipCategory )
				pygame.draw.circle(gameDisplay, Black, (x,y),current_Node_Rad + 2, 1)
				pygame.draw.circle(gameDisplay, Black, (x,y) ,current_Node_Rad)

				# Draw and Connect Weights
				for i in range(L0Nodes):  
					if self.Layer0[ipCategory][i] == 1:
						shade = getweigshad(self.weights1, i, index)
						pygame.draw.line(gameDisplay, (shade,shade,shade) ,(x,y),(position[0][i]), 3)
				

			x = 3*margin_x
			for index  in range(L2Nodes):
				margin_y = int(display_y/ (L2Nodes+1))
				y = (index+1) * margin_y
				position[2].append((x,y))

				# Draw Nodes
				current_Node_Rad = getnodeRad(self.Layer2, index, ipCategory )
				pygame.draw.circle(gameDisplay, Black, (x,y),current_Node_Rad + 2, 1)
				pygame.draw.circle(gameDisplay, Black, (x,y) ,current_Node_Rad)

				# Draw and Connect Weights
				if self.Layer2[ipCategory][index] >=0.8:
					for i in range(L1Nodes):
						shade = getweigshad(self.weights2, i, index)
						pygame.draw.line(gameDisplay, (shade,shade,shade),(x,y),(position[1][i]), 3)