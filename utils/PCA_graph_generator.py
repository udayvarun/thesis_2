import matplotlib.pyplot as plt

PCA = [1, 2, 3, 4, 5, 6, 7]
Error = [3.3557725930213493, 3.1219989438901004, 2.132287199403614, 
         1.6788126842571727, 0.488758132805126, 0.3242852634378725, 0.01012521789674953]
Time = [5, 9, 7, 9, 14, 20, 23]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(PCA, Error, marker='o', label="Error", color="blue")
plt.title("PCA Components vs Error")
plt.xlabel("PCA Components")
plt.ylabel("Error")
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(PCA, Time, marker='o', label="Time", color="orange")
plt.title("PCA Components vs Time")
plt.xlabel("PCA Components")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(r"experiment_data_set\figures\pca_time_error_plot.png")
plt.show()
