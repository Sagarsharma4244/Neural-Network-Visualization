import numpy as np
import matplotlib.pyplot as plt



def plot_loss(Total_final_loss,x, y1):
	for i in range(len(Total_final_loss)):
		y1[0].append(Total_final_loss[i][0][0])
		y1[1].append(Total_final_loss[i][0][1])
		y1[2].append(Total_final_loss[i][1][0])
		y1[3].append(Total_final_loss[i][1][1])
		y1[4].append(Total_final_loss[i][2][0])
		y1[5].append(Total_final_loss[i][2][1])
		y1[6].append(Total_final_loss[i][3][0])
		y1[7].append(Total_final_loss[i][3][1])
		x.append(i)
	
	plt.title("Final Loss")
	plt.figure(1)
	plt.plot(x ,y1[0])
	plt.plot(x ,y1[1])
	plt.plot(x ,y1[2])
	plt.plot(x ,y1[3])
	plt.plot(x ,y1[4])
	plt.plot(x ,y1[5])
	plt.plot(x ,y1[6])
	plt.plot(x ,y1[7])
	
	# plt.show()


def plot_grad(Gradient_desc_L2, y2, x1):
	for i in range(len(Gradient_desc_L2) -1):
		y2[0].append(Gradient_desc_L2[i+1][0][0])
		y2[1].append(Gradient_desc_L2[i+1][0][1])
		y2[2].append(Gradient_desc_L2[i+1][1][0])
		y2[3].append(Gradient_desc_L2[i+1][1][1])
		y2[4].append(Gradient_desc_L2[i+1][2][0])
		y2[5].append(Gradient_desc_L2[i+1][2][1])
		y2[6].append(Gradient_desc_L2[i+1][3][0])
		y2[7].append(Gradient_desc_L2[i+1][3][1])
		x1.append(i)
	
	
	plt.figure(2)
	plt.title("Gradient Descent")
	plt.plot(x1 ,y2[0])
	plt.plot(x1 ,y2[1])
	plt.plot(x1 ,y2[2])
	plt.plot(x1 ,y2[3])
	plt.plot(x1 ,y2[4])
	plt.plot(x1 ,y2[5])
	plt.plot(x1 ,y2[6])
	plt.plot(x1 ,y2[7])
	
	# plt.show()


def plot_weight1(Total_weights1, x_ax1, y_ax1 ):
	for i in range(len(Total_weights1)):
		
		x_ax1.append(i)
	
	plt.figure(3)
	plt.title("Weight1")
	plt.plot(x_ax1 ,y_ax1[0])
	plt.plot(x_ax1 ,y_ax1[1])
	plt.plot(x_ax1 ,y_ax1[2])
	plt.plot(x_ax1 ,y_ax1[3])
	plt.plot(x_ax1 ,y_ax1[4])
	plt.plot(x_ax1 ,y_ax1[5])
	plt.plot(x_ax1 ,y_ax1[6])
	plt.plot(x_ax1 ,y_ax1[7])
	plt.plot(x_ax1 ,y_ax1[8])
	plt.plot(x_ax1 ,y_ax1[9])
	plt.plot(x_ax1 ,y_ax1[10])
	plt.plot(x_ax1 ,y_ax1[11])
	plt.plot(x_ax1 ,y_ax1[12])
	plt.plot(x_ax1 ,y_ax1[13])
	plt.plot(x_ax1 ,y_ax1[14])
	plt.plot(x_ax1 ,y_ax1[15])
	plt.plot(x_ax1 ,y_ax1[16])
	plt.plot(x_ax1 ,y_ax1[17])
	# plt.show()
def record_weight1(Total_weights1, y_ax1,i):
	y_ax1[0].append(Total_weights1[i][0][0])
	y_ax1[1].append(Total_weights1[i][0][1])
	y_ax1[2].append(Total_weights1[i][0][2])
	y_ax1[3].append(Total_weights1[i][0][3])
	y_ax1[4].append(Total_weights1[i][0][4])
	y_ax1[5].append(Total_weights1[i][0][5])
	y_ax1[6].append(Total_weights1[i][1][0])
	y_ax1[7].append(Total_weights1[i][1][1])
	y_ax1[8].append(Total_weights1[i][1][2])
	y_ax1[9].append(Total_weights1[i][1][3])
	y_ax1[10].append(Total_weights1[i][1][4])
	y_ax1[11].append(Total_weights1[i][1][5])
	y_ax1[12].append(Total_weights1[i][2][0])
	y_ax1[13].append(Total_weights1[i][2][1])
	y_ax1[14].append(Total_weights1[i][2][2])
	y_ax1[15].append(Total_weights1[i][2][3])
	y_ax1[16].append(Total_weights1[i][2][4])
	y_ax1[17].append(Total_weights1[i][2][5])



def plot_weight2(Total_weights2, x_ax, y_ax):
	for i in range(len(Total_weights2)):
		
		x_ax.append(i)
	
	plt.figure(4)
	plt.title("Weight2")
	plt.plot(x_ax ,y_ax[0])
	plt.plot(x_ax ,y_ax[1])
	plt.plot(x_ax ,y_ax[2])
	plt.plot(x_ax ,y_ax[3])
	plt.plot(x_ax ,y_ax[4])
	plt.plot(x_ax ,y_ax[5])
	plt.plot(x_ax ,y_ax[6])
	plt.plot(x_ax ,y_ax[7])
	plt.plot(x_ax ,y_ax[8])
	plt.plot(x_ax ,y_ax[9])
	plt.plot(x_ax ,y_ax[10])
	plt.plot(x_ax ,y_ax[11])
def record_weight2(Total_weights2, y_ax,i):
	y_ax[0].append(Total_weights2[i][0][0])
	y_ax[1].append(Total_weights2[i][0][1])
	y_ax[2].append(Total_weights2[i][1][0])
	y_ax[3].append(Total_weights2[i][1][1])
	y_ax[4].append(Total_weights2[i][2][0])
	y_ax[5].append(Total_weights2[i][2][1])
	y_ax[6].append(Total_weights2[i][3][0])
	y_ax[7].append(Total_weights2[i][3][1])
	y_ax[8].append(Total_weights2[i][4][0])
	y_ax[9].append(Total_weights2[i][4][1])
	y_ax[10].append(Total_weights2[i][5][0])
	y_ax[11].append(Total_weights2[i][5][1])

