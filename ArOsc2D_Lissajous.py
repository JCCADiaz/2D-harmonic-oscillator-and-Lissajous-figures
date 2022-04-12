import numpy as np
import matplotlib.pyplot as plt 

'''- The following code represents the solution of a simple harmonic oscillator with two degrees of freedom, 
in this case X and Y. X and Y are in perpendicular directions.
- The Lissajous curve is the graph of the system, corresponding to the superposition of two simple harmonic 
motions in perpendicular directions.'''


class Oscillador2D:
    def __init__(self):
        self.dur_sec = 1
        
    def arOsc_solution(self, freq, delta, a=0, Amplitude=1): 
        # A general solution for a harmonic oscillator is: x(t) = A cos(ω t + a + delta), ω=2*pi*freq 
        # The parameter 'a' was included to be able to represent the solution in 2D correctly.
        t = np.linspace(0, self.dur_sec,num=1000) # default of 1000 points per curve
        data = Amplitude * np.cos(2*np.pi*freq*t + a + delta)
        return t, data 
    
    def oscillator_2D(self, freq1, delta0, nf=np.sqrt(2)):
        # The user can generalize this function by including 'ax=0', 'Ax', 'ay' and 'Ay' as input parameters.
        freq2 = nf*freq1
        delta = delta0*np.pi
        t, X = self.arOsc_solution(freq1, 0)
        t, Y = self.arOsc_solution(freq2, delta)
        return X, Y, freq1, delta
    
        
    def plot_Lissajous(self, X, Y, freq, delta):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Frequency: '+str(freq)+' Hz'+"  ::  delta: "+str(delta))
        plt.plot(X,Y) 
        
        # Remove ticks
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        ax.set_aspect('equal')
        
        plt.tight_layout()
        plt.show()
        
    def redraw_figure(self, step):
        #used to refresh a graph
        plt.draw()
        plt.pause(step)
    
    def lissajous_animated(self, m, step, freq1, delta0, nf=np.sqrt(2)):
        #Successively displays 'm' Lissajous figures, at a constant step, with increasing 'delta' values.
        X, Y, freq, delta = self.oscillator_2D(freq1, delta0, nf)
        plt.switch_backend('Qt5Agg')
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        line1, = ax.plot(X, Y, 'r-') # Returns a tuple of line objects, thus the comma
        
        fig.canvas.set_window_title('Frequency: '+str(freq)+' Hz'+"  ::  delta: "+str(delta))
        
        # Remove ticks
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        ax.set_aspect('equal')
        
        plt.tight_layout()

        for phase in np.linspace(0, 2, m):
            X, Y, freq, delta = self.oscillator_2D(freq1, delta0*phase, nf)
            
            fig.canvas.set_window_title('Frequency: '+str(freq)+' Hz'+"  ::  delta: "+str(delta))
            
            line1.set_xdata(X)
            line1.set_ydata(Y)
            self.redraw_figure(step)
            
    def drawing_Lissajous(self, step, freq1, delta0, nf=np.sqrt(2)):
        # Draw a lissajous figure point by point.
        X, Y, freq, delta = self.oscillator_2D(freq1, delta0, nf)
        plt.switch_backend('Qt5Agg')
        fig = plt.figure()
        ax = fig.add_subplot(111)
        line1, = ax.plot(X, Y, 'r-') # Returns a tuple of line objects, thus the comma
   
        fig.canvas.set_window_title('Frequency: '+str(freq)+' Hz'+"  ::  delta: "+str(delta))
        
        # Remove ticks
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        ax.set_aspect('equal')
        
        plt.tight_layout()

        for i in range (0, X.size):
            line1.set_xdata(X[:i])
            line1.set_ydata(Y[:i])
            self.redraw_figure(step)
        
        
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    # Just for illustrate...       
    A = Oscillador2D()
    A.lissajous_animated(500, 0.01, 5, 2/3, 1/3)
    A.drawing_Lissajous(0.001, 5, 2/3)



