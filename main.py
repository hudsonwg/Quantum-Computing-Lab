from qiskit import QuantumCircuit, assemble, Aer, QuantumCircuit
from qiskit.visualization import plot_histogram, plot_bloch_vector
from qiskit.providers.aer.library import save_statevector
from math import sqrt, pi
import matplotlib.pyplot as plt

def basic_quantum_circuit():
    # create a quantum circuit with a single qubit
    qc = QuantumCircuit(1)
    # changes initial state from default |0> to |1>
    initial_state = [0, 1]
    # initiialize 0th qubit (first qubit in circuit
    qc.initialize(initial_state, 0)
    # now visualize the circuit
    print(qc.draw(output="text"))
    # now call AER simulator,
    sim = Aer.get_backend('aer_simulator')
    # apply the quantum circuit to the simulator
    qc.save_statevector()
    qobj = assemble(qc)
    # measure qubit and save the result
    result = sim.run(qobj).result()
    out_state = result.get_statevector()
    # display result
    print(out_state)
    qc.measure_all()
    qc.draw(output="mpl")
    plt.show()
    # now lets check the counts for 0 and 1, using get_counts()
    counts = result.get_counts()
    plot_histogram(counts)
    plt.show()
    # the above plot shows a 100% chance of measuring a 1, because our quantum circuit forces the 1 state
def starter_superposition():
    #let's define the state |q_> as a vector of nonzero probabilities
    initial_state = [1/sqrt(2), 1j/sqrt(2)]

    qc = QuantumCircuit(1) #create single qubit circuit
    qc.initialize(initial_state, 0) #initialize 0th qubit to initial state vector
    qc.save_statevector()
    qobj = assemble(qc) #run sim
    sim = Aer.get_backend('aer_simulator') #open sim session
    state = sim.run(qobj).result().get_statevector() #run the circuit on the sim
    print(state) #check the state vector

    #now, lets view the probabilities in histogram form
    qobj = assemble(qc)
    results = sim.run(qobj).result().get_counts()
    plot_histogram(results)
    plt.show()
    #you can see now that the probability of measuring |0> vs |1> is equal



if __name__ == '__main__':
    #first, let's create a boring old basic quantum circuit, and measure it's states
    #basic_quantum_circuit()

    #now, let's try putting out qubit into a superposition, its about to get cool I think
    starter_superposition()