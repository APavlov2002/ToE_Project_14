import managers.managers as man


x_corner = 3
y_corner = 3
h_s = 1
time = 1
h = 0.01
square = man.create_material_body(x_corner, y_corner, h_s)
tr = move_material_body(time, h, square)

plot_trajectory(square, tr)


vf = man.move_through_space(1, 0.1)
plot_velocity_fields(vf)
