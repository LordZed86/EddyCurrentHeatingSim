import sympy as sp

# Given Constants
sigma_nickel = 1.450e7  # Conductivity of nickel (S/m)
c_water = 4184  # Specific heat of water (J/kg°C)
m_water = 0.03  # Mass of water (kg) (set as a constant for this experiment)
t = 300  # Time interval (s) ( set intervals for this experiment)

# Thickness of nickel (estimate) (small nickle plate submerged in water)
d_nickel = 0.001  # meters (1 mm)

# Experimental temperature changes (average from data)
delta_T_550 = 1.0  # °C (from 550 RPM trials)
delta_T_2000 = 1.0  # °C (from 2000 RPM trials)

# Angular velocities
omega_550 = 57.59  # rad/s
omega_2000 = 209.43  # rad/s

# Equation for Power from eddy currents
B = sp.symbols('B', real=True, positive=True)
P_550_expr = (B**2 * d_nickel**2 * sigma_nickel * omega_550**2) / 2
P_2000_expr = (B**2 * d_nickel**2 * sigma_nickel * omega_2000**2) / 2

# Heat transfer equation
Q_550 = m_water * c_water * delta_T_550
Q_2000 = m_water * c_water * delta_T_2000

# Solve for B from observed temperature changes
B_550_solution = sp.solve(P_550_expr * t - Q_550, B)[0]
B_2000_solution = sp.solve(P_2000_expr * t - Q_2000, B)[0]

# User input for custom RPM
custom_rpm = float(input("Enter RPM: "))
omega_custom = custom_rpm * (2 * sp.pi / 60)

P_custom_expr = (B_2000_solution**2 * d_nickel**2 * sigma_nickel * omega_custom**2) / 2
Q_custom = P_custom_expr * t
delta_T_custom = Q_custom / (m_water * c_water)

# Use estimated B to predict temperature rise at higher RPMs (e.g., 5000 RPM and 10,000 RPM)
omega_5000 = 5000 * (2 * sp.pi / 60)
omega_10000 = 10000 * (2 * sp.pi / 60)

P_5000_expr = (B_2000_solution**2 * d_nickel**2 * sigma_nickel * omega_5000**2) / 2
P_10000_expr = (B_2000_solution**2 * d_nickel**2 * sigma_nickel * omega_10000**2) / 2

Q_5000 = P_5000_expr * t
Q_10000 = P_10000_expr * t

delta_T_5000 = Q_5000 / (m_water * c_water)
delta_T_10000 = Q_10000 / (m_water * c_water)

B_550_solution, B_2000_solution, delta_T_5000.evalf(), delta_T_10000.evalf(), delta_T_custom.evalf()

print("Estimated B from 550 RPM trials (T):", B_550_solution)
print("Estimated B from 2000 RPM trials (T):", B_2000_solution)
print("Predicted ΔT for 5000 RPM (°C):", delta_T_5000.evalf())
print("Predicted ΔT for 10,000 RPM (°C):", delta_T_10000.evalf())
print(f"Predicted ΔT for {custom_rpm} RPM (°C):", delta_T_custom.evalf())

