Eddy Current Heat Estimator

This Python script estimates the heat generated in a nickel sample due to eddy currents caused by a rotating magnetic disc. It is designed to help analyze and predict the temperature increase in water placed above the disc over a given time period (e.g., 5 minutes), based on disc RPM and magnetic field parameters.

🔬 Project Overview

Eddy currents are loops of electrical current induced within conductors by a changing magnetic field. This script models the resulting Joule heating in a small nickel sample, which then transfers heat to surrounding water. The project aims to predict:
	•	The power generated via eddy currents.
	•	Temperature increase of the nickel sample.
	•	Estimated final water temperature after heat transfer.

This tool is ideal for physics experiments, educational demonstrations, and validating hypotheses in laboratory setups.

⚙️ Features
	•	Input-driven modeling based on RPM, magnetic field strength, sample mass, and more.
	•	Calculates magnetic frequency, power from eddy currents, and heating over time.
	•	Estimates water temperature increase from energy transferred by nickel.
	•	Adjustable parameters for rapid experimentation and hypothesis testing.

📚 Background

This project was originally developed as part of a physics-for-engineering course experiment, where we constructed a makeshift eddy current induction stove. The setup involved:
	•	A power drill to spin a disc embedded with alternating polarity magnets,
	•	A nickel sample placed inside a glass beaker of water above the rotating disc.

The goal was to explore how rotational magnetic fields induce eddy currents in a conductor, resulting in resistive heating.

While the mathematical modeling in the script is theoretically sound and aligned well with electromagnetic theory, the experimental results highlighted two key limitations:
	1.	Insufficient RPM — Our drill could not reach a high enough rotational speed to generate significant eddy currents using the relatively low-strength magnets we had available.
	2.	Thermal insulation — The glass beaker acted as a thermal barrier, significantly reducing the amount of heat transferred from the nickel to the water.

As a result, the experiment served more as a proof of concept rather than a fully functional induction heater. Nevertheless, the project provided valuable insights into energy conversion, magnetic field dynamics, and the challenges of experimental heat transfer — and the script remains useful for theoretical estimation, hypothesis testing, and instructional demonstrations.

🧠 Author

Kellen Jones
Veteran & Computer Science Student
Passionate about applied physics, energy systems, and experimental modeling.

📜 License

This project is licensed under the MIT License — see the LICENSE file for details.
