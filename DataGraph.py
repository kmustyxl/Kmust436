from AssignRule import *
import matplotlib.pyplot as plt
import time
start_time = time.clock()
the_best, the_worst = Bayes_net(pop_gen, ls_frequency)
end_time = time.clock()
run_time = end_time - start_time
gen = [i for i in range(pop_gen)]
fig = plt.figure(2)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
plt.sca(ax1)
plt.title('$Distributed$'+' '+'$flowshop$'+' '+'$scheduling$'+' '+'$problem$'+'\nRun:%ss'%run_time+'\n$Factory1$')
plt.ylabel(u'fitness')
plt.plot(gen, the_best[0], 'b',label = '$Best$')
plt.plot(gen, the_worst[0], 'r',label = '$Worst$')
plt.legend()
plt.grid()
plt.sca(ax2)
plt.title('$Factory1$')
plt.xlabel(u'gen')
plt.ylabel(u'fitness')
plt.plot(gen, the_best[1], 'b',label = '$Best$')
plt.plot(gen, the_worst[1], 'r',label = '$Worst$')
plt.legend()
plt.grid()
plt.show()


