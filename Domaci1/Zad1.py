import particle as prt

p1 = prt.particle()

p1.set_initial_conditions(10, 60, 0, 0, 0.01)

print("Ukupno vrijeme trajanja gibanje iznosi: {:.2f}s".format(p1.total_time()))
print("Najveca ostvarena brzina iznosi: {:.2f}m/s".format(p1.max_speed()))

p1.velocity_to_hit_target(4, 4, 1)
p1.reset()    

p1.set_initial_conditions(10, 60, 0, 0, 0.01)
p1.angle_to_hit_target(4, 2, 0.5)  
p1.reset()

