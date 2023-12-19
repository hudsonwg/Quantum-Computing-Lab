%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
NOTES ON QUANTUM
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


================
TO DO

- brush up on bra-ket notation
- learn complex conjugate
- maybe imaginary numbers in general
- shors algorithm, grovers algorithm

================
BASICS

quantum computers aren't binary in their bits, they just must output a binary representation when extracting information

the intuition is to use probability vectors, to represent quantum states. A classical example (which isn't practical but illustrates the concept well) is the position of an object, which we can represent with a coordinate classically.

the quantum state vector of this objects position would be the probability that the object exists in all positions, in this case a vector of zeros except at the position the object is at which would be a 1

=======================
BASIC REVIEW OF VECTORS

some two vectors are linearly independent if they cannot be described in terms of one another. 

Two linearly independent vectors in R2 for example, form a "basis" for R2, as a linear combination of the two can describe all points in R2

Orthonormal vectors are normalized (magnitude 1), orthogonal (linearly independent/right angle)

A qubit "statevector" is a linear combination of basis vectors

|q0> = n|0> + m|1>

USES BRA-KET NOTATION, REVISIT THIS IF CONFUSED

================
QISKIT INTRO

in Qiskit, use the quantum circuit object for circs. vector of ops + qstate vectors they operate on

qbits always start in the state |0>, we muse use initialize() to state them

NOTE: python uses j to represent i in complex numbers, vectors will be output as a float + floatingj, (i.e. [0.+0.j])

==============================
IMPORTANT RULE FOR MEASUREMENT

to find some probability of measuring a state |n> in the state |x> we can compute p(|x>) = |<x|n>|^2

<| means row vector called a bra (remember bras and kets), all kets |a> have a corresponding bra <a| and we can convert between them using the conjugate transpose. Kets are column vectors bras are row vectors


