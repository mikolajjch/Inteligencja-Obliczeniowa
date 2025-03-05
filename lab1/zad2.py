import math
import random
import matplotlib.pyplot as plt

v0 = 50
h = 100
g = 9.81

cel = random.randint(50, 340)
print(f"Cel jest w odległości {cel} metrów.")

trafiony = False
proby = 0

while not trafiony:
    proby += 1
    alpha = float(input("Kąt strzału: "))
    alpha_rad = math.radians(alpha)

    d = (v0 * math.cos(alpha_rad) / g) * (v0 * math.sin(alpha_rad) + math.sqrt(v0**2 * math.sin(alpha_rad)**2 + 2 * g * h))

    if cel - 5 <= d <= cel + 5:
        print(f"Cel trafiony, liczba prób to {proby}")
        trafiony = True
    else:
        print(f"Pocisk przeleciał {d:.2f} metrów!")

##############################################
if trafiony:
    t = [i * 0.1 for i in range(int(d * 2))]
    x = [v0 * math.cos(alpha_rad) * ti for ti in t]
    y = [-0.5 * g * ti**2 + v0 * math.sin(alpha_rad) * ti + h for ti in t]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="Trajectory of projectile", color="blue")

    plt.axvline(x=cel, color="red", linestyle="--", label=f"Distance d = {cel} m")

    plt.arrow(
        0, h,
        v0 * math.cos(alpha_rad) * 0.5,
        v0 * math.sin(alpha_rad) * 0.5,
        head_width=3,
        head_length=30,
        color="orange",
        label="Initial velocity v0 = {v0} m/s",
        #length_includes_head=True
        )

    plt.text(
        0,90, f"a = {alpha}°"
    )

################################################

    plt.title("Projectile Motion for the Trebuchet")
    plt.xlabel("Distance [m]")
    plt.ylabel("Hieght [m]")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.xlim(-5, cel + 50)
    plt.ylim(-10, max(y) + 50)
    plt.savefig("trajektoria.png")
    plt.show()

# zadanie zaproponowane przez DeepSeek jest lepsze pod względem optymalizacji i walidacji danych
