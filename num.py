import numpy as np  
import pandas as pd
import matplotlib .pyplot as plt


a = np.array ([[1,2,3],[4,5,6]]) 
print (a.shape)

pd.DataFrame({'A':[1, 2, 3]})

panda = pd.DataFrame
print (panda)

a = [1,2,3,4,] # x værdier til fire punkter
b = [1.2, 3, 8.5, 16.3] # y værdier
c = [.1*x for x in range (0,50)] # X koordinatet går op med 0,1 imellem 0 -50
colors = np.random.rand(4) # Random farve
# Scatter plottet med farve
scatter = plt.scatter(a,b,c=colors, cmap='viridis', s=100) #S=100 gør punkterne større

coef = np.polyfit (a,b,2) # Bedste rette linje
poly1d_fn = np.poly1d(coef) # Bruges til at lave polynomier, og gør det nemmere at arbejde med dem
print ("Graf", poly1d_fn) # Printer grafen for poly1d_fn


plt.title('Andengrads polynomie') # titel på grafen
plt.xlabel('X') # Navnet på x
plt.ylabel('Y') # Navnet på y 
plt.colorbar(scatter)
plt.plot(a, b, 'bo', c, poly1d_fn(c), 'k') # Her plotter du polynomiet
plt.xlim(0, 5) # Sætter grænser for x aksen
plt.ylim(0, 17) # Sætter grænser for y aksen
plt.show()  #Printer 
