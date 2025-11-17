# Applications-of-Spin-Dynamics-in-Quantum-Systems
This repo contains the applications of Spin Dynamics and Quantum Systems, a project which me and my team worked on together for our QM porject (Sem1).
<img width="1090" height="735" alt="image" src="https://github.com/user-attachments/assets/1e6ec7ee-61b4-4b1e-a42f-8677ac17abb2" />

The above simulation shows the precession of a spin around external magnetic field. When magnetic field is applied spin magnetic moment  doesn’t just align with it . It rotates and precesses around field direction
The arrow (magnetization vector ) on the Bloch sphere represents the net direction of many spins. Along with the time , arrow rotates around the z-axis shows spin precession.  The path of the tip of this arrow forms a circular trajectory — that’s the precession motion. This visualization helps connect quantum spin behavior with real physical systems like MRI.  
If we increase the magnetic field (Larmor Frequency) , the precession becomes faster. In MRI scanners, this frequency determines the resonance condition — meaning how the radiofrequency pulses interact with spins.

# Magnetization Components:
The total magnetization vector M can be broken down into three components:
```
M = (Mx, My, Mz)
```
(a) Mz - Longitudinal Magnetization
This represents the component in the direction of the magnetic field, represented by the z-axis and signifies how much the spins are aligned or opposed to the direction of the field. In the simulation above, Mz remains constant because there is no relaxation and no energy given off to surroundings. In the context of MRI, Mz will return to equilibrium after a pulse or perturbation, which is called T1 relaxation. 

(b) Mx and My - Transverse Magnetization

These two components represent the spin vector in the prependicular direction to the magnetic field, specifically in the x-y plane. Together, Mx and Mz represent the rotating or precessing part of the spin vector. As seen in the graphs with respect to Mx and My, these two components oscillate in a sine wave pattern which is the mathematical expression of precession.
The combined transverse magnetization is defined as :
```
|Mxy|=sqrt[(Mx)^2+(My)^2]
```
# In MRI and NMR:
It is the transverse magnetization, Mxy, that induces an electric signal in the detector coil. This is the signal converted into the image or spectrum.
### The above  simulation shows  the physics behind MRI and NMR:
In MRI, hydrogen nuclei-protons-inside the human body behave just like the spins in this simulation. The Larmor frequency identifies the nuclei that resonate with the radiofrequency pulse. Mx and My, the transverse magnetization, produce measurable electromagnetic signals. These signals are analyzed by MRI machines to reconstruct detailed images of tissues.

# The Graphical Interpretation of the above Code:
The above code plots four graphs:
1. Mx vs Time → Oscillating sine curve (which represents the rotating x-component)
2. My vs Time → Cosine curve (which shows 90° phase shift with respect to Mx)
3. Mz vs Time → Constant (no change without relaxation)
4. |Mxy| vs Time → Constant magnitude (which shows pure precession without any decay)
Future work :
In future, This part of the project can be expanded by exploring more applications through advanced simulations.

# References:
1.	https://users.dimi.uniud.it/~antonio.dangelo/MMS/materials/magnetic_risonance_imaging.pdf
2.	http://csci.ucsd.edu/courses/cogs260w2018/files/lecture-04/Lecture4_Readings_Chap14.pdf

1.	https://users.dimi.uniud.it/~antonio.dangelo/MMS/materials/magnetic_risonance_imaging.pdf
2.	http://csci.ucsd.edu/courses/cogs260w2018/files/lecture-04/Lecture4_Readings_Chap14.pdf
