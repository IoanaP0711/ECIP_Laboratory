#simpulate the true system state
#consider a simple system: x(t+1)=x(t)+1
#generate the true state x(t) for 50 simple steps
#plot the evolution of the true state
#true state= starea reala, exacta, a sistemului(fara erori, fara zgomot)

#!/usr/bin/env python3
import matplotlib.pyplot as plt


steps = 50
x0 = 0  
x = [x0]
for t in range(steps):
    x.append(x[-1] + 1)


t = list(range(steps + 1))

plt.figure(figsize=(8, 4))
plt.plot(t, x, marker="o")
plt.title("True System State Evolution (no noise)")
plt.xlabel("Time step t")
plt.ylabel("True state x(t)")
plt.grid(True)
plt.tight_layout()
plt.show()