import numpy as np
import matplotlib.pyplot as plt
import graphs
import NNvisuals

x =[]
y1 =[[],[],[],[],[],[],[],[]]
Total_final_loss = []
x1 =[]
y2 =[[],[],[],[],[],[],[],[]]
Gradient_desc_L2 = []
x_ax = []
y_ax = [[],[],[],[],[],[],[],[],[],[],[],[]]
Total_weights2 = []
x_ax1 = []
y_ax1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
Total_weights1 = []




def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative( x): #Slope
    return x * (1.0 - x)

class NeuralNetwork:
    def __init__(self, x, y):
        self.Layer0      = x
        # print("Layer0s = " + str(self.Layer0))
        self.y          = y
        # print("Y = " + str(self.y))
        self.Layer2     = np.zeros(self.y.shape)
        # print("Layer2 = " + str(self.Layer2))
        Nodes_Layer1 = 6  # Choose what you want.
        Nodes_Layer2 = len(y[0])
        self.weights1   = np.random.rand(self.Layer0.shape[1], Nodes_Layer1 ) 
        # print("Weights1 = " + str(self.weights1))
        self.weights2   = np.random.rand( Nodes_Layer1, Nodes_Layer2 )     
        # print("Weights2 = " + str(self.weights2))  
        print("Initial Weights1  = \n" + str(self.weights1))
        print("Initial Weights2  = \n" + str(self.weights2))

    def feedforward(self):
        self.Layer1 = sigmoid(np.dot(self.Layer0, self.weights1))
        self.Layer2 = sigmoid(np.dot(self.Layer1, self.weights2))

    def backprop(self):
    	# application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
    	Final_Cost = 2*(self.y - self.Layer2) * sigmoid_derivative(self.Layer2)
    	d_weights2 = np.dot(self.Layer1.T, Final_Cost)
    	Total_final_loss.append(Final_Cost)
    	Layer1_Cost = np.dot(Final_Cost, self.weights2.T) * sigmoid_derivative(self.Layer1)
    	d_weights1 = np.dot(self.Layer0.T, Layer1_Cost)
    	# update the weights with the derivative (slope) of the loss function
    	self.weights1 += d_weights1
    	self.weights2 += d_weights2
    	# print(self.weights2[5][1])
    	Total_weights2.append(self.weights2)
    	Gradient_desc_L2.append(sigmoid_derivative(self.Layer2))
    	graphs.record_weight2(Total_weights2, y_ax,i)
    	Total_weights1.append(self.weights1)
    	graphs.record_weight1(Total_weights1, y_ax1,i)

    def test(self):
    	self.Layer0 = [1,0,1]
    	self.Layer1 = sigmoid(np.dot(self.Layer0, self.weights1))
    	self.Layer2 = sigmoid(np.dot(self.Layer1, self.weights2))
    	
    	return self.Layer2

if __name__ == "__main__":
    X = np.array([[0,1,1],
                  [0,0,1],
                  [1,0,1],
                  [1,1,0]])
    y = np.array([[1,0,0,0],
    			  [0,1,0,0],
    			  [0,0,1,0],
    			  [0,0,0,1]])

    # print(y.shape)
    nn = NeuralNetwork(X,y)
    for i in range(1000):
    	nn.feedforward()
    	nn.backprop()

    graphs.plot_loss(Total_final_loss,x, y1)
    graphs.plot_grad(Gradient_desc_L2, y2, x1)
    graphs.plot_weight1(Total_weights1, x_ax1, y_ax1)
    graphs.plot_weight2(Total_weights2, x_ax, y_ax)
    
    # print("#" + str(i)+ "   "  + str(nn.Layer2[0]) + "  " + str(nn.Layer2[1]) + "  " + str(nn.Layer2[2]) + "  " + str(nn.Layer2[3]))
    print("INPUTS/ LAEYER0 = ") 
    print( nn.Layer0)
    print("Trained Weights1  = ")
    print(nn.weights1)
    print("Trained Layer 1  = ")
    print(nn.Layer1)
    print("Trained Weights2  = ")
    print(nn.weights2)
    print("Trained Layer 2  = ") 
    print(nn.Layer2)
    # print(Total_final_loss)
    
    NNV = NNvisuals.start(nn.Layer0, nn.weights1, nn.Layer1, nn.weights2, nn.Layer2)
    L0Nodes,L1Nodes, L2Nodes = NNV.makeNodesList()
    NNV.drawNode(L0Nodes, L1Nodes, L2Nodes)
    # print(nn.Layer0.shape)
    # print(nn.weights1.shape)
    # print(nn.Layer1.shape)
    # print(nn.weights2.shape)
    # print(nn.Layer2.shape)
    # print("Test output  ")
    # print(nn.test())
    plt.show()

    